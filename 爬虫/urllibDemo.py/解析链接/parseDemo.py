from urllib.parse import urlparse, urlunparse, urlsplit, urlunsplit, urljoin


# 链接标准格式 scheme://netloc/path;parameters?query#fragment· 返回类型为元组
result = urlparse("http://www.baidu.com/index.html;user?id=5#comment")
print(type(result), result, sep="\n")

# urllib.parse.urlparse(urlstring, scheme='', allow_fragments=True) 返回类型为元组
result = urlparse('www.baidu.com/index.html;user?id=5#comment', scheme='https')
print(result)
# 合并
data = ['http', 'www.baidu.com', 'index.html', 'user', 'a=6', 'comment']
print(urlunparse(data))

# 截取  返回类型为元组
result = urlparse("http://www.baidu.com/index.html;user?id=5#comment")
print(result)

# data为可迭代对象
data = ['http', 'www.baidu.com', 'index.html', 'a=6', 'comment']
print(urlunsplit(data))

# urljoin()
print(urljoin('http://www.baidu.com', 'FAQ.html'))
print(urljoin('http://www.baidu.com', 'https://cuiqingcai.com/FAQ.html'))
print(urljoin('http://www.baidu.com/about.html', 'https://cuiqingcai.com/FAQ.html'))
print(urljoin('http://www.baidu.com/about.html', 'https://cuiqingcai.com/FAQ.html?question=2'))
print(urljoin('http://www.baidu.com?wd=abc', 'https://cuiqingcai.com/index.php'))
print(urljoin('http://www.baidu.com', '?category=2#comment'))
print(urljoin('www.baidu.com', '?category=2#comment'))
print(urljoin('www.baidu.com#comment', '?category=2'))
