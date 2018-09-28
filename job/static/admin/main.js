$(function(){

    $("#url").validatebox({
        required:true,
        validType:"url",
        missingMessage:"请填写正确的链接地址",
        invalidMessage:"链接地址不正确"
    });

     $('#btn').bind('click', function(){


           $.messager.progress();	// 显示进度条

            $('#search').form('submit', {
                url:"/admin/search",
                onSubmit: function(){
                    var isValid = $(this).form('validate');
                    if (!isValid){
                        $.messager.progress('close');	// 如果表单是无效的则隐藏进度条
                    }
                    return isValid;	// 返回false终止表单提交
                },
                success: function(){
                    $.messager.progress('close');	// 如果提交成功则隐藏进度条
                }
            });
    });

     //字段添加对话框
    $("#field").click(function(e){
         //先弹出字段添加对话框
            $("#field-dialog").dialog({
                title: '字段管理',
                width: 1000,
                height: 650,
                closed: false,
                cache: false,
                href: '/admin/getField',
                modal: true

            });
    });


     $('#list').datagrid({
         toolbar: '#tb',
        fit:true,
		border:false,
		fitColumns:true,

		url:"/admin/getjoblist",

        columns:[[
            {
                field:'id',
                title:'ID',
                checkbox:true,
            },
            {
                field:'city_exp_edu',
                title:'城市-经验-学历',
                width:100,
                align:'center'
            },
            {
                field:'job_name',
                title:'职位名称',
                width:100,
                align:'center'
            },
            {
                field:'fancing_scale',
                title:'公司规模',
                width:100,
                align:'center'
            },{
                field:'company_name',
                title:'公司名称',
                width:100,
                align:'center'
            },{
                field:'compnay_position',
                title:'公司行业',
                width:100,
                align:'center'
            },{
                field:'hr_name',
                title:'hr名字',
                width:100,
                align:'center'
            },{
                field:'hr_position',
                title:'hr职位',
                width:100,
                align:'center'
            },{
                field:'experience',
                title:'工作经验',
                width:100,
                align:'center'
            },{
                field:'eduction',
                title:'学历',
                width:100,
                align:'center'
            },{
                field:'publish_time',
                title:'职位发布时间',
                width:100,
                align:'center'
            },{
                field:'add_time',
                title:'爬取时间',
                width:100,
                align:'center'
            },


        ]],
        data: [
            {
                "city":"北京",
                "job_name":"python"
            },
            {
                "city":"上海",
                "job_name":"php"
            }
        ],
         pagination:true,
		 pageSize:5,
		 pageList:[5,10,20,25,30],
		 pageNumber:1,
		 rownumbers:true,

    });



})