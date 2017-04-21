$(document).ready(function() {
    // CSRF code
    function getCookie(name) {
        var cookieValue = null;
        var i = 0;
        if (document.cookie && document.cookie !== '') {
            var cookies = document.cookie.split(';');
            for (i; i < cookies.length; i++) {
                var cookie = jQuery.trim(cookies[i]);
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
    var csrftoken = getCookie('csrftoken');

    function csrfSafeMethod(method) {
        // these HTTP methods do not require CSRF protection
        return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
    }
    $.ajaxSetup({
        crossDomain: false, // obviates need for sameOrigin test
        beforeSend: function(xhr, settings) {
            if (!csrfSafeMethod(settings.type)) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        }
    });

    var statuses = {
        1: 'Активные',
        2: 'Не активные',
        3: 'Черновики'
    };






    

    
    
            


    $(document).on('click', '.move-to__item', function() {
    var $this = $(this),
        $list = $this.parent('ul'),
        $order = $this.parents('.advertisement'),
        data = $.extend($this.data(), $order.data()),
 
        url = '/move2/';
 
    $list.hide();
 
    mscConfirm("Вы подтверждаете действие?", "", function () {
        $.ajax({
            url: url,
            data: data,
            method: 'POST',
            success: function() {
                $list.empty();
 
                $.each(statuses, function(statusId, statusText) {
                    if (+statusId !== data.status) {
                        $list.append($('<li data-status="' + statusId + '" data-id="' + data.id + '" class="move-to__item"> \
                           <a href="#">' + statusText + '</a> \
                       </li>'));
                    }
                });
 
                $('.advertisement-list')
                    .eq(data.status - 1)
                    .find('> ul')
                    .eq(+($order.data('type') !== 'order'))
                    .append($order);
            },
            error: function(d) {
                console.log(d);
            }
        });
    });
});

    
    
    
    $(document).on('click', '.move-in__item', function() {
    var $this = $(this),
        $list = $this.parent('ul'),
        $order = $this.parents('.advertisement-o'),
        data = $.extend($this.data(), $order.data()),
 
        url = '/move2/';
 

 
    mscConfirm("Переместить?", "", function () {
        $.ajax({
            url: url,
            data: data,
            method: 'POST',
            success: function() {
                location.reload();
                $list.empty();
 
                $.each(statuses, function(statusId, statusText) {
                    if (+statusId !== data.status) {
                        $list.append($('<li data-status="' + statusId + '" data-id="' + data.id + '" class="move-to__item"> \
                           <a href="#">' + statusText + '</a> \
                       </li>'));
                    }
                });
 
                $('.advertisement-list')
                    .eq(data.status - 1)
                    .find('> ul')
                    .eq(+($order.data('type') !== 'order'))
                    .append($order);
            },
            error: function(d) {
                console.log(d);
            }
        });
    });
});


    $('.move-to .user-login-link').on('click', function() {
        $(this).parent('.move-to').find('ul').toggle();
    });
    
    $('.add-to-favorites').on('click', function(e) {
        e.preventDefault();

        var $this = $(this),
            data = $this.data(),
            url = '/add2favorites/';
        mscConfirm("Добавить/Удалить избранное", "", function () {
        $.ajax({
            url: url,
            method: 'POST',
            data: data,
            success: function(d) {
                var inFavorites = data.in_favorites,
                    successText = inFavorites
                        ? '<i class="orders-mini-content-favourite" aria-hidden="true"></i>'
                        : '<i class="orders-mini-content-favourite orders-mini-content-favourite-active" aria-hidden="true"></i>';

                $this.data('in_favorites', !inFavorites);
                $this.html(successText);

                console.log(d);
            },
            error: function(d) {
                console.log(d);
            }
        });
        });
    });
    
    
    $('.delete__files').on('click', function(e) {
        e.preventDefault();
        var $this = $(this),
        data = $this.data();
        
        mscConfirm("Вы действительно хотите удалить обьект?", "", function () {
            $this.hide();
            $.ajax({
                url: '/delete-file/',
                method: 'POST',
                data: data,
                success: function(d) {
                    console.log(d);
                },
                error: function(d) {
                    console.log(d);
                }
                
            });
            
        });
       
    });
    
     $('.logout-ajax').on('click', function(e) {
        e.preventDefault();
        
        var $this = $(this),
            data = $this.data(),
            url = '/logout/';
        mscConfirm("Вы действительно хотите выйти?", "", function () {
            $.ajax({
                url: url,
                method: 'POST',
                data: data,
                success: function(d) {
                    window.location.href = '/accounts/login/';
                    console.log(d);
                },
                error: function(d) {
                    console.log(d);
                }
                
            });
            
        });
       
    });
    
    
    
    
   
    $('.companydeleteitem').on('click', function(e) {
        e.preventDefault();
        var $this = $(this),
        qtip = $(this).attr('data-id');
        data = $this.data();
  
        
        mscConfirm("Вы действительно хотите очистить поле?", "", function () {
            $this.hide();
            $.ajax({
                url: '/companydeleteitem/',
                method: 'POST',
                data: data,
                success: function(d) {
                    console.log(d);
                },
                error: function(d) {
                    console.log(d);
                }
                
            });
            
        });
       
    });
    
    $('.a-delete').on('click', function(e) {
        e.preventDefault();
        var $this = $(this),
        $list = $(this).parent('.advertisement'),
        data = $this.data();
  
        
        mscConfirm("Вы действительно хотите удалить из избранного?", "", function () {
            $list.hide();
            $.ajax({
                url: '/deletefromfavorites/',
                method: 'POST',
                data: data,
                success: function(d) {
                    console.log(d);
                },
                error: function(d) {
                    console.log(d);
                }
                
            });
            
        });
       
    });
    
    
    

});




