import requests

cookies = 'l_n_c=1; q_c1=583e58544657442499262f5daaf7e0ee|1540986913000|1540986913000; _xsrf=ac2d5a6978bfbc491ec72ca2ec640717; r_cap_id="MTExMTQzN2JkYjVlNDVhOTlkN2ZmNDg0YzU2OGFhODA=|1540986913|83389e13e0fc3591d0cbd5605fcc29e1e4722528"; cap_id="ODQ3ZDliZjNhNTE1NDNjZDk1ZDkwNWUxZjhkODk2YWM=|1540986913|11a6289b873cc36befb68453641e2191dc80d6a4"; l_cap_id="MTBmNTc3NTc5ZWYyNGUwYWI5YzBhYTQzMjg5NjQ1ZjU=|1540986913|1262666fbcc267726514880ea6fe0c0f396d8b57"; n_c=1; d_c0="AJAneD6Scg6PTgZLI2c00A-i9TNXcrwXd6g=|1540986916"; _xsrf=4frMCE1esvRodPzgNmp3wwf8zGhDTSXg; _zap=8b82db79-1f0b-447c-ada3-611f4ab7b547; __utma=51854390.1951255438.1540986917.1540986917.1540986917.1; __utmc=51854390; __utmz=51854390.1540986917.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __utmv=51854390.000--|3=entry_date=20181031=1; tgw_l7_route=69f52e0ac392bb43ffb22fc18a173ee6; capsion_ticket="2|1:0|10:1540989754|14:capsion_ticket|44:ZmM5YTU1NWNiN2RiNDQ4ZmIwNDZlNmNiMWI2ZmFkNzM=|3c99d9539489b502ac2ebeda887b765295a2434745802bac8ae96af4d544afd0"; z_c0="2|1:0|10:1540989762|4:z_c0|92:Mi4xb1VhN0FnQUFBQUFBa0NkNFBwSnlEaVlBQUFCZ0FsVk5RdkhHWEFDdzRtZG4wdWkzYTVkMFdXTVRTMGgwTXRBV05R|8a27f85e30d067f9fb026d208f36b0cb372644ee4e35f2fb3890ca4f22046d34"'
headers = {
    # "cookies" = 'l_n_c=1; q_c1=583e58544657442499262f5daaf7e0ee|1540986913000|1540986913000; _xsrf=ac2d5a6978bfbc491ec72ca2ec640717; r_cap_id="MTExMTQzN2JkYjVlNDVhOTlkN2ZmNDg0YzU2OGFhODA=|1540986913|83389e13e0fc3591d0cbd5605fcc29e1e4722528"; cap_id="ODQ3ZDliZjNhNTE1NDNjZDk1ZDkwNWUxZjhkODk2YWM=|1540986913|11a6289b873cc36befb68453641e2191dc80d6a4"; l_cap_id="MTBmNTc3NTc5ZWYyNGUwYWI5YzBhYTQzMjg5NjQ1ZjU=|1540986913|1262666fbcc267726514880ea6fe0c0f396d8b57"; n_c=1; d_c0="AJAneD6Scg6PTgZLI2c00A-i9TNXcrwXd6g=|1540986916"; _xsrf=4frMCE1esvRodPzgNmp3wwf8zGhDTSXg; _zap=8b82db79-1f0b-447c-ada3-611f4ab7b547; __utma=51854390.1951255438.1540986917.1540986917.1540986917.1; __utmc=51854390; __utmz=51854390.1540986917.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __utmv=51854390.000--|3=entry_date=20181031=1; tgw_l7_route=69f52e0ac392bb43ffb22fc18a173ee6; capsion_ticket="2|1:0|10:1540989754|14:capsion_ticket|44:ZmM5YTU1NWNiN2RiNDQ4ZmIwNDZlNmNiMWI2ZmFkNzM=|3c99d9539489b502ac2ebeda887b765295a2434745802bac8ae96af4d544afd0"; z_c0="2|1:0|10:1540989762|4:z_c0|92:Mi4xb1VhN0FnQUFBQUFBa0NkNFBwSnlEaVlBQUFCZ0FsVk5RdkhHWEFDdzRtZG4wdWkzYTVkMFdXTVRTMGgwTXRBV05R|8a27f85e30d067f9fb026d208f36b0cb372644ee4e35f2fb3890ca4f22046d34"',
    "Host": "www.zhihu.com",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.67 Safari/537.36"
}
jar = requests.cookies.RequestsCookieJar()
for cookie in cookies.split(";"):
    key, value = cookie.split("=", 1)
    jar.set(key, value)
res = requests.get("http://www.zhihu.com", cookies=jar, headers=headers)

try:
    with open("./zhihu.html", "w", encoding="utf-8") as f:
        f.write(res.text)
except Exception as e:
    print(e)
