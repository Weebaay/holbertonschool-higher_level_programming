// 3-script.js

let toggleButton = document.querySelector('#toggle_header');

toggleButton.addEventListener('click', function() {
	// trouver l'élement header
	let header = document.querySelector('header');

	
    // Vérifier la classe actuelle et basculer
    if (header.classList.contains('red')) {
        header.classList.remove('red');
        header.classList.add('green');
    } else {
        header.classList.remove('green');
        header.classList.add('red');
    }
});