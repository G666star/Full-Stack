var x = document.querySelectorAll('.one')
var y = document.querySelector('#two')

y.addEventListener('mouseover',function(){
  y.textContent = "Mouse currently Over";
  y.style.color = 'red';
})

// WORKS FINE WITH UNIQUE ID

// x.addEventListener('mouseover' ,function(){
// 	x.textContent = 'ttt mmm iii';
// })



// CHANGES EACH H1 IF HOVERED OVER ANY H1

// for (var i = 0; i < x.length; i++) {
// 	x[i].addEventListener('mouseover' ,function(){
// 	for (var i = 0; i < x.length; i++) {
// 		x[i].textContent = 'ytrewq'
// 	}
// })
// }

// WRONG METHOD

// x.addEventListener('mouseover',function () {
// 	for (var i = 0; i < x.length; i++) {
// 		x[i].textContent = 'qwerty';
// 	}
// })

