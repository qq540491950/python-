from urllib.error import URLError
from urllib.request import ProxyHandler, build_opener

proxy_handler = ProxyHandler({
    "http": "http://183.6.117.104:8080",
    "https": "https://175.148.76.53:1133"
})

opener = build_opener(ProxyHandler)
try:
    res = opener.open("https://www.baidu.com")
    # print(res.read().decode("utf-8"))
    with open("./baidu.txt", "w", encoding="utf-8") as f:
        f.write(res.read().decode("utf-8"))
except URLError as e:
    print(e.reason)
