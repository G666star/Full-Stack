/// PART 8 - LOOP EXERCISES
// Before we continue on with your project, let's practice some loops!
// You'll have just two problems, but you'll need to use each loop type we
// learned about to solve them!


///////////////////
//// PROBLEM 1 ///
/////////////////

// Use a For Loop to print (console.log()) out the word "hello" 5 times.
//
// Do this with a While Loop and a For Loop

// While Loop
var x=1
while(x<6){
	console.log('hello')
	x=x+1
}

// For Loop
for (var i = 0; i < 5; i++) {
	console.log('hi')
}



/////////////////
// PROBLEM 2 ///
///////////////

// Use Loops to console.log() (print out) all the odd numbers from 1 to 25
// Do this using two methods, a while loop and a for loop

// METHOD ONE
// While Loop
var x = 1
while(x<26){
	if (x%2!=0) {
		console.log('no. is '+x)
	}
	x++
}
// METHOD TWO
// For Loop
for (var i = 0; i <= 25; i++) {
	if (i%2!==0) {
		console.log('num is '+i)
	}
}