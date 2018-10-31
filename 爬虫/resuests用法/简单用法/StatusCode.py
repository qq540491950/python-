import requests

res = requests.get("http://www.jianshu.com")
if not res.status_code == requests.codes.ok:
    exit()
else:
    print("Response Successfully!")
