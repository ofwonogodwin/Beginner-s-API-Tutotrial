import requests

#The API End Point
url = "https://jsonplaceholder.typicode.com/posts/1"

#The Data we want to Update
data = {
    "name": "Rwoth Ofwono",
    "Title": "Learnt APIs with Chat GPT",
    "body":"Updated the name",
    "user Id":1
}

#Send a put request
response = requests.put(url,json=data)

#Printing Status code and the JSON data
print("Status Code :",response.status_code) 
print("Response")
print(response.json())