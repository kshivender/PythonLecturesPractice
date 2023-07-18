import json

f = open('dictionaryjson.json','r')
a = json.load(f)

b = input("Enter the word = ")
print(a.get(b))