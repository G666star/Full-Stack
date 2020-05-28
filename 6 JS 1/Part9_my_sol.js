var fn = prompt('enter 1st name');
var ln = prompt('enter last name');
var a = prompt('enter age');
var h = prompt('enter height');
var p = prompt('enter pet name');
alert('ok saved');

if (fn[0] === ln[0] && a<30 && a>20 && h>=170 && p[p.length-1] === 'y') {
	console.log('heloo hi');
}

else{
	console.log('nothing');
}