import requests

#API endpoint
url = "https://jsonplaceholder.typicode.com/posts/1"

#Sending th Delete Request
response = requests.delete(url)

#Results.
print("Status Code:",response.status_code)

if response.status_code == 200:
    print("Succesfully Deleted the Resource")

else:
    print("Something went Wrong")
