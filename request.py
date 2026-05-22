import requests

param = {
    "page": 2,
    "limt":2
}
headers = {
    "Authorization": "Bearer TOKEN",
    "Content-Type": "application/json"
}
payload  = {
    "name" : "anurag",
    "role": "Engineer"
}
response = requests.get( "https://jsonplaceholder.typicode.com/users", params=param, headers=headers, timeout=5)

# timout prevents hanging requests.

print(response)
print(response.status_code)
print(response.raise_for_status())
# print(response.text)  # raw data in string

data = response.json()  #converts response into the python object
print(data)
print(type(data))
print(len(data))


response = requests.post( "https://jsonplaceholder.typicode.com/users", data=payload)
response = requests.post( "https://jsonplaceholder.typicode.com/users", json=payload)
# json instead of data because json converts dict → JSON and sets correct content-type header.
# Example:
# POST /users
# Content-Type: application/json



# for high scale system requests  is blocking instead aiohttp or httpx for async http.


# why we use session?
# It gives connection reuse
# cookies persistance
# performance 


# serialization = python(dict) to json
# deserialization = json to python(dict)
