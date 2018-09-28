/**
 * Created by Administrator on 2015/1/26.
 */

$(function () {
///////datagrid选中行变色与鼠标经过行变色///////////////
            var dtSelector = ".table.default";
            var tbList = $(dtSelector);


            tbList.each(function () {
                var self = this;
// 鼠标经过的行变色
                $("tr:not(:first)", $(self)).hover(
                        function () {
                            $(this).addClass('hoverTD');
                            $(this).removeClass('table-td-content');

                        },
                        function () {
                            $(this).removeClass('hoverTD');
                            $(this).addClass('table-td-content');

                        }
                );

// 选择行变色
                $("tr", $(self)).click(function () {
                    var trThis = this;
                    $(self).find(".trSelected").removeClass('trSelected');
                    if ($(trThis).get(0) == $("tr:first", $(self)).get(0)) {
                        return;
                    }
                    $(trThis).addClass('trSelected');
                    selected_row_id = $(self).find(".trSelected").attr('id');
                });
            });
        });

