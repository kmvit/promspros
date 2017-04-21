function myConfirm(msg, func){
  var div=document.createElement('div');
  div.style.cssText="text-align:center;padding:10px;position:fixed;width:200px;height:40px;bottom:50%;right:50%;margin-right:-100px;margin-bottom:-20px;border:1px dotted #000"
  div.onclick=function(e){
    var t=e?e.target:window.event.srcElement;
    if(t.tagName=='INPUT'){
      t.value=='Да'&&func('да');
      this.parentNode.removeChild(this)
    }
  }
  div.innerHTML='<div>'+msg+'<div><input type="button" value="Да"><input type="button" value="Нет">'
  return document.body.appendChild(div);
}



$(function(){
 /* выбор города */
 $('.delivery_list').click(function(){
 $(".cities_list").slideToggle('fast');
 });
 $('ul.cities_list li').click(function(){
 var tx = $(this).html();
 var tv = $(this).attr('alt');
 $(".cities_list").slideUp('fast');
 $(".delivery_list span").html(tx);
 $(".delivery_text").html(tv);
 });
 })
 
 
 
 //Обработка клика на стрелку вправо
$(document).on('click', ".carousel-button-right",function(){ 
	var carusel = $(this).parents('.carousel');
	right_carusel(carusel);
	return false;
});
//Обработка клика на стрелку влево
$(document).on('click',".carousel-button-left",function(){ 
	var carusel = $(this).parents('.carousel');
	left_carusel(carusel);
	return false;
});
function left_carusel(carusel){
   var block_width = $(carusel).find('.carousel-block').outerWidth();
   $(carusel).find(".carousel-items .carousel-block").eq(-1).clone().prependTo($(carusel).find(".carousel-items")); 
   $(carusel).find(".carousel-items").css({"left":"-"+block_width+"px"});
   $(carusel).find(".carousel-items .carousel-block").eq(-1).remove();    
   $(carusel).find(".carousel-items").animate({left: "0px"}, 200); 
   
}
function right_carusel(carusel){
   var block_width = $(carusel).find('.carousel-block').outerWidth();
   $(carusel).find(".carousel-items").animate({left: "-"+ block_width +"px"}, 200, function(){
	  $(carusel).find(".carousel-items .carousel-block").eq(0).clone().appendTo($(carusel).find(".carousel-items")); 
      $(carusel).find(".carousel-items .carousel-block").eq(0).remove(); 
      $(carusel).find(".carousel-items").css({"left":"0px"}); 
   }); 
}

$(function() {
//Раскомментируйте строку ниже, чтобы включить автоматическую прокрутку карусели
	auto_right('.carousel:first');
})

// Автоматическая прокрутка
function auto_right(carusel){
	setInterval(function(){
		if (!$(carusel).is('.hover'))
			right_carusel(carusel);
	}, 3000)
}
// Навели курсор на карусель
$(document).on('mouseenter', '.carousel', function(){$(this).addClass('hover')})
//Убрали курсор с карусели
$(document).on('mouseleave', '.carousel', function(){$(this).removeClass('hover')})