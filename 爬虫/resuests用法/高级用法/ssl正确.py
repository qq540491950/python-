import requests

# 正确返回，但是有警告
response = requests.get('https://www.12306.cn', verify=False)
print(response.status_code)
