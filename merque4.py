import json
x={'4': 5, '6': 7, '1': 3, '2': 4}
print(json.dumps(x, sort_keys=True,indent=4))
