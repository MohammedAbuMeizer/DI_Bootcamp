let colorAr = ["red","blue","green","white","black"];
let colorSt = "" ;

for (var i = 0; i < colorAr.length; i++) {
	colorSt = colorSt + "My #" + (i+1) + " choice is " + colorAr[i]+"   ,    ";
}
	document.getElementById("result").innerHTML = colorSt;
