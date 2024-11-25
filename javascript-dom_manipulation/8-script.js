// 8-script

document.addEventListener('DOMContentLoaded', () => {
	// Sélectionner l'élément avec l'ID 'hello'
	const helloElement = document.getElementById('hello');

fetch('https://hellosalut.stefanbohacek.dev/?lang=fr')
	.then(response => response.json())
	.then(data => {
		helloElement.textContent = data.hello;
	})
	.catch(error => {
		console.error('Erreur lors de la requête:', error);
		helloElement.textContent = 'Erreur de chargement';
	});
});
