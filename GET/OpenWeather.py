#This is to cater for the Open Weather APIs

import requests

#Open Weather API endpoint
url = "https://api.github.com"

#Checking Response
response = requests.get(url) 

# Response Status Code
print("Status Code :",response.status_code)

# The JSON Data
print("Json Data :",response.json())