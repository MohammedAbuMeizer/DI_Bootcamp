import json
sampleJson = """{ 
   "company":{ 
      "employee":{ 
         "name":"emma",
         "payable":{ 
            "salary":7000,
            "bonus":800
         }
      }
   }
}"""

json_lo = json.loads(sampleJson)
json_lo["company"]["employee"]["birth_date"] = True
print(json_lo["company"]["employee"]["payable"]["salary"])
print(json_lo)

y = json.dumps(json_lo)
with open("j.txt","w") as fil:
    fil.write(y)
print(y)