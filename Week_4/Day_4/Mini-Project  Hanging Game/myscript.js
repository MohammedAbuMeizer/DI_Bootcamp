let sentence = prompt("enter a sentencs");
let wordHidden = "";
let result = "";
let temp = [] ;
let tempI = 0;




for (let i = 0; i < sentence.length; i++) {
	wordHidden = wordHidden + "*";
}
	console.log(wordHidden);
	let arrW = wordHidden.split("");
	let arrS = sentence.split("");


function setLetter(button) {
	let i = 0;
	let tempp = sentence.indexOf(button);
	while(tempp != "-1"){
		 temp[i] = tempp;
		 tempp = sentence.indexOf(button,tempp+1);
		 i++;
	}

		for (let i = 0; i < arr.length; i++) {

			tempI = temp[i];
			arr[tempI] = button;
			}
	
			result=arr.toString();
			console.log(result);

	


}

