import requests

flask_app_url = 'http://127.0.0.1:5000/email_list'

# Data to be sent with the request
data = {'order_name': 'Jennifer', 'order_email': 'enter test email', 'order_total': '$123.45'}
response = requests.post(flask_app_url, data=data)