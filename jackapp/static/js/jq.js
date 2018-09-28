
function ajax(obj){

        xhr = new XMLHttpRequest();
        xhr.onreadystatechange = function (ev) {

            if(xhr.readyState==4){
                if (xhr.status==200){
                    //alert(xhr.responseText);
                    obj.success(xhr.responseText);
                }
            }

        };

        xhr.onerror = function (xhr) {
            obj.error(xhr);
        };

        xhr.open("post",obj.url,obj.async);

        xhr.setRequestHeader("Content-type","application/x-www-form-urlencoded;charset=utf-8");

        datastr = '';
        for(var item in obj.data){
            datastr+=item+"="+obj.data[item]+"&";
        }
        datastr = datastr.substr(0,datastr.length-1);
        xhr.send(datastr);

}