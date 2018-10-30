import urllib.request
import urllib.parse

url = "http://httpbin.org/post"
# headers = {
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.67 Safari/537.36",
#     "Host": "httpbin.org"
# }
dict = {
    "name": "lirt"
}
data = bytes(urllib.parse.urlencode(dict), encoding="utf-8")
req = urllib.request.Request(url=url, data=data, method="POST")
# header另外一种方法
req.add_header("User-Agent", "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.67 Safari/537.36")
res = urllib.request.urlopen(req)
print(res.read().decode("utf-8"))
