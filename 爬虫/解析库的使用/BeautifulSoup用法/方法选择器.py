from bs4 import BeautifulSoup
import re

html = '''
<div class="panel">
    <div class="panel-heading">
        <h4>Hello</h4>
    </div>
    <div class="panel-body">
        <ul class="list" id="list-1" name="elements">
            <li class="element">Foo</li>
            <li class="element">Bar</li>
            <li class="element">Jay</li>
        </ul>
        <ul class="list list-small" id="list-2">
            <li class="element">Foo</li>
            <li class="element">Bar</li>
        </ul>
    </div>
</div>
'''
# find_all，顾名思义，就是查询所有符合条件的元素
# API find_all(name , attrs , recursive , text , **kwargs)
soup = BeautifulSoup(html, "lxml")

# name 根据节点名来查询元素
# print(soup.find_all(name="ul"))
# print(type(soup.find_all(name="ul")[0]))
for ul in soup.find_all(name="ul"):
    # print(ul.find_all(name="li"))
    for li in ul.find_all(name="li"):
        print(li.string)

# attrs 属性来进行查询
print(soup.find_all(attrs={"id": "list-1"}))
print(soup.find_all(attrs={"name": "elements"}))
# 另外的写法

print(soup.find_all(id="list-1"))
print(soup.find_all(class_="element"))

html1 = '''
<div class="panel">
    <div class="panel-body">
        <a>Hello, this is a link</a>
        <a>Hello, this is a link, too</a>
    </div>
</div>
'''
soup1 = BeautifulSoup(html1, "lxml")
# text参数可以匹配节点的文本
print(soup1.find_all(text=re.compile("link")))

'''
find() 方法返回的是单个元素，也就是第一个匹配的元素，
而 find_all() 返回的是所有匹配的元素组成的列表
'''
print(soup.find(name="ul"))

'''
find_parents() find_parent()
find_parents() 返回所有祖先节点，find_parent() 返回直接父节点。
find_next_siblings() find_next_sibling()
find_next_siblings() 返回后面所有兄弟节点，find_next_sibling() 返回后面第一个兄弟节点。
find_previous_siblings() find_previous_sibling()
find_previous_siblings() 返回前面所有兄弟节点，find_previous_sibling() 返回前面第一个兄弟节点。
find_all_next() find_next()
find_all_next() 返回节点后所有符合条件的节点, find_next() 返回第一个符合条件的节点。
find_all_previous() 和 find_previous()
'''