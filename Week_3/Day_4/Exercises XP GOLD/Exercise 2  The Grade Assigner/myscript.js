let score = prompt("Enter Your Grade ? ");

if (isNaN(score) == false) {
	if (score>90) {
		console.log("A");
		document.getElementById("result").innerHTML = "Your Level is A.";
	}else if (score > 80 && score <= 90 ) {
		document.getElementById("result").innerHTML = "Your Level is B.";

	}else if (score >= 70 && score <= 80) {
		document.getElementById("result").innerHTML = "Your Level is C.";

	}else if (score < 70 ) {
		document.getElementById("result").innerHTML = "Your Level is D.";

	}
	 
} else{
			document.getElementById("result").innerHTML = "what you have entered is NaN..";

}