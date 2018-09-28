#!/bin/bash
PATH=/bin:/sbin:/usr/bin:/usr/sbin:/usr/local/bin:/usr/local/sbin:~/bin
export PATH
public_file=/www/server/panel/install/public.sh
if [ ! -f $public_file ];then
	wget -O $public_file http://download.bt.cn/install/public.sh -T 5;
fi
. $public_file

download_Url=$NODE_URL
Root_Path=`cat /var/bt_setupPath.conf`
Setup_Path=$Root_Path/server/apache
run_path="/root"
Is_64bit=`getconf LONG_BIT`
apacheVersion='2.4.26'
apache_22_version='2.2.34'
centos_version=`cat /etc/redhat-release | grep ' 7.' | grep -i centos`
if [ "${centos_version}" != '' ]; then
	rpm_path="centos7"
else
	rpm_path="centos6"
fi

Mpm_Opt(){
	MemInfo=$(free -g |grep Mem |awk '{print $2}')
	ServerLimit=$((400*(1+${MemInfo})))
	echo "ServerLimit" ${ServerLimit} >> ${Setup_Path}/conf/httpd.conf
	wget -O ${Setup_Path}/conf/extra/httpd-mpm.conf ${download_Url}/conf/httpd-mpm.conf
	sed -i 's/$work/'${ServerLimit}'/g' ${Setup_Path}/conf/extra/httpd-mpm.conf 
}

Install_OpenSSL()
{
	openssl_version=`cat /usr/local/openssl/version.pl`
    if [ "${openssl_version}" != '1.0.2l_shared' ];then
    	rm -rf /usr/local/openssl
        cd ${run_path}
        wget ${download_Url}/src/openssl-1.0.2l.tar.gz -T 20
        tar -zxf openssl-1.0.2l.tar.gz
        rm -f openssl-1.0.2l.tar.gz
        cd openssl-1.0.2l
        ./config --openssldir=/usr/local/openssl zlib-dynamic shared
        make && make install
        echo '1.0.2l_shared' > /usr/local/openssl/version.pl
        cd ..
        rm -rf openssl-1.0.2l
    fi
cat > /etc/ld.so.conf.d/openssl.conf <<EOF
/usr/local/openssl/lib
EOF
ldconfig
}

Install_Nghttp2()
{
	if [ ! -f /usr/local/nghttp2/version.pl ];then
		wget ${download_Url}/src/nghttp2-1.22.0.tar.gz
		tar -zxf nghttp2-1.22.0.tar.gz
		cd nghttp2-1.22.0
		./configure --prefix=/usr/local/nghttp2
		make && make install
		ln -sf /usr/local/nghttp2/lib/libnghttp2.so.14 /usr/lib/libnghttp2.so.14
		ln -sf /usr/local/nghttp2/lib/libnghttp2.so.14 /usr/lib64/libnghttp2.so.14
		echo '1.22.0' > /usr/local/nghttp2/version.pl
		cd ..
		rm -rf nghttp2-1.22.0*
	fi
}


