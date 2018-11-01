import requests

# http://user:password@host:port
'''
若需验证HTTP Basic Auth 使用http: // user: password@host: port
格式如例："https": "http://user:password@10.10.1.10:3128"
还支持SOCKS协议代理
proxies = {
    "http": "socks5://user:password@10.10.1.10:3128",
    "https": "socks5://user:password@10.10.1.10:1080"
}
'''
proxies = {
    "http": "http://10.10.1.10:3128",
    "https": "http://10.10.1.10:1080"
}
res = requests.get("http://www.taobao.com", proxies=proxies)
print(res.status_code)
