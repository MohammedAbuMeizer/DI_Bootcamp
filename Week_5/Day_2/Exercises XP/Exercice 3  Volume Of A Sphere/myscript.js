
let radius = 0;
let volume = document.getElementById("volume");
let result = 0;

let calculatee = document.getElementById("submit");

function volumeOfSphere() {
	radius = Number.parseInt(document.getElementById("radius").value);
	result = (radius * radius * radius * 3.14 *4 / 3);
	volume.value  = result;
}

//volumeOfSphere();
