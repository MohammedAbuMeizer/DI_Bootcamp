let guestList = {
  randy: "Germany",
  karla: "France",
  wendy: "Japan",
  norman: "England",
  sam: "Argentina"
}

let person = prompt("Whats your name ? ");

if (person in guestList) {
	console.log("Hi Im " + person + " Im from " + guestList[person]);
}else{
	console.log("Hi! Im a guest");
}