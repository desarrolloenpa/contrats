function load_page(url) {
    var _url = "../" + url;
    document.getElementById("main-iframe").src = _url;
}

function Fajax(div, url, data) {
    $("#" + div).html("<div class='loading'>Loading...</div>");
    $(".loading").show();

    $.ajax({
        url: url,
        data: data,
        type: 'GET',
        dataType: "html",
        success: function (data) {
            $(".loading").hide();
            $("#" + div).html(data)
        },
        error: function (xhr, errmsg, err) {
            $(".loading").hide();
            console.log(xhr.status + ": " + xhr.responseText);
            $("#" + div).html("<div class='alert alert-danger'></>Error: " + xhr.responseText + "</div>");
        }
    });
}


function isNumeric(keyCode, Acceptedkey) {
    if (Acceptedkey.includes(keyCode)) {
        return true
    }
    if (keyCode >= 48 && keyCode <= 57) {
        return true
    }
    return false
}


function error_messages(content) {
    $.confirm({
        title: 'Encontrado un error!',
        content: content,
        icon: 'fa fa-warning',
        type: 'red',
        buttons: {
            omg: {
                text: 'Aceptar',
                btnClass: 'btn-red',
            },
        }
    });
}


$(document).ready(function () {
    $('.input-float').keydown(function (event) {
        // teclas especiales backspace, tabulador, return, izquierda, derecha, suprimir, -, .
        var Acceptedkey = [8, 9, 13, 46, 127, 173, 189, 190, 97, 98, 99, 100, 101, 102, 103, 104, 105, 96, 110,
							48, 49, 50, 51, 52, 53, 54, 56, 57, 58]
        if (!isNumeric(event.keyCode, Acceptedkey)) {
            event.preventDefault()
        }
    })
    $('.input-float').blur(function () {
        var patter = /^(\d+(.{0,1}\d{0,2})?)$/
        if (!patter.test($(this).val())) {
            $(this).addClass('border-danger')
            $(this).val('')
            return false
        }
    })
    $('.input-float').focus(function () {
        $(this).removeClass('border-danger')
        $(this).addClass('border-normal')
    })

    $('.input-counter').keydown(function (event) {
        var Acceptedkey = [8, 9, 13, 127, 173, 189, 190, 97, 98, 99, 100, 101, 102, 103, 104, 105, 96, 110, 
							48, 49, 50, 51, 52, 53, 54, 56, 57, 58]
        if (!isNumeric(event.which, Acceptedkey)) {
            event.preventDefault()
        }
    })
    $('.input-counter').blur(function () {
        var patter = /^\d{1,4}$/
        if (!patter.test($(this).val())) {
            $(this).addClass('border-danger')
            $(this).val('')
            return false
        }
    })
    $('.input-counter').focus(function () {
        $(this).removeClass('border-danger')
        $(this).addClass('border-normal')
    })

    $('.input-number').keydown(function (event) {
        var Acceptedkey = [8, 9, 13, 127, 173, 189, 190, 97, 98, 99, 100, 101, 102, 103, 104, 105, 96, 110]
        if (!isNumeric(event.which, Acceptedkey)) {
            event.preventDefault()
        }
    })
    $('.input-number').blur(function () {
        var patter = /^\d{2,4}$/
        if (!patter.test($(this).val())) {
            $(this).addClass('border-danger')
            this.val('')
            return false
        }
    })
    $('.input-number').focus(function () {
        $(this).removeClass('border-danger')
        $(this).addClass('border-normal')
    })
})

