from urllib import request, error

# error.URLError页面不存在返回 Not Found
try:
    res = request.urlopen("http://cuiqingcai.com/index.htm")
except error.URLError as e:
    print(e.reason)
