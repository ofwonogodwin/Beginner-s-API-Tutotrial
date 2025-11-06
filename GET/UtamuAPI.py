import requests

#UTAMU Api endpoint
url = "https://api.github.com"

#The Response Data
response = requests.get(url)

#Getting the Response Data
print("Status Code:",response.status_code)

#JSON Data
print("Json Data :",response.json())