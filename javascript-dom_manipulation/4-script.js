// 4-script

let addButton = document.querySelector('#add_item');

addButton.addEventListener('click', function() {

	let newElement = document.createElement('li');

	newElement.textContent = 'Item';

	let myList = document.querySelector('.my_list');
	myList.appendChild(newElement);
});
