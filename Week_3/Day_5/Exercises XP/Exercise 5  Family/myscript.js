let family = {
  name: "mohammed",
  age: 26 ,
  hoppy: "coding",
  tall: 185 ,
  weight: 90
}

for (property in family) {
   console.log(`property= ${property} `)
}

for (property in family) {
   console.log(`value = ${family[property]}`)
}