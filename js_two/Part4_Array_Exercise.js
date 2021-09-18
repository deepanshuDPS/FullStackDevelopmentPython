// PART 4 ARRAY EXERCISE
// This is  a .js file with commented hints, its optional to use this.

// Create Empty Student Roster Array
// This has been done for you!
var roster = []

// Create the functionctions for the tasks


// ADD A NEW STUDENT

// Create a functionction called addNew that takes in a name
// and uses .push to add a new student to the array
function add(value)
{
  roster.push(value);
  console.log(roster);
}
// REMOVE STUDENT

// Create a functionction called remove that takes in a name
// Finds its index location, then removes that name from the roster

function remove(value){
for( var i = 0; i < roster.length; i++){
   if ( roster[i] === value) {
     roster.splice(i, 1);
     break;
   }
}
console.log(roster);
}
// HINT: http://stackoverflow.com/questions/5767325/how-to-remove-a-particular-element-from-an-array-in-javascript
//

// DISPLAY ROSTER
function display(){
  console.log(roster);
}
// Create a functionction called display that prints out the orster to the console.


// Start by asking if they want to use the web app
var enteredValue = prompt("Do you ready of adding or deleting (y/quit)")
while(enteredValue!=="quit"){

  enteredValue = prompt("Do functionction add,remove,display or quit");
  if(enteredValue==="add"){
    add(prompt("Enter Value to add:"))
  }
  else if(enteredValue==="remove"){
    remove(prompt("Enter Value to remove:"))
  }
  else if(enteredValue==="display")
    display()
  else if(enteredValue==="quit")
    break;
}
// Now create a while loop that keeps asking for an action (add,remove, display or quit)
// Use if and else if statements to execute the correct functionction for each command.
