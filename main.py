import requests

link = input("Please enter the link of the channel :")

response = requests.get(link)

print(response)