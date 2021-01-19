let str = prompt("please enter numbers divided by comma and space : ");

function myFunction(){
	var result = "";
	var dived = str.split(", ");
	 for (var i = str.length - 1; i >= 0; i--) {
	 	if (isNAN(parseInt(str[i]) ==false ) {
	 	result= result * str[i];
	 }
	}
	 	document.getElementById("sentence").innerHTML = result;

}