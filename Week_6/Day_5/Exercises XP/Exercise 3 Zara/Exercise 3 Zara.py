brand = {
    "name" : "Zara",
    "creation" : 1975,
    "creator_name" : "Amancio Ortega Gaona",
    "type_of_clothes" : ["men", "women", "children", "home"],
    "international_competitors" : ["Gap", "H&M", "Benetton"],
    "number_stores" : 7000,
    "major_color" : { "France" : "blue", "Spain" : "red", "US" : ["pink", "green"] },
}

brand["number_stores"] = 2 
print(f"The clients of Zara are : {brand['type_of_clothes']}")
brand["country_creation"] = "spain"

if "international_competitors" in brand :
    brand["international_competitors"].append("Desigual")


brand.pop("creation")

last = brand["international_competitors"]
print(f"last international competitor : {last[len(last) - 1]}")

major = brand["major_color"]
major_us = major["US"]

print(f"the major clothes’ colors in the US : {major_us}")

print(f"amount of key value pairs : {len(brand)}")

the_keys = ""

for key in brand.keys():
    print(f"   {key}")

##############################################################

more_on_zara = {"creation_date": 1975 ,
                "number_stores": 10000 
                }
for key1,val1 in more_on_zara.items():
    brand[key1] = val1

print(f" the value of the key number_stores : {brand['number_stores']}")



