function getCookie(name) {
    var r = document.cookie.match("\\b" + name + "=([^;]*)\\b");
    return r ? r[1] : undefined;
}

function updateCategoryList(after_success_func) {
    $.post(
        "/category/list",
        {_xsrf: getCookie("_xsrf")},
        function (data) {
            var categories = data
            $("#categorylist").children().remove()
            var innerHtml = "";
            for (var i = 0; i < categories.length; i++) {
                innerHtml += "<li><label class='checkbox text-justify'><input value='" + categories[i].id + "' type='checkbox' name='post_category[]' id='post_category_" + categories[i].id + "'/>" + categories[i].name + "</label></li>";

//                if (categories[i].parent == 0) {
//                    innerHtml += "<li><label class='checkbox'><input value='" + categories[i].id + "' type='checkbox' name='post_category[]' id='post_category_" + categories[i].id + "'/>" + categories[i].name + "</label>";
//
//                    innerHtml += "<ul class='nav list-group'>";
//                    for (j = 0; j < categories.length; j++) {
//                        if (categories[j].parent == categories[i].id) {
//                            innerHtml += "<li><label class='checkbox'><input value='" + categories[j].id + "' type='checkbox' name='post_category[]' id='post_category_" + categories[j].id + "'/>" + categories[j].name + "</label></li>";
//                        }
//                    }
//                    innerHtml += "</ul></li>";
//                }
            }
            $("#categorylist").append(innerHtml);
            if (after_success_func)
                after_success_func();
        }
    );
}
$(function () {
    $("#category_quick_add").click(function () {
        var name = $("#new_category").val();
        if (name == "") {
            alert("please input the category name!");
            return;
        }
        _xsrf__ = getCookie("_xsrf");
        var selectedItems = new Array();
        $("input[name='post_category[]']:checked").each(function () {
            selectedItems.push($(this).val());
        });
        if (selectedItems.length == 0)
            selectedItems.push(0);
        $.post("/admin/category/quickadd",
            {_xsrf: _xsrf__,
                name: $("#new_category").val(),
                parent: selectedItems.join(",")},
            function (data, textStatus, jqXHR) {
                updateCategoryList(function () {
                    //new_category_name = $("#new_category").val();
                    $("#new_category").val('')
                });
            });
    });
})