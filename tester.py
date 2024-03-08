import requests

flask_app_url = 'http://127.0.0.1:5000'

# Data to be sent with the request
data1 = {'order_name': 'Yeji', 'order_email': 'corew531@gmail.com', 'order_total': '$123.45'}
response = requests.post(flask_app_url, data=data1)
print("Response message:", response.text)
