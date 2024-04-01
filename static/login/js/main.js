$login = $("#login")
$check_code = $("#check-code")
$phone_number_invalid = $("#phone-number-invalid")
$next = $(".next")
$confirm_code = $("#confirm-code-button")
$phone_number = $("#phone-number-input")
$(".number").on("input", function () {
    $(this).next().focus()
})
$confirm_code.on("click", function () {
    code = ""
    $(".number").each(function (idx, number) {

        $(number).val()
        code += $(number).val()
        // and the rest of your code
    });
    console.log($phone_number.val())
    console.log(code)

    var form = new FormData();
    form.append("phone_number", $phone_number.val());
    form.append("code", code);

    var settings = {
        "url": "http://127.0.0.1:8000/api/check_code/",
        "method": "POST",
        "timeout": 0,
        "processData": false,
        "mimeType": "multipart/form-data",
        "contentType": false,
        "data": form
    };

    $.ajax(settings).done(function (response) {
        console.log(response);
    });
})

$("#username-login").on("click", function () {
    $login.addClass("right-panel-active")
    $login.removeClass("left-panel-active")

    $phone_number_invalid.css('opacity', '0')
})
$("#phone-login").on("click", function () {
    $login.removeClass("right-panel-active")
    $login.addClass("left-panel-active")

})

$("#login-pn-button").on("click", function () {

    console.log($phone_number.val())

    var form = new FormData();
    form.append("phone_number", $phone_number.val());

    var settings = {
        "url": "http://127.0.0.1:8000/api/phone_number_login/",
        "method": "POST",
        "timeout": 0,
        "processData": false,
        "mimeType": "multipart/form-data",
        "contentType": false,
        "data": form
    };

    $.ajax(settings).done(function (response) {
        console.log(response);
        $check_code.removeClass("hidden")
        $login.addClass("hidden")
        $("#number-1").focus()
    }).fail(function (jqXHR, textStatus, errorThrown) {
        console.log(textStatus)
        $phone_number_invalid.css('opacity', '1')

    })
})

