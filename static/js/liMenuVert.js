(function($){
	$.fn.liMenuVert = function(){
		return this.each(function(){
			var
			menuWrap = $(this),
			menuWrapWidth = menuWrap.outerWidth(),
			menuWrapLeft = menuWrap.offset().left,
			menuSubSub = $('ul',menuWrap);

			menuSubSub.each(function(){
				var
				mSubSub = $(this),
				mSubList = mSubSub.closest('li'),
				mArrowRight = $('<div>').addClass('arrow-right'),
				mSubLink = mSubList.children('a');

				function on_click(e){
					e.stopPropagation();
					e.preventDefault();
					if (mSubLink.hasClass('active')) {
						mSubLink.find('div.arrow-right').remove();
						mSubLink.removeClass('active')
						var mSubHide = $(this).parent('li ul');
						if (!mSubHide.hasClass('menu_vert')) {
							mSubHide.hide();
						}
						mSubHide.find('ul').each(function(idx, elm) {
							$(elm).hide();
							var mActive = $(elm).find('a.active');
							mActive.find('div.arrow-right').remove();
							mActive.removeClass('active');
						});
					} else {
						var mActive = mSubLink.closest('ul').find('li a.active');
						mActive.find('div.arrow-right').remove();
						mActive.removeClass('active');
						mSubLink.closest('ul').find('ul').hide();
						mActive.parent().children('ul').children('li.active').removeClass('active');
						mHoverLink = $(this);
						mHoverLink.next('ul').children('li').width(mHoverLink.next('ul').width());	//correct width in ie7
						var
						mSubSubLeft = mSubLink.position().left + mSubLink.outerWidth(),
						p1 = (mSubLink.closest('ul').outerWidth()-mSubLink.closest('ul').width())/2;
						mSubSub.css({top:0});
						mSubSub.css({left:mSubSubLeft});
						mSubSub.show();
						var w3 = $(window).width();
						var w6 = (mSubSub.offset().left + mSubSub.outerWidth());
						w6 = w3 - 1;
						if(w6 >= w3){
							mSubSub.closest('ul').addClass('toLeft');
							mSubSubLeft = -mSubSub.outerWidth();
						}
						if(mSubSub.parents('ul').hasClass('toLeft')){
							mSubSubLeft = -mSubSub.outerWidth();
						}
						mSubSub.css({left:mSubSubLeft});
						mSubLink.addClass('active');
						mSubLink.append(mArrowRight);
					}
				}
				mSubList.children('a').on('click', on_click);
			});
			menuWrapWidth = menuWrap.outerWidth();
			menuWrapLeft = menuWrap.offset().left;
			$(window).resize(function(){
				menuWrapWidth = menuWrap.outerWidth();
				menuWrapLeft = menuWrap.offset().left;
			});
		});
	};
})(jQuery);

/*инициализация*/
$('.menu_vert').liMenuVert();

$('.category').on('click', function(event) {
	$('.category').removeClass('active');
	$(this).addClass('active');
	$('#id_category').val($(this).text());
	$('#item').css('display','none');
	$('#id_category').css('display','block');
	event.stopPropagation();
});
$('#id_category').on('click', function(event) {
	$('#id_category').css('display','none');
	$('#item').css('display','block');
	event.stopPropagation();
});
$(window).click(function() {
	if ($('#item').css('display') === 'block') {

		var mActive = $('.menu_vert .category.active');
		if (mActive.length) {
			var mParent = mActive.closest('ul').parent('li');

			$('li[role="tab"] > a.active').removeClass('active');
			$('li[role="tab"] > a > div.arrow-right').remove();

			var mArrowRight = $('<div>').addClass('arrow-right');
			mParent.parent().parent().children('a').addClass('active');
			mParent.parent().parent().children('a').append(mArrowRight);

			mParent.parent().find('ul').hide();
			mActive.closest('ul').show();
			var liSecond = mParent.parent().children('li');
			liSecond.find('a').removeClass('active');
			liSecond.find('a').find('div.arrow-right').remove();
			mArrowRight = $('<div>').addClass('arrow-right');
			mParent.children('a').addClass('active');
			mParent.children('a').append(mArrowRight);
		} else {
			$('#id_category').val('');
		}

		$('#item').css('display','none');
		$('#id_category').css('display','block');
	}
});

