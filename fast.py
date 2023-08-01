import requests


url = 'https://tamiella.azurewebsites.net/predict'
headers = {
   'accept': 'application/json',
   'Content-Type': 'application/json',
}


data = '{"sepal_length": 6.2,"sepal_width": 3.4,"petal_length": 5.4,"petal_width": 2.3}'
response = requests.post(url, headers=headers, data=data)
response.text
