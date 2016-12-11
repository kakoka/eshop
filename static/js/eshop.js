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

////


simpleCart.bind( "afterAdd" , function( item ) {
    var product_id = item.get("pk");
    $.ajax({
        url: '{% url "add" %}',
        data: {product_id: product_id}, // передаваемые параметры в обработчик
        type: 'POST', // или GET - метод передачи данных
        headers: {'X-CSRFToken': document.getElementsByName('csrfmiddlewaretoken')[0].value},
        dataType: 'json', // тип данных в ожидаемом ответе
        success: function (results) {
            var cart = JSON.parse(results);
            console.log(cart);
            }
            });
        });

    // remove item from cart
    simpleCart.bind( "beforeRemove" , function( item ) {
    var product_id = item.get("pk");
    $.ajax({
        url: '{% url "remove" %}',
        data: {product_id: product_id, quantity: 1},//{product_id: product_id}, // передаваемые параметры в обработчик
        type: 'POST', // или GET - метод передачи данных
        headers: {'X-CSRFToken': document.getElementsByName('csrfmiddlewaretoken')[0].value},
        dataType: 'json', // тип данных в ожидаемом ответе
        success: function () {
            console.log("Removed from cart!");
            }
            });
        });

    simpleCart.bind( "simpleCart_empty" , function() {
        $.get( '{% url "empty" %}') });

    simpleCart.trigger( "beforeEmpty" );

    // непонятно как заставить ждать нажатия кнопки

    simpleCart.bind( "beforeCheckout" , function() {
        $('#dialog').dialog({
            modal:true,
            buttons:{
                Ok: function(){
                    $(this).dialog( "close" );
                    }
                }
        });
        $.get( '{% url "cart" %}', function( data ) {
            $( ".result" ).html( data );
            $('#dialog').dialog('open').html(data);
            });
        });


////


$email_message .= "\n".'========================================================'."\n";
$email_message .= 'Has placed an order as per below:'."\n";

for($i=1; $i < $content['itemCount'] + 1; $i++) {
$name = 'item_name_'.$i;
$sname = 'item_sname_'.$i;
$quantity = 'item_quantity_'.$i;
$price = 'item_price_'.$i;
$total = $content[$quantity]*$content[$price];
$grandTotal += $total;
$body .= 'Order #'.$i.':: Style: '.$content[$sname].': Color: '.$content[$name].' --- Qty x     '.$content[$quantity].' --- Unit Price $'.number_format($content[$price], 2, '.', '').' --- Subtotal $'.number_format($total, 2, '.', '')."\n";
$body .= '========================================================'."\n";