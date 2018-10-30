import urllib.parse
import urllib.request

data = bytes(urllib.parse.urlencode({"word": "hello"}), encoding="utf-8")
res = urllib.request.urlopen("http://httpbin.org/post", data=data)
print(res.read())
