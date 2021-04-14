import requests
#requests.get('http://127.0.0.1:5000/status')
#print(response.status_code)
response = requests.post(
    'http://127.0.0.1:5000/send',
    data='123'
)
print(response.text)