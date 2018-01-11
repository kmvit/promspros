/*
 fancyBox - jQuery Plugin
 version: 2.1.5 (Fri, 14 Jun 2013)
 @requires jQuery v1.6 or later

 Examples at http://fancyapps.com/fancybox/
 License: www.fancyapps.com/fancybox/#license

 Copyright 2012 Janis Skarnelis - janis@fancyapps.com

*/
(function(t,F,f,z){var K=f("html"),p=f(t),q=f(F),b=f.fancybox=function(){b.open.apply(this,arguments)},J=navigator.userAgent.match(/msie/i),A=null,u=F.createTouch!==z,w=function(a){return a&&a.hasOwnProperty&&a instanceof f},r=function(a){return a&&"string"===f.type(a)},G=function(a){return r(a)&&0<a.indexOf("%")},m=function(a,c){var e=parseInt(a,10)||0;c&&G(a)&&(e*=b.getViewport()[c]/100);return Math.ceil(e)},x=function(a,b){return m(a,b)+"px"};f.extend(b,{version:"2.1.5",defaults:{padding:15,margin:20,
width:800,height:600,minWidth:100,minHeight:100,maxWidth:9999,maxHeight:9999,pixelRatio:1,autoSize:!0,autoHeight:!1,autoWidth:!1,autoResize:!0,autoCenter:!u,fitToView:!0,aspectRatio:!1,topRatio:.5,leftRatio:.5,scrolling:"auto",wrapCSS:"",arrows:!0,closeBtn:!0,closeClick:!1,nextClick:!1,mouseWheel:!0,autoPlay:!1,playSpeed:3E3,preload:3,modal:!1,loop:!0,ajax:{dataType:"html",headers:{"X-fancyBox":!0}},iframe:{scrolling:"auto",preload:!0},swf:{wmode:"transparent",allowfullscreen:"true",allowscriptaccess:"always"},
keys:{next:{13:"left",34:"up",39:"left",40:"up"},prev:{8:"right",33:"down",37:"right",38:"down"},close:[27],play:[32],toggle:[70]},direction:{next:"left",prev:"right"},scrollOutside:!0,index:0,type:null,href:null,content:null,title:null,tpl:{wrap:'<div class="fancybox-wrap" tabIndex="-1"><div class="fancybox-skin"><div class="fancybox-outer"><div class="fancybox-inner"></div></div></div></div>',image:'<img class="fancybox-image" src="{href}" alt="" />',iframe:'<iframe id="fancybox-frame{rnd}" name="fancybox-frame{rnd}" class="fancybox-iframe" frameborder="0" vspace="0" hspace="0" webkitAllowFullScreen mozallowfullscreen allowFullScreen'+
(J?' allowtransparency="true"':"")+"></iframe>",error:'<p class="fancybox-error">The requested content cannot be loaded.<br/>Please try again later.</p>',closeBtn:'<a title="Close" class="fancybox-item fancybox-close" href="javascript:;"></a>',next:'<a title="Next" class="fancybox-nav fancybox-next" href="javascript:;"><span></span></a>',prev:'<a title="Previous" class="fancybox-nav fancybox-prev" href="javascript:;"><span></span></a>'},openEffect:"fade",openSpeed:250,openEasing:"swing",openOpacity:!0,
openMethod:"zoomIn",closeEffect:"fade",closeSpeed:250,closeEasing:"swing",closeOpacity:!0,closeMethod:"zoomOut",nextEffect:"elastic",nextSpeed:250,nextEasing:"swing",nextMethod:"changeIn",prevEffect:"elastic",prevSpeed:250,prevEasing:"swing",prevMethod:"changeOut",helpers:{overlay:!0,title:!0},onCancel:f.noop,beforeLoad:f.noop,afterLoad:f.noop,beforeShow:f.noop,afterShow:f.noop,beforeChange:f.noop,beforeClose:f.noop,afterClose:f.noop},group:{},opts:{},previous:null,coming:null,current:null,isActive:!1,
isOpen:!1,isOpened:!1,wrap:null,skin:null,outer:null,inner:null,player:{timer:null,isActive:!1},ajaxLoad:null,imgPreload:null,transitions:{},helpers:{},open:function(a,c){if(a&&(f.isPlainObject(c)||(c={}),!1!==b.close(!0)))return f.isArray(a)||(a=w(a)?f(a).get():[a]),f.each(a,function(e,d){var l={},h;"object"===f.type(d)&&(d.nodeType&&(d=f(d)),w(d)?(l={href:d.data("fancybox-href")||d.attr("href"),title:d.data("fancybox-title")||d.attr("title"),isDom:!0,element:d},f.metadata&&f.extend(!0,l,d.metadata())):
l=d);var g=c.href||l.href||(r(d)?d:null);var k=c.title!==z?c.title:l.title||"";var n=(h=c.content||l.content)?"html":c.type||l.type;!n&&l.isDom&&(n=d.data("fancybox-type"),n||(n=(n=d.prop("class").match(/fancybox\.(\w+)/))?n[1]:null));if(r(g)&&(n||(b.isImage(g)?n="image":b.isSWF(g)?n="swf":"#"===g.charAt(0)?n="inline":r(d)&&(n="html",h=d)),"ajax"===n)){var m=g.split(/\s+/,2);g=m.shift();m=m.shift()}h||("inline"===n?g?h=f(r(g)?g.replace(/.*(?=#[^\s]+$)/,""):g):l.isDom&&(h=d):"html"===n?h=g:n||g||!l.isDom||
(n="inline",h=d));f.extend(l,{href:g,type:n,content:h,title:k,selector:m});a[e]=l}),b.opts=f.extend(!0,{},b.defaults,c),c.keys!==z&&(b.opts.keys=c.keys?f.extend({},b.defaults.keys,c.keys):!1),b.group=a,b._start(b.opts.index)},cancel:function(){var a=b.coming;a&&!1!==b.trigger("onCancel")&&(b.hideLoading(),b.ajaxLoad&&b.ajaxLoad.abort(),b.ajaxLoad=null,b.imgPreload&&(b.imgPreload.onload=b.imgPreload.onerror=null),a.wrap&&a.wrap.stop(!0,!0).trigger("onReset").remove(),b.coming=null,b.current||b._afterZoomOut(a))},
close:function(a){b.cancel();!1!==b.trigger("beforeClose")&&(b.unbindEvents(),b.isActive&&(b.isOpen&&!0!==a?(b.isOpen=b.isOpened=!1,b.isClosing=!0,f(".fancybox-item, .fancybox-nav").remove(),b.wrap.stop(!0,!0).removeClass("fancybox-opened"),b.transitions[b.current.closeMethod]()):(f(".fancybox-wrap").stop(!0).trigger("onReset").remove(),b._afterZoomOut())))},play:function(a){var c=function(){clearTimeout(b.player.timer)},e=function(){c();b.current&&b.player.isActive&&(b.player.timer=setTimeout(b.next,
b.current.playSpeed))},d=function(){c();q.unbind(".player");b.player.isActive=!1;b.trigger("onPlayEnd")};!0===a||!b.player.isActive&&!1!==a?b.current&&(b.current.loop||b.current.index<b.group.length-1)&&(b.player.isActive=!0,q.bind({"onCancel.player beforeClose.player":d,"onUpdate.player":e,"beforeLoad.player":c}),e(),b.trigger("onPlayStart")):d()},next:function(a){var c=b.current;c&&(r(a)||(a=c.direction.next),b.jumpto(c.index+1,a,"next"))},prev:function(a){var c=b.current;c&&(r(a)||(a=c.direction.prev),
b.jumpto(c.index-1,a,"prev"))},jumpto:function(a,c,e){var d=b.current;d&&(a=m(a),b.direction=c||d.direction[a>=d.index?"next":"prev"],b.router=e||"jumpto",d.loop&&(0>a&&(a=d.group.length+a%d.group.length),a%=d.group.length),d.group[a]!==z&&(b.cancel(),b._start(a)))},reposition:function(a,c){var e=b.current,d=e?e.wrap:null;if(d){var l=b._getPosition(c);a&&"scroll"===a.type?(delete l.position,d.stop(!0,!0).animate(l,200)):(d.css(l),e.pos=f.extend({},e.dim,l))}},update:function(a){var c=a&&a.type,e=
!c||"orientationchange"===c;e&&(clearTimeout(A),A=null);b.isOpen&&!A&&(A=setTimeout(function(){var d=b.current;d&&!b.isClosing&&(b.wrap.removeClass("fancybox-tmp"),(e||"load"===c||"resize"===c&&d.autoResize)&&b._setDimension(),"scroll"===c&&d.canShrink||b.reposition(a),b.trigger("onUpdate"),A=null)},e&&!u?0:300))},toggle:function(a){b.isOpen&&(b.current.fitToView="boolean"===f.type(a)?a:!b.current.fitToView,u&&(b.wrap.removeAttr("style").addClass("fancybox-tmp"),b.trigger("onUpdate")),b.update())},
hideLoading:function(){q.unbind(".loading");f("#fancybox-loading").remove()},showLoading:function(){b.hideLoading();var a=f('<div id="fancybox-loading"><div></div></div>').click(b.cancel).appendTo("body");q.bind("keydown.loading",function(a){27===(a.which||a.keyCode)&&(a.preventDefault(),b.cancel())});if(!b.defaults.fixed){var c=b.getViewport();a.css({position:"absolute",top:.5*c.h+c.y,left:.5*c.w+c.x})}},getViewport:function(){var a=b.current&&b.current.locked||!1,c={x:p.scrollLeft(),y:p.scrollTop()};
a?(c.w=a[0].clientWidth,c.h=a[0].clientHeight):(c.w=u&&t.innerWidth?t.innerWidth:p.width(),c.h=u&&t.innerHeight?t.innerHeight:p.height());return c},unbindEvents:function(){b.wrap&&w(b.wrap)&&b.wrap.unbind(".fb");q.unbind(".fb");p.unbind(".fb")},bindEvents:function(){var a=b.current,c;a&&(p.bind("orientationchange.fb"+(u?"":" resize.fb")+(a.autoCenter&&!a.locked?" scroll.fb":""),b.update),(c=a.keys)&&q.bind("keydown.fb",function(e){var d=e.which||e.keyCode,l=e.target||e.srcElement;if(27===d&&b.coming)return!1;
e.ctrlKey||e.altKey||e.shiftKey||e.metaKey||l&&(l.type||f(l).is("[contenteditable]"))||f.each(c,function(c,g){if(1<a.group.length&&g[d]!==z)return b[c](g[d]),e.preventDefault(),!1;if(-1<f.inArray(d,g))return b[c](),e.preventDefault(),!1})}),f.fn.mousewheel&&a.mouseWheel&&b.wrap.bind("mousewheel.fb",function(c,d,l,h){for(var e=f(c.target||null),k=!1;e.length&&!(k||e.is(".fancybox-skin")||e.is(".fancybox-wrap"));)k=(k=e[0])&&!(k.style.overflow&&"hidden"===k.style.overflow)&&(k.clientWidth&&k.scrollWidth>
k.clientWidth||k.clientHeight&&k.scrollHeight>k.clientHeight),e=f(e).parent();0!==d&&!k&&1<b.group.length&&!a.canShrink&&(0<h||0<l?b.prev(0<h?"down":"left"):(0>h||0>l)&&b.next(0>h?"up":"right"),c.preventDefault())}))},trigger:function(a,c){var e,d=c||b.coming||b.current;if(d){f.isFunction(d[a])&&(e=d[a].apply(d,Array.prototype.slice.call(arguments,1)));if(!1===e)return!1;d.helpers&&f.each(d.helpers,function(c,e){if(e&&b.helpers[c]&&f.isFunction(b.helpers[c][a]))b.helpers[c][a](f.extend(!0,{},b.helpers[c].defaults,
e),d)});q.trigger(a)}},isImage:function(a){return r(a)&&a.match(/(^data:image\/.*,)|(\.(jp(e|g|eg)|gif|png|bmp|webp|svg)((\?|#).*)?$)/i)},isSWF:function(a){return r(a)&&a.match(/\.(swf)((\?|#).*)?$/i)},_start:function(a){var c={};a=m(a);var e=b.group[a]||null;if(!e)return!1;c=f.extend(!0,{},b.opts,e);e=c.margin;var d=c.padding;"number"===f.type(e)&&(c.margin=[e,e,e,e]);"number"===f.type(d)&&(c.padding=[d,d,d,d]);c.modal&&f.extend(!0,c,{closeBtn:!1,closeClick:!1,nextClick:!1,arrows:!1,mouseWheel:!1,
keys:null,helpers:{overlay:{closeClick:!1}}});c.autoSize&&(c.autoWidth=c.autoHeight=!0);"auto"===c.width&&(c.autoWidth=!0);"auto"===c.height&&(c.autoHeight=!0);c.group=b.group;c.index=a;b.coming=c;if(!1===b.trigger("beforeLoad"))b.coming=null;else{d=c.type;e=c.href;if(!d)return b.coming=null,b.current&&b.router&&"jumpto"!==b.router?(b.current.index=a,b[b.router](b.direction)):!1;b.isActive=!0;if("image"===d||"swf"===d)c.autoHeight=c.autoWidth=!1,c.scrolling="visible";"image"===d&&(c.aspectRatio=!0);
"iframe"===d&&u&&(c.scrolling="scroll");c.wrap=f(c.tpl.wrap).addClass("fancybox-"+(u?"mobile":"desktop")+" fancybox-type-"+d+" fancybox-tmp "+c.wrapCSS).appendTo(c.parent||"body");f.extend(c,{skin:f(".fancybox-skin",c.wrap),outer:f(".fancybox-outer",c.wrap),inner:f(".fancybox-inner",c.wrap)});f.each(["Top","Right","Bottom","Left"],function(a,b){c.skin.css("padding"+b,x(c.padding[a]))});b.trigger("onReady");if("inline"===d||"html"===d){if(!c.content||!c.content.length)return b._error("content")}else if(!e)return b._error("href");
"image"===d?b._loadImage():"ajax"===d?b._loadAjax():"iframe"===d?b._loadIframe():b._afterLoad()}},_error:function(a){f.extend(b.coming,{type:"html",autoWidth:!0,autoHeight:!0,minWidth:0,minHeight:0,scrolling:"no",hasError:a,content:b.coming.tpl.error});b._afterLoad()},_loadImage:function(){var a=b.imgPreload=new Image;a.onload=function(){this.onload=this.onerror=null;b.coming.width=this.width/b.opts.pixelRatio;b.coming.height=this.height/b.opts.pixelRatio;b._afterLoad()};a.onerror=function(){this.onload=
this.onerror=null;b._error("image")};a.src=b.coming.href;!0!==a.complete&&b.showLoading()},_loadAjax:function(){var a=b.coming;b.showLoading();b.ajaxLoad=f.ajax(f.extend({},a.ajax,{url:a.href,error:function(a,e){b.coming&&"abort"!==e?b._error("ajax",a):b.hideLoading()},success:function(c,e){"success"===e&&(a.content=c,b._afterLoad())}}))},_loadIframe:function(){var a=b.coming,c=f(a.tpl.iframe.replace(/\{rnd\}/g,(new Date).getTime())).attr("scrolling",u?"auto":a.iframe.scrolling).attr("src",a.href);
f(a.wrap).bind("onReset",function(){try{f(this).find("iframe").hide().attr("src","//about:blank").end().empty()}catch(e){}});a.iframe.preload&&(b.showLoading(),c.one("load",function(){f(this).data("ready",1);u||f(this).bind("load.fb",b.update);f(this).parents(".fancybox-wrap").width("100%").removeClass("fancybox-tmp").show();b._afterLoad()}));a.content=c.appendTo(a.inner);a.iframe.preload||b._afterLoad()},_preloadImages:function(){var a=b.group,c=b.current,e=a.length,d=c.preload?Math.min(c.preload,
e-1):0,f;for(f=1;f<=d;f+=1){var h=a[(c.index+f)%e];"image"===h.type&&h.href&&((new Image).src=h.href)}},_afterLoad:function(){var a=b.coming,c=b.current;b.hideLoading();if(a&&!1!==b.isActive)if(!1===b.trigger("afterLoad",a,c))a.wrap.stop(!0).trigger("onReset").remove(),b.coming=null;else{c&&(b.trigger("beforeChange",c),c.wrap.stop(!0).removeClass("fancybox-opened").find(".fancybox-item, .fancybox-nav").remove());b.unbindEvents();var e=a.content;var d=a.type;var l=a.scrolling;f.extend(b,{wrap:a.wrap,
skin:a.skin,outer:a.outer,inner:a.inner,current:a,previous:c});var h=a.href;switch(d){case "inline":case "ajax":case "html":a.selector?e=f("<div>").html(e).find(a.selector):w(e)&&(e.data("fancybox-placeholder")||e.data("fancybox-placeholder",f('<div class="fancybox-placeholder"></div>').insertAfter(e).hide()),e=e.show().detach(),a.wrap.bind("onReset",function(){f(this).find(e).length&&e.hide().replaceAll(e.data("fancybox-placeholder")).data("fancybox-placeholder",!1)}));break;case "image":e=a.tpl.image.replace("{href}",
h);break;case "swf":e='<object id="fancybox-swf" classid="clsid:D27CDB6E-AE6D-11cf-96B8-444553540000" width="100%" height="100%"><param name="movie" value="'+h+'"></param>';var g="";f.each(a.swf,function(a,b){e+='<param name="'+a+'" value="'+b+'"></param>';g+=" "+a+'="'+b+'"'});e+='<embed src="'+h+'" type="application/x-shockwave-flash" width="100%" height="100%"'+g+"></embed></object>"}w(e)&&e.parent().is(a.inner)||a.inner.append(e);b.trigger("beforeShow");a.inner.css("overflow","yes"===l?"scroll":
"no"===l?"hidden":l);b._setDimension();b.reposition();b.isOpen=!1;b.coming=null;b.bindEvents();if(!b.isOpened)f(".fancybox-wrap").not(a.wrap).stop(!0).trigger("onReset").remove();else if(c.prevMethod)b.transitions[c.prevMethod]();b.transitions[b.isOpened?a.nextMethod:a.openMethod]();b._preloadImages()}},_setDimension:function(){var a=b.getViewport(),c=0,e=b.wrap,d=b.skin,l=b.inner,h=b.current;var g=h.width;var k=h.height,n=h.minWidth,v=h.minHeight,p=h.maxWidth,q=h.maxHeight,u=h.scrolling,r=h.scrollOutside?
h.scrollbarWidth:0,y=h.margin,B=m(y[1]+y[3]),t=m(y[0]+y[2]);e.add(d).add(l).width("auto").height("auto").removeClass("fancybox-tmp");y=m(d.outerWidth(!0)-d.width());var z=m(d.outerHeight(!0)-d.height());var C=B+y;var w=t+z;var E=G(g)?(a.w-C)*m(g)/100:g;var D=G(k)?(a.h-w)*m(k)/100:k;if("iframe"===h.type){var A=h.content;if(h.autoHeight&&1===A.data("ready"))try{if(A[0].contentWindow.document.location){l.width(E).height(9999);var I=A.contents().find("body");r&&I.css("overflow-x","hidden");D=I.outerHeight(!0)}}catch(L){}}else if(h.autoWidth||
h.autoHeight)l.addClass("fancybox-tmp"),h.autoWidth||l.width(E),h.autoHeight||l.height(D),h.autoWidth&&(E=l.width()),h.autoHeight&&(D=l.height()),l.removeClass("fancybox-tmp");g=m(E);k=m(D);var H=E/D;n=m(G(n)?m(n,"w")-C:n);p=m(G(p)?m(p,"w")-C:p);v=m(G(v)?m(v,"h")-w:v);q=m(G(q)?m(q,"h")-w:q);I=p;var F=q;h.fitToView&&(p=Math.min(a.w-C,p),q=Math.min(a.h-w,q));C=a.w-B;t=a.h-t;h.aspectRatio?(g>p&&(g=p,k=m(g/H)),k>q&&(k=q,g=m(k*H)),g<n&&(g=n,k=m(g/H)),k<v&&(k=v,g=m(k*H))):(g=Math.max(n,Math.min(g,p)),h.autoHeight&&
"iframe"!==h.type&&(l.width(g),k=l.height()),k=Math.max(v,Math.min(k,q)));if(h.fitToView)if(l.width(g).height(k),e.width(g+y),a=e.width(),B=e.height(),h.aspectRatio)for(;(a>C||B>t)&&g>n&&k>v&&!(19<c++);)k=Math.max(v,Math.min(q,k-10)),g=m(k*H),g<n&&(g=n,k=m(g/H)),g>p&&(g=p,k=m(g/H)),l.width(g).height(k),e.width(g+y),a=e.width(),B=e.height();else g=Math.max(n,Math.min(g,g-(a-C))),k=Math.max(v,Math.min(k,k-(B-t)));r&&"auto"===u&&k<D&&g+y+r<C&&(g+=r);l.width(g).height(k);e.width(g+y);a=e.width();B=e.height();
c=(a>C||B>t)&&g>n&&k>v;g=h.aspectRatio?g<I&&k<F&&g<E&&k<D:(g<I||k<F)&&(g<E||k<D);f.extend(h,{dim:{width:x(a),height:x(B)},origWidth:E,origHeight:D,canShrink:c,canExpand:g,wPadding:y,hPadding:z,wrapSpace:B-d.outerHeight(!0),skinSpace:d.height()-k});!A&&h.autoHeight&&k>v&&k<q&&!g&&l.height("auto")},_getPosition:function(a){var c=b.current,e=b.getViewport(),d=c.margin,f=b.wrap.width()+d[1]+d[3],h=b.wrap.height()+d[0]+d[2],d={position:"absolute",top:d[0],left:d[3]};c.autoCenter&&c.fixed&&!a&&h<=e.h&&
f<=e.w?d.position="fixed":c.locked||(d.top+=e.y,d.left+=e.x);d.top=x(Math.max(d.top,d.top+(e.h-h)*c.topRatio));d.left=x(Math.max(d.left,d.left+(e.w-f)*c.leftRatio));return d},_afterZoomIn:function(){var a=b.current;a&&((b.isOpen=b.isOpened=!0,b.wrap.css("overflow","visible").addClass("fancybox-opened"),b.update(),(a.closeClick||a.nextClick&&1<b.group.length)&&b.inner.css("cursor","pointer").bind("click.fb",function(c){f(c.target).is("a")||f(c.target).parent().is("a")||(c.preventDefault(),b[a.closeClick?
"close":"next"]())}),a.closeBtn&&f(a.tpl.closeBtn).appendTo(b.skin).bind("click.fb",function(a){a.preventDefault();b.close()}),a.arrows&&1<b.group.length&&((a.loop||0<a.index)&&f(a.tpl.prev).appendTo(b.outer).bind("click.fb",b.prev),(a.loop||a.index<b.group.length-1)&&f(a.tpl.next).appendTo(b.outer).bind("click.fb",b.next)),b.trigger("afterShow"),a.loop||a.index!==a.group.length-1)?b.opts.autoPlay&&!b.player.isActive&&(b.opts.autoPlay=!1,b.play()):b.play(!1))},_afterZoomOut:function(a){a=a||b.current;
f(".fancybox-wrap").trigger("onReset").remove();f.extend(b,{group:{},opts:{},router:!1,current:null,isActive:!1,isOpened:!1,isOpen:!1,isClosing:!1,wrap:null,skin:null,outer:null,inner:null});b.trigger("afterClose",a)}});b.transitions={getOrigPosition:function(){var a=b.current,c=a.element,e=a.orig,d={},f=50,h=50,g=a.hPadding,k=a.wPadding,n=b.getViewport();!e&&a.isDom&&c.is(":visible")&&(e=c.find("img:first"),e.length||(e=c));w(e)?(d=e.offset(),e.is("img")&&(f=e.outerWidth(),h=e.outerHeight())):(d.top=
n.y+(n.h-h)*a.topRatio,d.left=n.x+(n.w-f)*a.leftRatio);if("fixed"===b.wrap.css("position")||a.locked)d.top-=n.y,d.left-=n.x;return d={top:x(d.top-g*a.topRatio),left:x(d.left-k*a.leftRatio),width:x(f+k),height:x(h+g)}},step:function(a,c){var e=c.prop;var d=b.current;var f=d.wrapSpace,h=d.skinSpace;if("width"===e||"height"===e){var g=c.end===c.start?1:(a-c.start)/(c.end-c.start);b.isClosing&&(g=1-g);d="width"===e?d.wPadding:d.hPadding;d=a-d;b.skin[e](m("width"===e?d:d-f*g));b.inner[e](m("width"===e?
d:d-f*g-h*g))}},zoomIn:function(){var a=b.current,c=a.pos,e=a.openEffect,d="elastic"===e,l=f.extend({opacity:1},c);delete l.position;d?(c=this.getOrigPosition(),a.openOpacity&&(c.opacity=.1)):"fade"===e&&(c.opacity=.1);b.wrap.css(c).animate(l,{duration:"none"===e?0:a.openSpeed,easing:a.openEasing,step:d?this.step:null,complete:b._afterZoomIn})},zoomOut:function(){var a=b.current,c=a.closeEffect,e="elastic"===c,d={opacity:.1};e&&(d=this.getOrigPosition(),a.closeOpacity&&(d.opacity=.1));b.wrap.animate(d,
{duration:"none"===c?0:a.closeSpeed,easing:a.closeEasing,step:e?this.step:null,complete:b._afterZoomOut})},changeIn:function(){var a=b.current,c=a.nextEffect,e=a.pos,d={opacity:1},f=b.direction;e.opacity=.1;if("elastic"===c){var h="down"===f||"up"===f?"top":"left";"down"===f||"right"===f?(e[h]=x(m(e[h])-200),d[h]="+=200px"):(e[h]=x(m(e[h])+200),d[h]="-=200px")}"none"===c?b._afterZoomIn():b.wrap.css(e).animate(d,{duration:a.nextSpeed,easing:a.nextEasing,complete:b._afterZoomIn})},changeOut:function(){var a=
b.previous,c=a.prevEffect,e={opacity:.1},d=b.direction;"elastic"===c&&(e["down"===d||"up"===d?"top":"left"]=("up"===d||"left"===d?"-":"+")+"=200px");a.wrap.animate(e,{duration:"none"===c?0:a.prevSpeed,easing:a.prevEasing,complete:function(){f(this).trigger("onReset").remove()}})}};b.helpers.overlay={defaults:{closeClick:!0,speedOut:200,showEarly:!0,css:{},locked:!u,fixed:!0},overlay:null,fixed:!1,el:f("html"),create:function(a){a=f.extend({},this.defaults,a);this.overlay&&this.close();this.overlay=
f('<div class="fancybox-overlay"></div>').appendTo(b.coming?b.coming.parent:a.parent);this.fixed=!1;a.fixed&&b.defaults.fixed&&(this.overlay.addClass("fancybox-overlay-fixed"),this.fixed=!0)},open:function(a){var c=this;a=f.extend({},this.defaults,a);this.overlay?this.overlay.unbind(".overlay").width("auto").height("auto"):this.create(a);this.fixed||(p.bind("resize.overlay",f.proxy(this.update,this)),this.update());a.closeClick&&this.overlay.bind("click.overlay",function(a){if(f(a.target).hasClass("fancybox-overlay"))return b.isActive?
b.close():c.close(),!1});this.overlay.css(a.css).show()},close:function(){p.unbind("resize.overlay");if(this.el.hasClass("fancybox-lock")){f(".fancybox-margin").removeClass("fancybox-margin");var a=p.scrollTop();var b=p.scrollLeft();this.el.removeClass("fancybox-lock");p.scrollTop(a).scrollLeft(b)}f(".fancybox-overlay").remove().hide();f.extend(this,{overlay:null,fixed:!1})},update:function(){var a="100%";this.overlay.width(a).height("100%");if(J){var b=Math.max(F.documentElement.offsetWidth,F.body.offsetWidth);
q.width()>b&&(a=q.width())}else q.width()>p.width()&&(a=q.width());this.overlay.width(a).height(q.height())},onReady:function(a,b){var c=this.overlay;f(".fancybox-overlay").stop(!0,!0);c||this.create(a);a.locked&&this.fixed&&b.fixed&&(c||(this.margin=q.height()>p.height()?f("html").css("margin-right").replace("px",""):!1),b.locked=this.overlay.append(b.wrap),b.fixed=!1);!0===a.showEarly&&this.beforeShow.apply(this,arguments)},beforeShow:function(a,b){if(b.locked){!1!==this.margin&&(f("*").filter(function(){return"fixed"===
f(this).css("position")&&!f(this).hasClass("fancybox-overlay")&&!f(this).hasClass("fancybox-wrap")}).addClass("fancybox-margin"),this.el.addClass("fancybox-margin"));var c=p.scrollTop();var d=p.scrollLeft();this.el.addClass("fancybox-lock");p.scrollTop(c).scrollLeft(d)}this.open(a)},onUpdate:function(){this.fixed||this.update()},afterClose:function(a){this.overlay&&!b.coming&&this.overlay.fadeOut(a.speedOut,f.proxy(this.close,this))}};b.helpers.title={defaults:{type:"float",position:"bottom"},beforeShow:function(a){var c=
b.current,e=c.title,d=a.type;f.isFunction(e)&&(e=e.call(c.element,c));if(r(e)&&""!==f.trim(e)){c=f('<div class="fancybox-title fancybox-title-'+d+'-wrap">'+e+"</div>");switch(d){case "inside":d=b.skin;break;case "outside":d=b.wrap;break;case "over":d=b.inner;break;default:d=b.skin,c.appendTo("body"),J&&c.width(c.width()),c.wrapInner('<span class="child"></span>'),b.current.margin[2]+=Math.abs(m(c.css("margin-bottom")))}c["top"===a.position?"prependTo":"appendTo"](d)}}};f.fn.fancybox=function(a){var c=
f(this),e=this.selector||"",d=function(d){var g=f(this).blur(),h=l;if(!(d.ctrlKey||d.altKey||d.shiftKey||d.metaKey||g.is(".fancybox-wrap"))){var n=a.groupAttr||"data-fancybox-group";var m=g.attr(n);m||(n="rel",m=g.get(0)[n]);m&&""!==m&&"nofollow"!==m&&(g=e.length?f(e):c,g=g.filter("["+n+'="'+m+'"]'),h=g.index(this));a.index=h;!1!==b.open(g,a)&&d.preventDefault()}};a=a||{};var l=a.index||0;e&&!1!==a.live?q.undelegate(e,"click.fb-start").delegate(e+":not('.fancybox-item, .fancybox-nav')","click.fb-start",
d):c.unbind("click.fb-start").bind("click.fb-start",d);this.filter("[data-fancybox-start=1]").trigger("click");return this};q.ready(function(){f.scrollbarWidth===z&&(f.scrollbarWidth=function(){var a=f('<div style="width:50px;height:50px;overflow:auto"><div/></div>').appendTo("body"),b=a.children(),b=b.innerWidth()-b.height(99).innerWidth();a.remove();return b});f.support.fixedPosition===z&&(f.support.fixedPosition=function(){var a=f('<div style="position:fixed;top:20px;"></div>').appendTo("body"),
b=20===a[0].offsetTop||15===a[0].offsetTop;a.remove();return b}());f.extend(b.defaults,{scrollbarWidth:f.scrollbarWidth(),fixed:f.support.fixedPosition,parent:f("body")});var a=f(t).width();K.addClass("fancybox-lock-test");var c=f(t).width();K.removeClass("fancybox-lock-test");f("<style type='text/css'>.fancybox-margin{margin-right:"+(c-a)+"px;}</style>").appendTo("head")})})(window,document,jQuery);