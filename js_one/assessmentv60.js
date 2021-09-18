var firstName = prompt("Enter First Name");
var lastName = prompt("Enter Last Name");
var age = prompt("Enter Spy age:");
var height = prompt("Enter spy height in cm:");
var petName = prompt("Enter spy pet name");

var flag = true;

if(firstName[0]!=lastName[0])
  flag = false;

if(age>30 && age <20)
  flag = false;

if(height<170)
  flag = false;

if(petName[petName.length - 1]!='y' && petName[petName.length - 1]!='Y')
flag= false;

if(flag)
console.log("You win the quiz");
else
console.log("You lost the quiz");
