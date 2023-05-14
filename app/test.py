import requests

response = requests.get("http://dimanova12.pythonanywhere.com/all")
print(response.json())
