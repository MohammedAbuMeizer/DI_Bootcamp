var num1 = prompt('please enter the first number');
var num2 = prompt('please enter the second number');

console.log(num1+'+'+ num2 +'='+math.sum(num1,num2));
console.log(num1+'-'+ num2 +'='+math.subtract(num1,num2));
console.log(num1+'*'+ num2 +'='+math.multiply(num1,num2));
console.log(num1+'/'+ num2 +'='+math.divide(num1,num2));

var sum=num1+'+'+ num2 +'='+math.sum(num1,num2);
var sub=num1+'-'+ num2 +'='+math.subtract(num1,num2);
var mul=num1+'*'+ num2 +'='+math.multiply(num1,num2);
var div=num1+'/'+ num2 +'='+math.divide(num1,num2);


document.getElementById("calculator").innerHTML = sum + '   |   '+sub+'   |   '+mul+'   |   '+div;
