$(document).ready(function () {
    $("#livebox").on("input", function (e) {
        $("#datalist").empty();
        $.ajax({
            method: "post",
            url: "/search",
            data: {text: $("#livebox").val()},
            success: function (res) {
                let data = "<div class='chat-about'>";
                $.each(res, function (index, value) {
                    if (value) {
                        data += "<a href='#' type='submit' role='button' class='list-group-item list-group-item-action' id ='ajax-result' onclick='checker()'>" + value.name + ' ' + value.lastname + "</sub>";
                    } else {
                        data += "<p class='list-group-item list-group-item-action' id ='not followed' >" + "User not found" + "</p>";
                    }
                });
                data += "</div>";
                $("#datalist").html(data);
            }
        });
    });
    let checker = document.getElementById('livebox')
    $(checker).focusin(function () {
        $(this).css("background-color", "#FFFFCC");
    });
    $(checker).focusout(function () {
        const elements = document.getElementsByClassName('list-group-item list-group-item-action');
        while (elements.length > 0) {
            elements[0].parentNode.removeChild(elements[0]);
        }
    });
});