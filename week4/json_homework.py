import requests
import json

data = {'title': 'homework', 'body': 'geunhye kim', 'userId': 1}
response = requests.post(
    'https://jsonplaceholder.typicode.com/posts', data=data)

data = json.loads(response.text)

file = open("result.txt", "w")

file.write('title: ' + data['title'] + '\n')
file.write('body: ' + data['body'] + '\n')
file.write('userId: ' + data['userId'])

file.close()