(function(b){b.autoScroll=function(a){a=a||{};a.styleClass=a.styleClass||"header";b('<div class="'+a.styleClass+'"></div>');var c=b(a.target||document);$(window).scroll(function(){var a=c.scrollTop();60<a&&($(".header-nav").addClass('active'),$(".search-block").css({"padding-top":"20px"}));60>a&&($(".header-nav").removeClass('active'),$(".search-block").css({"padding-top":"20px"}))})}})(jQuery);
$(document).ready(function(){$.autoScroll();cuSel({changedEl:".cusel"});$(".tabs").tabs();$.mask.definitions["~"]="[+-]";$(".input-phone").mask("+7 (999) 999-99-99");$(".modalbox").fancybox({padding:0,helpers:{overlay:{locked:!1}}});$(".profile-table-hidden-link").click(function(){"\u043f\u043e\u043a\u0430\u0437\u0430\u0442\u044c \u0434\u043e\u043f\u043e\u043b\u043d\u0438\u0442\u0435\u043b\u044c\u043d\u0443\u044e \u0438\u043d\u0444\u043e\u0440\u043c\u0430\u0446\u0438\u044e"==$(".profile-table-hidden-link").html()?
$(this).html("\u0441\u043a\u0440\u044b\u0442\u044c \u0434\u043e\u043f\u043e\u043b\u043d\u0438\u0442\u0435\u043b\u044c\u043d\u0443\u044e \u0438\u043d\u0444\u043e\u0440\u043c\u0430\u0446\u0438\u044e"):$(this).html("\u043f\u043e\u043a\u0430\u0437\u0430\u0442\u044c \u0434\u043e\u043f\u043e\u043b\u043d\u0438\u0442\u0435\u043b\u044c\u043d\u0443\u044e \u0438\u043d\u0444\u043e\u0440\u043c\u0430\u0446\u0438\u044e");$(this).toggleClass("profile-table-hidden-link-a");$(this).parents(".profile-table-wrapper:first").find(".profile-table-hidden").slideToggle(0);
return!1});$(".offer-img-list-del-link").click(function(){$(this).parents(".offer-img-list > li:first").remove();return!1});$("div#overlay").addClass("main-section");$("div#overlay").addClass("new-section")});

var tabs = document.querySelectorAll('.ui-tab');

window.onbeforeunload = function() {
	function add_tab_storage(){
		for (let i = 0; i < tabs.length; i++) {
			if (tabs[i].classList.contains('ui-tabs-active')) {
				localStorage.setItem('tab', tabs[i].textContent);
			}
		}
	};
	add_tab_storage();
};


window.onload = function() {
	function add_class_tab() {
		var storage_tab = localStorage.getItem('tab');
		for (let i = 0; i < tabs.length; i++) {
			if (tabs[i].textContent == storage_tab) {
				tabs[i].classList.add('ui-tabs-active');
			} else {
				tabs[i].classList.remove('ui-tabs-active');
			}
		};
	};
	add_class_tab();
}
