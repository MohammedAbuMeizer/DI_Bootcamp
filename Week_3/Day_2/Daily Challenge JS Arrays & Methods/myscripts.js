let fruits = ["Banana", "Apples", "Oranges", "Blueberries"];

fruits.shift();

document.getElementById("shift").innerHTML = fruits.toString();

fruits.sort();

document.getElementById("sort").innerHTML = fruits.toString();

fruits.push("kiwi");

document.getElementById("push").innerHTML = fruits.toString();

fruits.reverse();
fruits.pop();
fruits.sort();

document.getElementById("pop").innerHTML = fruits.toString();

fruits.reverse();

document.getElementById("reverse").innerHTML = fruits.toString();

let moreFruits = ["Banana", ["Apples", ["Oranges"], "Blueberries"]];

var x = moreFruits[1][1][0];

document.getElementById("orange").innerHTML = x;

