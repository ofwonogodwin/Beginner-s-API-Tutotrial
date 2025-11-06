import requests

#Getting the EndPoint
url = "https://jsonplaceholder.typicode.com/posts/1"

#The Response Data
response = requests.get(url)

#The status Codepr
print("Status Code :",response.status_code)

#JSON Data
print("Json Data:",response.json())