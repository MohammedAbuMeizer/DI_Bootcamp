function myFunction(selTag) {
  var x = selTag.options[selTag.selectedIndex].text;
   document.getElementById("result").innerHTML = "You selected: " + x;
}

function addOption(){
	let select = document.getElementById("genres");
	let option = document.createElement("option");
	option.text = "classic";
	option.value = "classic";
	option.selected = true;
	select.add(option);

}

addOption();