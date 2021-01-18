let str = prompt("please enter a new sentence : ");

if (str.includes("nemo") == true) {
	document.getElementById("sentence").innerHTML = "I found Nemo at [the order of the word you find nemo]!";
	console.log('“I found Nemo at [the order of the word you find nemo]!');
}	else{ console.log('I cant find Nemo');
	document.getElementById("sentence").innerHTML = "I cant find Nemo";


	}
