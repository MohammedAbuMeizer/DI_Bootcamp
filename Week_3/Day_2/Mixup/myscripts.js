let str1 = 'mix';
let str2 = 'pod';

let strA = "";
let strB = "";
let strC = "";
let strD = "";

strA = str1.slice(0,2);
strB = str1.slice(2,3);
strC = str2.slice(0,2);
strD = str2.slice(2,3);

let newWord = strA + strD +" " +strC  + strB;
console.log(newWord);