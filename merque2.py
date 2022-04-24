import json
dic={"name": "David", "class": "I",  "age": 6}
json.dumps(dic)
with open("meraki2.json","w")as dic1:
    json.dump(dic,dic1,indent=4)