#Trying APIs

import requests

#The API endpoint
url = "https://api.github.com"

#Getting the response from the API
response = requests.get(url)

#Checking The ststus Code
print("Status Code :",response.status_code)

#The Jso Response
print("Response Data : ",response.json())