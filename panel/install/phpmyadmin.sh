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
Setup_Path=$Root_Path/server/phpmyadmin
webserver=""



Install_phpMyAdmin()
{
	if [ -d "${Root_Path}/server/apache"  ];then
		webserver='apache'
	elif [ -d "${Root_Path}/server/nginx"  ];then
		webserver='nginx'
	fi

	if [ "${webserver}" == "" ];then
		echo "No Web server installed!"
		exit 0;
	fi
	wget -O phpMyAdmin.zip $download_Url/src/phpMyAdmin-${1}.zip -T20
	mkdir -p $Setup_Path

	unzip -o phpMyAdmin.zip -d $Setup_Path/ > /dev/null
	rm -f phpMyAdmin.zip
	rm -rf $Root_Path/server/phpmyadmin/phpmyadmin*
	
	
	phpmyadminExt=`cat /dev/urandom | head -n 32 | md5sum | head -c 16`;
	mv $Setup_Path/databaseAdmin $Setup_Path/phpmyadmin_$phpmyadminExt
	chmod -R 744 $Setup_Path/phpmyadmin_$phpmyadminExt
	chown -R www.www $Setup_Path/phpmyadmin_$phpmyadminExt
	
	secret=`cat /dev/urandom | head -n 32 | md5sum | head -c 32`;
	sed -i "s#^\$cfg\['blowfish_secret'\].*#\$cfg\['blowfish_secret'\] = '${secret}';#" $Setup_Path/phpmyadmin_$phpmyadminExt/config.sample.inc.php
	\cp -a -r $Setup_Path/phpmyadmin_$phpmyadminExt/config.sample.inc.php  $Setup_Path/phpmyadmin_$phpmyadminExt/config.inc.php
	sed -i "s#^\$cfg\['blowfish_secret'\].*#\$cfg\['blowfish_secret'\] = '${secret}';#" $Setup_Path/phpmyadmin_$phpmyadminExt/libraries/config.default.php
	
	echo $1 > $Setup_Path/version.pl
	
	PHPVersion=""
	if [ -f "$Root_Path/server/php/52/bin/php" ];then
		PHPVersion="52"
	fi
	if [ -f "$Root_Path/server/php/53/bin/php" ];then
		PHPVersion="53"
	fi
	if [ -f "$Root_Path/server/php/54/bin/php" ];then
		PHPVersion="54"
	fi
	if [ -f "$Root_Path/server/php/55/bin/php" ];then
		PHPVersion="55"
	fi
	if [ -f "$Root_Path/server/php/56/bin/php" ];then
		PHPVersion="56"
	fi
	if [ -f "$Root_Path/server/php/70/bin/php" ];then
		PHPVersion="70"
	fi
	if [ -f "$Root_Path/server/php/71/bin/php" ];then
		PHPVersion="71"
	fi
	if [ -f "$Root_Path/server/php/72/bin/php" ];then
		PHPVersion="72"
	fi

	if [ "${webserver}" == "nginx" ];then
		sed -i "s#$Root_Path/wwwroot/default#$Root_Path/server/phpmyadmin#" $Root_Path/server/nginx/conf/nginx.conf
		rm -f $Root_Path/server/nginx/conf/enable-php.conf
		\cp $Root_Path/server/nginx/conf/enable-php-$PHPVersion.conf $Root_Path/server/nginx/conf/enable-php.conf
		sed -i "/pathinfo/d" $Root_Path/server/nginx/conf/enable-php.conf
		/etc/init.d/nginx reload
	else
		sed -i "s#$Root_Path/wwwroot/default#$Root_Path/server/phpmyadmin#" $Root_Path/server/apache/conf/extra/httpd-vhosts.conf
		sed -i "0,/php-cgi/ s/php-cgi-\w*\.sock/php-cgi-${PHPVersion}.sock/" $Root_Path/server/apache/conf/extra/httpd-vhosts.conf
		/etc/init.d/httpd reload
	fi
	
	
	
	if [ -f "/etc/init.d/iptables" ];then
		isstart=`/etc/init.d/iptables status|grep 'Firewall modules are not loaded'`
		if [ "$isstart" = '' ];then
			iptables -I INPUT -p tcp -m state --state NEW -m tcp --dport 888 -j ACCEPT
			/etc/init.d/iptables save

			iptables_status=`/etc/init.d/iptables status | grep 'not running'`
			if [ "${iptables_status}" == '' ];then
				/etc/init.d/iptables stop
				/etc/init.d/iptables start
			fi
		fi
	fi

	if [ "$isVersion" == '' ];then
		if [ ! -f "/etc/init.d/iptables" ];then
			firewall-cmd --permanent --zone=public --add-port=888/tcp
			firewall-cmd --reload
		fi
	fi
	
}

Uninstall_phpMyAdmin()
{
	rm -rf $Root_Path/server/phpmyadmin/phpmyadmin*
	rm -f $Root_Path/server/phpmyadmin/version.pl
}

actionType=$1
version=$2

if [ "$actionType" == 'install' ];then
	Install_phpMyAdmin $version
elif [ "$actionType" == 'uninstall' ];then
	Uninstall_phpMyAdmin
fi
