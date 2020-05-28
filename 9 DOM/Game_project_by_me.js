var restart = document.querySelector('#b');

var box = document.querySelectorAll('td');



function clearboard() {
	for (var i = 0; i < box.length; i++) {
	box[i].textContent = "";
	}
	
}

restart.addEventListener('click', clearboard)


function gameon() {
	if (this.textContent === '') {
		this.textContent = 'X';
	}
	else if (this.textContent === 'X') {
		this.textContent = 'O';
	}
	else{
		this.textContent = '';
	}
}

for (var i = 0; i < box.length; i++) {
	box[i].addEventListener('click', gameon)
}