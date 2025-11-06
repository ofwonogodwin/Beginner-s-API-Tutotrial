import requests

#Bitnob API endpoint
url = "https://api.bitnob.co"

# Getting the data
response = requests.get(url)

#Checking the Status Code
print("Status Code :",response.status_code)

#Now the JSON data
print("Json Data :",response.json())