let person1 = parseInt(prompt("Enter the age of person 1 :"));
let person2 = parseInt(prompt("Enter the age of person 2 :"));
let bigger ;
let younger ; 
let year =0 ; 
let date1 = new Date();
let result ;
let i = 0;

person1 = parseInt(date1.getFullYear()) - person1; //2021-1995
person2 = parseInt(date1.getFullYear()) - person2; //2021-2010




if (person1 > person2) {//26 > 11
	bigger = person1;//26
	younger = person2;//11
	i=younger;
	}else{
	bigger = person2;
	younger = person1;
	i=younger;
}


while ((bigger/2) >= i){
	i++;
	year= year+1;
	console.log(year);
}
	
	document.getElementById("divv").innerHTML = "The age of the younger is : " + younger + "<br>" +
	"The age of the bigger is : " + bigger + "<br>" + "the younger will be an half of the bigger in : "  



	document.getElementById("result").innerHTML = 
	parseInt(date1.getFullYear())+year-1;


