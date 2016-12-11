/**
 * Created by kakoka on 17.11.16.
 */

'use strict';

$(function () {
    $('#dialog').dialog({
        autoOpen: false,
        show: 'default',
        hide: 'default'
    });

    $(".item_add").click(function () {
        var product_id = $(this).attr('rel');

{#        alert('Будем параметр: ' + product_id);#}

        $.ajax({
            url: 'cart/add/',
            data: {product_id: product_id}, // передаваемые параметры в обработчик
            type: 'POST', // или GET - метод передачи данных
            headers: {'X-CSRFToken': document.getElementsByName('csrfmiddlewaretoken')[0].value},
            dataType: 'json', // тип данных в ожидаемом ответе
            success: function(results){
                var cart = JSON.parse(results);
                console.log(cart);
                // var json = $.parseJSON(response);
                // $.each(response, function (key, val) {
                //     console.log(key, val)
                // });
                // json = $.parseJSON(response);
                // console.log(json);
                // на самом деле, в data находится именно ваш ожидаемы ответ
                // от обработчика, но т.к. мы тут реальный ответ
                // использовать не можем, то используем ответ
                // созданный вручную - переменная ajaxResponse
                $('#dialog').dialog('open').html(cart); //, data.value.product_pk);
            }
        });
    });
});


