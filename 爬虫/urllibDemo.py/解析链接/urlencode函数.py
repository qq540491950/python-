from urllib.parse import urlencode, parse_qs, parse_qsl, quote, unquote

# urlencode() 方法，它在构造 GET 请求参数的时候非常有用
params = {
    "name": "lirt",
    "age": 23
}
base_url = "http://www.baidu.com?"
url = base_url + urlencode(params)
print(url)

# 反序列化 类型：字典
query = "name=lirt&age=25"
print(parse_qs(query))

# 反序列化 类型：元组列表
print(parse_qsl(query))

# quote() 转换成url编码格式
name = "李瑞涛"
url1 = "http://www.baidu.com?name=" + quote(name)
print(url1)

url2 = "http://www.baidu.com?name=%E6%9D%8E%E7%91%9E%E6%B6%9B"
print(unquote(url2))
