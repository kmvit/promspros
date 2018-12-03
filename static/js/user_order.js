

function button_order_user() {
	var order = document.querySelectorAll('.orders-mini');
	var ads = document.querySelectorAll('.wrap__other');

	var iter_order;
	for (let i = 0; i < order.length; i++) {
		iter_order = order[i];
		var iter = 0;
		for (let j = 0; j < ads.length; j++) {
			if (ads[j] != undefined) {	
				if (ads[j].getAttribute('data-date') == iter_order.getAttribute('data-date') &&
					ads[j].getAttribute('data-user') == iter_order.getAttribute('data-user') &&
					ads[j].getAttribute('data-type') == iter_order.getAttribute('data-type')) {
					other_ads = ads[j].querySelector('.other__ads')
					var button = order[i].querySelector('.button__other__order')
					iter++;
					if (button != null) {
						
						button.classList.remove('button_order_user_none');
						button.classList.add('button_order_user');

						var count_span = button.querySelector('.count__orders')
						count_span.textContent = iter

						button.addEventListener('mouseup', show_block);
					}
				} else {
					iter = 0;
				}	
			}
		}
	}

	function show_block(e) {
		var button_active = e.target;
		if (button_active.getAttribute('data-count') == '0') {
			button_active.setAttribute('data-count', '1')
			while (true) {
				if (button_active.classList.contains('orders-mini') == false) {
					button_active = button_active.parentElement;
				} else {
					button_active = button_active;
					break;
				}
			};
			var hide_block = button_active.querySelector('.ads_none');

			var item_date = button_active.getAttribute('data-date');
			var item_user_id = button_active.getAttribute('data-user');
			var wrapper_list = button_active;

			while (true) {
				if (wrapper_list.classList.contains('orders-mini-wrapper') == false) {
					wrapper_list = wrapper_list.parentElement;
				} else {
					wrapper_list = wrapper_list;
					break;
				}
			}

			additional_ads = wrapper_list.querySelectorAll('.wrap__other')
			if (additional_ads.length != 0) {
					hide_block.classList.remove('ads_none');
					hide_block.classList.add('additional_ads');
					title = hide_block.children[0];
					title.classList.add('other__user__title');
					title.classList.remove('title__none');
				for (let i = 0; i < additional_ads.length; i++) {
					var additional_ads_date = additional_ads[i].getAttribute('data-date');
					var additional_ads_user = additional_ads[i].getAttribute('data-user');
					if (additional_ads_date == item_date && additional_ads_user == item_user_id) {
						var blocks_adds = button_active.querySelector('.add_block');
						blocks_adds.insertAdjacentHTML('beforeEnd', additional_ads[i].innerHTML);
					}
				}
			}
		} else if (button_active.getAttribute('data-count') == '1') {
			button_active.setAttribute('data-count', '0')
			while (true) {
				if (button_active.classList.contains('orders-mini') == false) {
					button_active = button_active.parentElement;
				} else {
					button_active = button_active;
					break;
				}
			}
			hide_block = button_active.querySelector('.additional_ads');
			hide_block.classList.add('ads_none');
			hide_block.classList.remove('additional_ads');
			childs = hide_block.children;
			clear_block = button_active.querySelector('.add_block');
			clear_block.innerHTML = '';
			
		}
	}
};
button_order_user();

