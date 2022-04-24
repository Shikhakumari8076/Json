import json
unique= '{"a":  1, "a":  2, "a":  3, "a": 4, "b": 1, "b": 2}'
json_obj = json.loads(unique)
print(json_obj)
