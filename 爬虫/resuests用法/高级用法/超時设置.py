import requests

'''
请求分为两个阶段,即connect和read
timeout = connect + read
如果要分别指定，传入一个元组
如果要永久等待 设为None或者不加参数
'''
# time = 1
time = (5, 10)
res = requests.get("http://www.taobao.com", timeout=time)
print(res.status_code)
