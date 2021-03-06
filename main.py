import requests
import json

api_request = requests.get("http://api.openweathermap.org/data/2.5/weather?q=ankara&appid=24bb5a00705b2420901490c95519ab0b")

print(api_request)

result = json.loads(api_request.content)
