from urllib import request, error

try:
    res = request.urlopen("http://cuiqingcai.com/index.htm")
except error.HTTPError as e:
    print(e.reason, e.code, e.headers, sep="\n")
