import urllib.request
import json

url = 'https://api.github.com/repos/python/cpython'
response = urllib.request.urlopen(url)
data = json.loads(response.read().decode('utf-8'))

print(f"Repository: {data['name']}")
print(f"Description: {data['description']}")
print(f"Stars: {data['stargazers_count']}")