Install_Apache_24()
{
	Uninstall_Apache
	cd ${run_path}
	Run_User="www"
    groupadd ${Run_User}
    useradd -s /sbin/nologin -g ${Run_User} ${Run_User}
	
	mkdir -p ${Setup_Path}
	rm -rf ${Setup_Path}/*
	rm -f /etc/init.d/httpd
	wget ${download_Url}/rpm/${rpm_path}/${Is_64bit}/bt-httpd-2.4.25.rpm
	rpm -ivh bt-httpd-2.4.25.rpm --force --nodeps
	rm -f bt-httpd-2.4.25.rpm


    mv ${Setup_Path}/conf/httpd.conf ${Setup_Path}/conf/httpd.conf.bak
	
	wget -O ${Setup_Path}/conf/httpd.conf ${download_Url}/conf/httpd24.conf -T 20
	wget -O ${Setup_Path}/conf/extra/httpd-vhosts.conf ${download_Url}/conf/httpd-vhosts.conf -T 20
	wget -O ${Setup_Path}/conf/extra/httpd-default.conf ${download_Url}/conf/httpd-default.conf -T 20
	wget -O ${Setup_Path}/conf/extra/mod_remoteip.conf ${download_Url}/conf/mod_remoteip.conf -T 20
	Mpm_Opt
    mkdir ${Setup_Path}/conf/vhost
	chmod -R 755 ${Setup_Path}/conf/vhost
	mkdir -p $Root_Path/wwwroot/default
	mkdir -p $Root_Path/wwwlogs
	mkdir -p $Root_Path/server/phpmyadmin
	mkdir -p $Root_Path/server/pass
	chmod -R 755 $Root_Path/wwwroot/default
	chown -R www.www $Root_Path/wwwroot/default
	sed -i "s#/www/wwwroot/default#$Root_Path/server/phpmyadmin#" ${Setup_Path}/conf/extra/httpd-vhosts.conf
	sed -i "s#IncludeOptional conf/vhost/\*\.conf#IncludeOptional /www/server/panel/vhost/apache/\*\.conf#" ${Setup_Path}/conf/httpd.conf
	
	CheckPHPVersion
	wget -O $Root_Path/server/apache/htdocs/index.html ${download_Url}/error/index.html -T 20
	wget -O /etc/init.d/httpd ${download_Url}/init/init.d.httpd -T20
    chmod +x /etc/init.d/httpd
	chkconfig --add httpd
	chkconfig --level 2345 httpd on
	cd ${Setup_Path}
	rm -f src.tar.gz
	echo "2.4" > ${Setup_Path}/version.pl
}

Install_Apache_22()
{
	Uninstall_Apache
	cd ${run_path}
	Run_User="www"
    groupadd ${Run_User}
    useradd -s /sbin/nologin -g ${Run_User} ${Run_User}
    
    mkdir -p ${Setup_Path}
	rm -rf ${Setup_Path}/*
	rm -f /etc/init.d/httpd
	cd ${Setup_Path}
	if [ ! -f "${Setup_Path}/src.tar.gz" ];then
		wget -O ${Setup_Path}/src.tar.gz ${download_Url}/src/httpd-${apache_22_version}.tar.gz -T20
	fi
	tar -zxvf src.tar.gz
	mv httpd-${apache_22_version} src
	cd src
    ./configure --prefix=${Setup_Path} --enable-mods-shared=most --with-ssl=/usr/local/openssl --enable-headers --enable-mime-magic --enable-proxy --enable-so --enable-rewrite --enable-ssl --enable-deflate --enable-suexec --with-included-apr --with-mpm=prefork --with-expat=builtin
    make && make install
	
	if [ ! -f "${Setup_Path}/bin/httpd" ];then
		echo '========================================================'
		echo -e "\033[31mERROR: apache-${apache_22_version} installation failed.\033[0m";
		rm -rf ${Setup_Path}
		exit 0;
	fi

    mv ${Setup_Path}/conf/httpd.conf ${Setup_Path}/conf/httpd.conf.bak
	wget -O ${Setup_Path}/conf/httpd.conf ${download_Url}/conf/httpd22.conf -T20
	wget -O ${Setup_Path}/conf/extra/httpd-vhosts.conf ${download_Url}/conf/httpd-vhosts-22.conf -T20
	wget -O ${Setup_Path}/conf/extra/httpd-default.conf ${download_Url}/conf/httpd-default.conf -T20
	wget -O ${Setup_Path}/conf/extra/mod_remoteip.conf ${download_Url}/conf/mod_remoteip.conf -T20
	sed -i "s#Include conf/vhost/\*\.conf#Include /www/server/panel/vhost/apache/\*\.conf#" ${Setup_Path}/conf/httpd.conf
	sed -i "s#/www/wwwroot/default#/www/server/phpmyadmin#" ${Setup_Path}/conf/extra/httpd-vhosts.conf
	sed -i '/LoadModule php5_module/s/^/#/' ${Setup_Path}/conf/httpd.conf

    mkdir -p ${Setup_Path}/conf/vhost
	mkdir -p $Root_Path/wwwroot/default
	mkdir -p $Root_Path/wwwlogs
	chmod -R 755 $Root_Path/wwwroot/default
	chown -R www.www $Root_Path/wwwroot/default

    ln -sf /usr/local/lib/libltdl.so.3 /usr/lib/libltdl.so.3
    mkdir ${Setup_Path}/conf/vhost

	wget -O ${Setup_Path}/htdocs/index.html ${download_Url}/error/index.html -T20
	wget -O /etc/init.d/httpd ${download_Url}/init/init.d.httpd -T20
    chmod +x /etc/init.d/httpd
	chkconfig --add httpd
	chkconfig --level 2345 httpd on
	
	cd ${Setup_Path}
	rm -f src.tar.gz
	echo "2.2" > ${Setup_Path}/version.pl
	echo '2.2' > /var/bt_apacheVersion.pl
	cat > /www/server/panel/vhost/apache/phpinfo.conf <<EOF
<VirtualHost *:80>
DocumentRoot "/www/server/phpinfo"
ServerAdmin phpinfo
ServerName 127.0.0.2
<Directory "/www/server/phpinfo">
    SetOutputFilter DEFLATE
    Options FollowSymLinks
    AllowOverride All
    Order allow,deny
    Allow from all
    DirectoryIndex index.php index.html index.htm default.php default.html default.htm
</Directory>
</VirtualHost>
EOF
	if [ -f "/www/server/php/52/libphp5.so" ];then
		\cp -a -r /www/server/php/52/libphp5.so /www/server/apache/modules/libphp5.so
		sed -i '/#LoadModule php5_module/s/^#//' ${Setup_Path}/conf/httpd.conf
	fi
	if [ -f "/www/server/php/53/libphp5.so" ];then
		\cp -a -r /www/server/php/53/libphp5.so /www/server/apache/modules/libphp5.so
		sed -i '/#LoadModule php5_module/s/^#//' ${Setup_Path}/conf/httpd.conf
	fi
	if [ -f "/www/server/php/54/libphp5.so" ];then
		\cp -a -r /www/server/php/54/libphp5.so /www/server/apache/modules/libphp5.so
		sed -i '/#LoadModule php5_module/s/^#//' ${Setup_Path}/conf/httpd.conf
	fi
	
	if [ -f /www/server/apache/modules/libphp5.so ];then
		/etc/init.d/httpd start
	fi
}

CheckPHPVersion()
{
	PHPVersion=""
	if [ -d "/www/server/php/52/bin" ];then
		PHPVersion="52"
	fi
	if [ -d "/www/server/php/53/bin" ];then
		PHPVersion="53"
	fi
	if [ -d "/www/server/php/54/bin" ];then
		PHPVersion="54"
	fi
	if [ -d "/www/server/php/55/bin" ];then
		PHPVersion="55"
	fi
	if [ -d "/www/server/php/56/bin" ];then
		PHPVersion="56"
	fi
	if [ -d "/www/server/php/70/bin" ];then
		PHPVersion="70"
	fi
	if [ -d "/www/server/php/71/bin" ];then
		PHPVersion="71"
	fi
	if [ -d "/www/server/php/72/bin" ];then
		PHPVersion="72"
	fi
	if [ "${PHPVersion}" != '' ];then
		sed -i "s#VERSION#$PHPVersion#" ${Setup_Path}/conf/extra/httpd-vhosts.conf
	fi
}

Uninstall_Apache()
{
	service httpd stop
	pkill -9 httpd
	chkconfig --del httpd
	rm -rf $Setup_Path
	rm -f /etc/init.d/httpd
	rm -f /www/server/panel/vhost/apache/phpinfo.conf
}

actionType=$1
version=$2

if [ "$actionType" == 'install' ];then
	Install_OpenSSL
	Install_OpenSSL
	Install_Nghttp2
	if [ "$version" == '2.2' ]; then
		Install_Apache_22
	else
		Install_Apache_24
	fi
	
	/etc/init.d/httpd start
else 
	if [ "$actionType" == 'uninstall' ];then
	Uninstall_Apache
	fi
fi
