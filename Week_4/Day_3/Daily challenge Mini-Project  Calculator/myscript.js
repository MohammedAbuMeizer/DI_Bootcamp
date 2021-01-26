
// Variables

// variable to pass the all the values to the display
let calcString = "";

// variable for the display div
let calcDisplay = document.getElementById("display");
//console.log(calcDisplay);

// function to recieve numbers and symbols
function my_f(btn){

    //console.log(btn);

    calcString = calcString + btn;
    //console.log(calcString);

    calcDisplay.innerHTML = calcString;

}


// function to calculate and output the result
function results(){

    let calcResult = eval(calcString);
    console.log(calcResult);

    calcDisplay.innerHTML = calcResult;

    calcString = calcResult;
}


// clear function
function clear1(){

    calcString = "";
    calcDisplay.innerHTML = 0;

}


// back function
function back(){

    // if more than 0 in display
    if (calcDisplay.innerHTML.length > 1){

        // slice up the last value in the string
        calcString = calcString.slice(0, -1);

        console.log(calcString);

        calcDisplay.innerHTML = calcDisplay.innerHTML.slice(0, -1)
    }

    else{

        calcDisplay.innerHTML = 0;

    }
}