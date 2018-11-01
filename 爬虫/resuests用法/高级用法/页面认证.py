import requests
from requests.auth import HTTPBasicAuth

'''
两种方式都可以
'''
res = requests.get("http://www.baidui.com", auth=HTTPBasicAuth("username", "password"))
# res = requests.get("http://www.xxx.com", auth=("username", "password"))
print(res.status_code)
