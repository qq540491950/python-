from urllib.request import HTTPPasswordMgrWithDefaultRealm, HTTPBasicAuthHandler, build_opener
from urllib.error import URLError

# 直接弹窗认证的网站
username = "lirt"
password = "123456"
url = "http://localhost:8080/sxgljh"

p = HTTPPasswordMgrWithDefaultRealm()
p.add_password(None, url, username, password)
auth_handler = HTTPBasicAuthHandler(password_mgr=p)
opener = build_opener(auth_handler)

try:
    result = opener.open(url)
    html = result.read().decode("utf-8")
    print(html)
except URLError as e:
    print(e.reason)
