import json

x =  '{ "name":"John", "age":30, "city":"New York"}'

y = json.loads(x)  #json to python
print(y)
print(y["age"])


x_dict = {
  "name": "John",
  "age": 30,
  "city": "New York"
}

json_data = json.dumps(x_dict) #python to json
print(json_data)