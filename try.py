import requests

#Example API Endpoint
url = ""

#Make a get Request to API
response = requests.get(url)

#Check status if the Request was succesful
print("StatusCode :",response.status_code)