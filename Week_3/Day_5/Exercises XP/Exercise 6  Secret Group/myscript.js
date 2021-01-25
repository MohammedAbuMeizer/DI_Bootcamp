let names = ["Jack", "Philip", "Sarah", "Amanda", "Bernard", "Kyle"];
names.sort();
let secret = ""

for (let i = 0; i < names.length; i++) {
	secret = secret +names[i].charAt(0);
}

console.log(secret);