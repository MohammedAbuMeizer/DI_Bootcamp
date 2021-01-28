let stock = { 
    "banana": 6, 
    "apple": 0,
    "pear": 12,
    "orange": 32,
    "blueberry":1
}  

let prices = {    
    "banana": 4, 
    "apple": 2, 
    "pear": 1,
    "orange": 1.5,
    "blueberry":10
} 

let shoppingList =["banana", "orange", "apple"];

function myBill() {

    let sumPrice = 0;

    for (var i = 0; i < shoppingList.length; i++) {
        if ((shoppingList[i] in stock) && (stock[shoppingList[i]] != 0)) {

            stock[shoppingList[i]] = stock[shoppingList[i]] - 1;

            if (shoppingList[i] in prices) {
                sumPrice = sumPrice + prices[shoppingList[i]];
            }
        }       
    }
    console.log(stock);
    return sumPrice;
}

document.getElementById("result").innerHTML = "you have to pay : "+ myBill();