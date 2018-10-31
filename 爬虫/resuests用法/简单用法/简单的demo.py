import requests

res = requests.get("http://www.baidu.com")
print(type(res))
print(res.status_code)
print(type(res.text))
# print(str(res.content, "utf-8"))
res.encoding = "utf-8"
print(res.text)
print(res.cookies)
