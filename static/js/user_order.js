
function button_order_user() {
	var order = document.querySelectorAll('.orders-mini');
	var ads = document.querySelectorAll('.wrap__other');

	for (let i = 0; i < order.length; i++) {
		order[i].addEventListener('mouseenter', show_button);
		order[i].addEventListener('mouseleave', hide_button);
	}

	function show_button(e) {
		var data_date = e.target.getAttribute('data-date');
		var data_user = e.target.getAttribute('data-user');
		for (let i = 0; i < order.length; i++) {
			var order_date = order[i].getAttribute('data-date');
			var order_user = order[i].getAttribute('data-user');

			if (order_date == data_date &&
				order_user == data_user &&
				order[i].getAttribute('data-ads')) {
				console.log(order[i])
				console.log(e.target)
				var button = e.target.querySelector('.button__other__order');
				button.classList.add('button_order_user');
				button.classList.remove('button_order_user_none');
				button.addEventListener('mouseup', show_block);
			}
		}

	}

	function hide_button(e) {
		var button = e.target.querySelector('.button__other__order');
		button.classList.add('button_order_user_none');
		button.classList.remove('button_order_user');
		
	}

	function show_block(e) {
		var button_active = e.target;
		if (button_active.textContent == 'Заказы от пользователя') {
			button_active.textContent = 'Скрыть';
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
		} else if (button_active.textContent == 'Скрыть') {
			button_active.textContent = 'Заказы от пользователя';
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
