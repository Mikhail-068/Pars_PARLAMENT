import json


with open('Person2.json') as f:
    man = json.load(f)

print(len(man))