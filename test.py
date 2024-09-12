import requests

url = 'http://localhost:5000/question'

question = "I want to try some chicken spicy wings"
data = {'question': question}

response = requests.post(url, json=data)

print(response.json())