import requests

#Example API endpoint
url = "https://api.github.com/users/octocat"

#Make a GET request to the API
response = requests.get(url)

#Check status/If the request was succesful
print("StatusCode :",response.status_code)

#Print JSON rsponse
print("Json Response")
print(response.json())