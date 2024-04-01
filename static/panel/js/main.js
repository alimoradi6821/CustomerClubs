$welcome_msg = $("#welcome-text")
$btn_edit_welcome_msg = $("#btn-edit-wel-msg")
$(document).ready(function () {

    var settings_customer = {
        "url": "http://127.0.0.1:8000/api/customer/",
        "method": "GET",
        "timeout": 0,
        "headers": {
            "Authorization": "Token 37996b1a9f880bf33748c1e6a2d93c709ae40aaf"
        },
        "processData": false,
        "mimeType": "multipart/form-data",
        "contentType": false,
    };

    $.ajax(settings_customer).done(function (response) {
        console.log(response);

        var json = JSON.parse(response);
        $.each(json, function (index, obj) {
            console.log(obj["person"])
            var fname = ''
            var lname = ''
            var point = ''
            var condtion = 'فعال'
            var customer_group = ''
            if (obj["first_name"] !== null) {

                console.log(obj["person"])
                fname = obj["first_name"]
            }

            if (obj["last_name"] !== null) {

                console.log(obj["person"])
                lname = obj["last_name"]
            }
            if (obj["point"] !== null) {

                console.log(obj["point"])
                point = obj["point"]
            }
            if (obj["customer_group"] !== null) {

                console.log(obj["point"])
                point = obj["customer_group"]
            }
            if (obj["active"] === false) {

                console.log(obj["point"])
                condtion = 'غیر فعال'
            }


            var row = '<tr><td> ' + fname + lname + ' </td> <td> ' + obj["person"] + ' </td> <td>' + point + '</td> <td>' + customer_group + '</td>  <td>' + condtion + '</td> </tr>'
            $("#customer-table tbody").append(row);
        });
        $('.table').DataTable();

    });

    var settings_wel_msg = {
        "url": "http://127.0.0.1:8000/api/welcome_msg/",
        "method": "GET",
        "timeout": 0,
        "headers": {
            "Authorization": "Token 37996b1a9f880bf33748c1e6a2d93c709ae40aaf"
        },
        "processData": false,
        "mimeType": "multipart/form-data",
        "contentType": false,
    };

    $.ajax(settings_wel_msg).done(function (response) {
        console.log(response);
        var json = JSON.parse(response);
        $welcome_msg.text(json[0]["welcome_message"])
          $btn_edit_welcome_msg.attr('disabled','')
    });
});

$btn_edit_welcome_msg.on("click", function () {
    console.log($welcome_msg.val())
    var settings = {
        "url": `http://127.0.0.1:8000/api/welcome_msg/${$welcome_msg.val()}/`,
        "method": "PATCH",
        "timeout": 0,
        "headers": {
            "Authorization": "Token 37996b1a9f880bf33748c1e6a2d93c709ae40aaf"
        },
    };

    $.ajax(settings).done(function (response) {
        console.log(response);
        $("#alert").dialog();
    });
})
$welcome_msg.on('input',function () {
    $btn_edit_welcome_msg.removeAttr('disabled')
})