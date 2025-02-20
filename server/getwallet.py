import requests
response = requests.get("http://localhost:8000/wallet")
print(response.json())