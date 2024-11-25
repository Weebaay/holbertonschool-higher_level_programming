// 5-script

const changeHeader = document.getElementById('update_header');

changeHeader.addEventListener('click', () => {
	const headerElement = document.querySelector('header');
	headerElement.textContent = 'New Header!!!';
});