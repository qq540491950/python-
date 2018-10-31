import requests

# requests字节流读取
res = requests.get("https://github.com/favicon.ico")
with open("favicon.ico", "wb") as f:
    f.write(res.content)
