let numNights = "" ;
let destination = "";
let numDcars = "";

function hotel_cost(numNights) {
    let costHotel = 0;
        while(isNaN(numNights) || (numNights == "")) {
            numNights = prompt("how many days you want to rent room ? ");
        }

        costHotel = numNights *140 ;
        console.log(costHotel);

        return costHotel;
}


function plane_ride_cost(destination) {

    let priceDest = 0;

    destination = prompt("where is your destination ? ");

    while(!isNaN(destination) || (destination == "")) {
            destination = prompt("where is your destination ? ");
        }

    if (destination == "London") {

        priceDest = 183 ;

    }else if (destination == "Paris") {
        priceDest = 220 ;
    }else {
        priceDest = 300 ;
    }
    console.log(priceDest);
    return priceDest;

}


function rental_car_cost(numDcars) {
    let priceDcar = 0 ;

    while(isNaN(numDcars) || (numDcars == "")) {
            numDcars = prompt("how many days you want to rent car? ");
        }

        priceDcar = priceDcar + (numDcars*40 );
        console.log(priceDcar);

        return priceDcar;

}


function total_vacation_cost() {

    let result = "";
    result = result + "The car cost : " + rental_car_cost(numDcars) + " $ <br>" 
                    + "The hotel cost : " + hotel_cost(numNights) + " $ <br>"
                    + "The plane ride cost : " + plane_ride_cost(destination) + "$";
    return result;                  

}

document.getElementById("result").innerHTML = total_vacation_cost();