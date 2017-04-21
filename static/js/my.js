(function(jq) {
    jq.autoScroll = function(ops) {
        ops = ops || {};
        ops.styleClass = ops.styleClass || 'header';
        var t = jq('<div class="'+ops.styleClass+'"></div>'),
            d = jq(ops.target || document);

        $(window).scroll(function(){
            var sv = d.scrollTop();


            if  (sv > 60) {
                $('.header-nav-wrapper').css({'position':'fixed' , 'top': '0', 'left': '0', zIndex: '4500'});
                $('.header-inner').css({'padding-top':'30px', 'padding-bottom':'30px'});
            } if (sv < 60)  {
                $('.header-nav-wrapper').css({'position':'relative', 'top': 'auto','left': 'auto'});
                $('.header-inner').css({'padding-top':'10px', 'padding-bottom':'10px'});
            }
        });

    };
})(jQuery);

$(document).ready(function(){


    $.autoScroll();

    var params = {
        changedEl: '.cusel'
    }
    cuSel(params);

    $(".tabs").tabs();

    $.mask.definitions['~']='[+-]';
    $(".input-phone").mask("+7 (999) 999-99-99");


    $(".modalbox").fancybox({
        padding : 0,
        helpers: {
            overlay: {
                locked: false
            }
        }
    });

    $('.profile-table-hidden-link').click(function () {
        if($('.profile-table-hidden-link').html()==('показать дополнительную информацию')) {
            $(this).html('скрыть дополнительную информацию');
        }   else {
            $(this).html('показать дополнительную информацию')
        };
        $(this).toggleClass('profile-table-hidden-link-a');
        $(this).parents('.profile-table-wrapper:first').find('.profile-table-hidden').slideToggle(0);
        return false;
    });

    $('.offer-img-list-del-link').click(function () {
        $(this).parents('.offer-img-list > li:first').remove();
        return false;
    });


    $('div#overlay').addClass('main-section');
    $('div#overlay').addClass('new-section');


});

