// PART 4 ARRAY EXERCISE
// This is  a .js file with commented hints, its optional to use this.

// Create Empty Student Roster Array
// This has been done for you!
var roster = []

// Create the functions for the tasks

// ADD A NEW STUDENT

// Create a function called addNew that takes in a name
// and uses .push to add a new student to the array
function addNew() {
	var name = prompt('enter name to add')
	roster.push(name)
}

// REMOVE STUDENT

// Create a function called remove that takes in a name
// Finds its index location, then removes that name from the roster
function remove() {
	var rem_n = prompt('enter name to remove')
	index = roster.indexOf(rem_n)
	roster.splice(index,1)
}


// HINT: http://stackoverflow.com/questions/5767325/how-to-remove-a-particular-element-from-an-array-in-javascript
//

// DISPLAY ROSTER

// Create a function called display that prints out the roster to the console.
function display() {
	console.log(roster);
}

// Start by asking if they want to use the web app
var web = prompt('want u use? y or n');
var act = 'empty'
// Now create a while loop that keeps asking for an action (add,remove, display or quit)
if (web === 'y') {
	while(act !== 'quit'){
		var act = prompt('choose from add, remove, display, quit');
		
		if (act === 'add') {
		 addNew();
		}
		else if (act === 'remove') {
			 remove();
		}
		else if (act === 'display') {
			 display();
		}
		else{
			alert('thanks')
		}
	}
}
else{
	alert('thanks anyways')
}





// Use if and else if statements to execute the correct function for each command.
