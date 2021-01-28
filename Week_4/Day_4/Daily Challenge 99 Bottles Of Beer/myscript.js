let number = parseInt(prompt("Enter number want us to start with"));
let sentence = "bottles of beer on the wall";
let sentence2 = "down, pass it around"
let result = "";
if (!(number <= 0)) {
	for (let i = 0; i <= number; i++) {
		number = number -i;
		if (number != 0 && number > i) {
			result = result+(number + " " + sentence + "<br>" );
			for (let j = 0; j < i ; j++) {
				result = result + number + " " + sentence + "<br>";
		}
			result = result+ "Take "+(i+1) + " "+sentence2 + "<br>";
			document.getElementById("result").innerHTML = result ;
		} 
		else {
			result = result + (number + " " + sentence + "<br>" + "Take "+(number) + " "+sentence2 + "<br>");
			document.getElementById("result").innerHTML = result;

		}
	}
}