let verb = prompt("Enter a verb word");
const subStringIng = "ing";
let verbLn = verb.length ;


if ((verbLn >= 3 ) &&  (!verb.includes(subStringIng))) 
{
	if ((verb.charAt(verbLn-2) == "a" ) || (verb.charAt(verbLn-2) == "i" ) ||
	 (verb.charAt(verbLn-2) == "o" ) || (verb.charAt(verbLn-2) == "u" ) ||
	 (verb.charAt(verbLn-2) == "e" ) && (verb.charAt(verbLn -1 ) != "e")) {
		verb = verb + verb.charAt(verbLn-1) + subStringIng;
		document.getElementById("result").innerHTML = verb ;
	} else if ((verbLn >= 3 ) &&  (!verb.includes(subStringIng)) &&
	 (verb.charAt(verbLn -1) == "e") && (verb.charAt(verbLn-2) != "e")) {
	 	verb = verb.slice(0,-1);
		document.getElementById("result").innerHTML = verb + subStringIng ;
	} else if ((verbLn >= 3 ) &&  (!verb.includes(subStringIng)) &&
	 		   (verb.charAt(verbLn -1) == "e") && (verb.charAt(verbLn-2) == "e")) {
				document.getElementById("result").innerHTML = verb + subStringIng ;

	}	

}	

else if (verbLn >= 3 && verb.includes(subStringIng)){
	verb = verb + "ly";
	document.getElementById("result").innerHTML = verb ;

}else if (verbLn < 3) {
	 document.getElementById("result").innerHTML = verb ;

}