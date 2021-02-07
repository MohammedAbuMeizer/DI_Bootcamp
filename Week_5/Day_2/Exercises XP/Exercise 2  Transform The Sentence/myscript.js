let boldArray = [];
let change = document.getElementById("par");
function getBold_items() {
	boldArray = document.getElementsByTagName("strong");
}

getBold_items();

function highlight() {
	for (let i = 0; i < boldArray.length; i++) {
		boldArray[i].style.color = "blue";
	}

}
function return_normal() {
	for (let i = 0; i < boldArray.length; i++) {
		boldArray[i].style.color = "black";
	}
}
//highlight();


