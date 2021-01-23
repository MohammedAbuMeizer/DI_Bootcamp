let language = prompt("which language you speak ? ");
let result = language.toUpperCase();
switch(result){
	case "ENGLISH":
	document.getElementById("result").innerHTML = "Hello";
	case "FRENSH":
	document.getElementById("result").innerHTML = "bonjour";
	case "HEBROW":
	document.getElementById("result").innerHTML = "Shalom";
	break;
	default :
	document.getElementById("result").innerHTML = "01110011 01101111 01110010 01110010 01111001";
}