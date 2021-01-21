let x = prompt("enter the value of x");
let y =prompt("enter the value of y");

if (x==5 && y==2) {
	document.getElementById("ex1").innerHTML = "x is the biggest number";

}

var newdog = "Chihuahua";
document.getElementById("ex2-1").innerHTML = newdog.length;
document.getElementById("ex2-2").innerHTML = newdog.toUpperCase();
document.getElementById("ex2-3").innerHTML = newdog.toLowerCase();

let newdog_word= prompt("enter the correct name of the dog");

if (newdog == newdog_word) {
	document.getElementById("ex2-4").innerHTML = " I love Chihuahua, its my favorite dog breed ";

}else{
			document.getElementById("ex2-4").innerHTML = " I dont care, I prefer cats ";
			console.log('I dont care, I prefer cats');

}

var num = prompt("enter your number to check if even or not");

if (num%2 == 0) {
		document.getElementById("ex3").innerHTML = " your num is even ";

}else{
			document.getElementById("ex3").innerHTML = " your num is not even ";

}

let users = ["Lea123", "Princess45", "cat&doglovers", "helooo@000"];

if (users.length == 0 ) {
		document.getElementById("ex4-1").innerHTML = " no one is online" ;

}else if (users.length== 1 ){

	document.getElementById("ex4-1").innerHTML = users[0] + " is online ";
}else if(users.length == 2 ){
		document.getElementById("ex4-1").innerHTML = users[0]+" "+users[1] + " is online ";

}else {
	var numm = users.length - 2 ;
		document.getElementById("ex4-1").innerHTML = users[0]+" "+users[1] + " and " + numm + "users are online ";

}