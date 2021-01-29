let amount = prompt("Enter a list of 3 bills separated by comma : ");

let amountArr = amount.split(",");

let amoountBill = [] ;

let result = "";


function calculateTip(arr) {

    for (let i = 0; i < arr.length; i++) {
        if (arr[i] < 50) {
            amoountBill[i] = arr[i]*1.2;
            result = result + "Returant " + (i+1)+ " : " + amoountBill[i] + "$"+ "<br>";
        }else if (arr[i]> 200) {
            amoountBill[i] = arr[i] * 1.1;
            result = result + "Returant " + (i+1)+ " : " + amoountBill[i] + "$"+ "<br>";
        }
        else if (50 <= arr[i] <= 200 ) {
            amoountBill[i] = arr[i] * 1.15;
            result = result + "Returant " + (i+1)+ " : " + amoountBill[i] + "$"+ "<br>";
        }
    }

    return result;
}

document.getElementById("result").innerHTML = calculateTip(amountArr);
