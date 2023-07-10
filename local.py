import requests

res = requests.get('http://localhost:3000/api/v2/main/0')
print(res.json())
