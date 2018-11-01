from bs4 import BeautifulSoup

html = """
<html>
    <head>
        <title>The Dormouse's story</title>
    </head>
    <body>
        <p class="story">
            Once upon a time there were three little sisters; and their names were
            <a href="http://example.com/elsie" class="sister" id="link1">
                <span>Elsie</span>
            </a>
            <a href="http://example.com/lacie" class="sister" id="link2">Lacie</a>
            and
            <a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>
            and they lived at the bottom of a well.
        </p>
        <p class="story">...</p>
"""
soup = BeautifulSoup(html, "lxml")
# print(soup.p.contents) 直接子节点的列表

# 调用children属性 子节点
for i, child in enumerate(soup.p.children):
    print(i, child)

# 调用descendants属性 子孙节点
for i, child in enumerate(soup.p.descendants):
    print(i, child)
