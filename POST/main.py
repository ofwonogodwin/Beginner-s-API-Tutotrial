import requests

#The API End Point
url = "https://jsonplaceholder.typicode.com/posts"

#The data we want to send
data = {
    "Name":"Godwin Ofwono",
    "Mother":"Getrude Nekesa",
    "title":"Learning APIs with ChatGPT",
    "body":"This is my first POST request in Python",
    "userId":1
}
 #Send a Post Request
response = requests.post(url,json=data)

#Print the Status Code and Results
print("Status Code :",response.status_code)
print("Response Data")
print(response.json())
