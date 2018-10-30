import http.cookiejar
import urllib.request

cookie = http.cookiejar.LWPCookieJar()
cookie.load("cookies1.txt", ignore_discard=True, ignore_expires=True)
handler = urllib.request.HTTPCookieProcessor(cookie)
opener = urllib.request.build_opener(handler)
res = opener.open("http://www.baidu.com")
with open("./baidu.xx", "w", encoding="utf-8") as f:
    f.write(res.read().decode("utf-8"))
