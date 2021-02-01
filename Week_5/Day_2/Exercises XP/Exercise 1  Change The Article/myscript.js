let elements = document.getElementsByClassName("para_article");
elements[3].remove();

function removeH2() {

	let h2Elm = document.getElementsByTagName("h2");
	h2Elm[0].remove();

	}

let x = document.getElementById("h2El");
x.addEventListener("click",removeH2);


function reSize() {

	let h2Elm = document.getElementsByTagName("h1");
	let mat = Math.random() * 101 + "px";
	h2Elm[0].style.fontSize = mat;

	}

let y = document.getElementById("h1El");
y.addEventListener("click",reSize);

function hideEl() {
	elements[0].style.display = "none";
}
elements[0].addEventListener("click",hideEl);


let inputEl = document.getElementsByTagName("input");


function getValuesInput() {

	
	  x = document.createElement("TABLE");
	  x.setAttribute("id", "myTable");
	  document.body.appendChild(x);

	  var y = document.createElement("TR");
	  y.setAttribute("id", "myTr");
	  document.getElementById("myTable").appendChild(y);

	  var z = document.createElement("TD");
	  var l = document.createElement("TD");
	  var t = document.createTextNode(inputEl[0].value);
	  var m = document.createTextNode(inputEl[1].value);

	  z.appendChild(t);
	  l.appendChild(m);
	  document.getElementById("myTr").appendChild(z);
	  document.getElementById("myTr").appendChild(l);

}

getValuesInput();

