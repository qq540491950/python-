import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'
}
# res = requests.get("https://www.zhihu.com/explore")
res = requests.get("https://www.zhihu.com/explore", headers=headers)
with open("./zhihu.html", "w", encoding="utf-8") as f:
    f.write(str(res.text))
