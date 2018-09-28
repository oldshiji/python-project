window.addEventListener("load",function () {


    //创建账号
    document.getElementById("register").addEventListener("click",function (e) {

        var data = {}
        data['accid'] = document.getElementsByName("accid")[0].value;
        data['name']  = document.getElementsByName("name")[0].value;
        data['mobile']= document.getElementsByName("mobile")[0].value;

        ajax({
            url:"http://127.0.0.1:8090/createaccid",
            async:true,
            data:{
                "accid":data['accid'],
                "name":data['name'],
                "mobile":data['mobile']
            },
            success:function(response){
                alert(response);
            },
            error:function(xhr){

            },
        });

    })

})