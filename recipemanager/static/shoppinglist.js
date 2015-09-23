$(document).ready(function() {

    var shoppingList = [];

    function getCookie(name) {
        var cookieValue = null;
        if (document.cookie && document.cookie != '') {
            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
                var cookie = jQuery.trim(cookies[i]);
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) == (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }

    function close_accordion_section() {
        $('.accordion .accordion-section-title').removeClass('active');
        $('.accordion .accordion-section-content').slideUp(300).removeClass('open');
    }

    $('.accordion-section-title').click(function(e) {

        var currentAttrValue = $(this).attr('href');

        if($(e.target).is('.active')) {
            close_accordion_section();
        }else {
            close_accordion_section();

            $(this).addClass('active');
            $('.accordion ' + currentAttrValue).slideDown(300).addClass('open');
        }

        e.preventDefault();
    });


    $("button#addItem").on("click", function () {
        var productName = $("#itembox").val();
        if (productName.length == 0) {
            alert('Please enter an item!');
            return;
        }
        var category = $("#aisleSelect").val();
        var listItem = $("#" + category + "-list");
        console.log(listItem);
        if (listItem) {
            listItem.append("<div id='list'><li class='" + category + "'> " + productName + "</li></div>");
        }
        if (listItem != undefined) {
            $("#categories").prepend(listItem.parent());
            $(listItem.parent()).show();
        }

        $("#itembox").keypress(function (e) {
            if (e.which == 13) {
                $("button#addItem").submit();
            }
        });

        $("#itembox").val("");

        $('#controls').fadeIn();

        var newItem = {
            name: productName,
            category: category
        };
        shoppingList.push(newItem);
        console.log(shoppingList);


        var xhr = new XMLHttpRequest();
        xhr.onreadystatechange = function() {
            if (xhr.readyState == 4 && xhr.status == 200) {
                var data = JSON.parse(xhr.responseText);

            }
        };
        xhr.open("POST", "/get-shoppinglist/", true);

        xhr.setRequestHeader("Content-Type", 'application/json');
        xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));

        var sendList = JSON.stringify(shoppingList);
        xhr.send(sendList);

        document.getElementById("addItem").addEventListener("click", function(){
        });

    });

    $(document).on('click', 'li', function () {
        $(this).toggleClass('complete');
    });

    $(document).on('dblclick', 'li', function () {
        $(this).remove();
    });

    $('button#clearAllItems').on('click', function () {
        $('div li').remove();
        $('#categories').remove();
        $('#controls').fadeOut();
    });


    var xhr = new XMLHttpRequest();
       xhr.onreadystatechange = function() {
           if (xhr.readyState == 4 && xhr.status == 200){
               alert(xhr.responseText);

           }
       };
    xhr.open("GET", "/get-shoppinglist/", true);

    xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));

    xhr.send(null);


});
