let sentence = "The movie is not that bad really, I like it" ;
let wordNot =0 ;
let wordBad =0;
let replceWord = "";

let sln=sentence.length;

wordNot = sentence.indexOf("not");//first index of not
wordBad = sentence.indexOf("bad");//first index of bad



//-1 if there is no word using or 

if (wordNot < wordBad || wordNot == -1) {
	replceWord = sentence.slice(wordNot,wordBad+3);
	sentence = sentence.replace(replceWord,"good");
	console.log(sentence);
	document.getElementById("result").innerHTML = sentence.toString() ;
}else if (wordBad == -1 || wordBad == -1) {
		document.getElementById("result").innerHTML = sentence.toString() ;

}