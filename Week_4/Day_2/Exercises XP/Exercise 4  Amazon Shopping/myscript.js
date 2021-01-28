let amazonBasket = {
    glasses: 1,
    books: 2,
    floss: 100
};

function checkBasket() {
	let item = prompt("Ask us for items : ");

	if (item in amazonBasket) {
		return "We have !!";
	}else{
		return "We dont have sorry";
	}
	}


document.getElementById("result").innerHTML = checkBasket();