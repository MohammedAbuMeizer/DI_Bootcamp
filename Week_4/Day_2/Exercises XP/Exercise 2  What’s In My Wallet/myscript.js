let Quarters  = 0.25;
let Dimes = 0.10;
let Nickels = 0.05;
let Pennies = 0.01;
let totalAmount = 4.25;

let change = [Quarters,Dimes,Nickels,Pennies];
let arr = [25, 20, 5, 0];

function changeEnough(arr,totalAmount) {

	let resultCal = 0;
	for (var i = 0; i < arr.length; i++) {
		resultCal = resultCal + arr[i] * change[i];
	}

	if (resultCal>totalAmount) {
		console.log(true);
		return true;
	}else {
		console.log(false);
		return false;
	}

}


changeEnough([2, 100, 0, 0], 14.11);//false
changeEnough([0, 0, 20, 5], 0.75);//true