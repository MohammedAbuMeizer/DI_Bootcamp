let start = 0 ;
let Elements = "";
let ElementsArr = [];
let sum = 0;

function mul23(start) {
	let ind = 0 ;
	ElementsArr[ind] = start;
	while ( start < 500 ){
		
			Elements = Elements +" "+ start;
			start = start + 23 ;
			ind = ind +1;
			ElementsArr[ind] = start;
	}

			for (let i = 0; i < ElementsArr.length-1; i++) {
				sum = sum + ElementsArr[i];			}

	console.log(ElementsArr);
	console.log("Elements : " + Elements);
	console.log("sum : " + sum);
	return sum;
}


document.getElementById("result").innerHTML = mul23(start);