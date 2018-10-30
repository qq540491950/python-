import http.cookiejar
import urllib.request

cookie = http.cookiejar.CookieJar()
handler = urllib.request.HTTPCookieProcessor(cookie)
opener = urllib.request.build_opener(handler)
res = opener.open("http://www.baidu.com")
for item in cookie:
    print(item.name + "=" + item.value)
