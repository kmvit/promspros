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
