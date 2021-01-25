let people = ["Greg", "Mary", "Devon", "James"]

people.splice(0, 1); 

people[people.indexOf("James")] = "Jason";
console.log(people);

people.push("Mohammed");
console.log(people);

for (var i = 0; i < people.length; i++) {
		console.log(people[i] );

}

var stopJ = people.indexOf("Jason") + 1;
console.log(stopJ);
for (var j = 0; j < stopJ; j++) {
		console.log(people[j] );

}

let copyAr = people.slice(1,2) + " , " + people.slice(2,3);
console.log(copyAr);

console.log(people.indexOf("Mary"));
console.log(people.indexOf("Foo"));

let last = people[people.length - 1];
console.log(last);