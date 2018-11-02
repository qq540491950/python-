from pyquery import PyQuery as pq

html = '''
<div id="container">
    <ul class="list">
         <li class="item-0">first item</li>
         <li class="item-1"><a href="link2.html">second item</a></li>
         <li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
         <li class="item-1 active"><a href="link4.html">fourth item</a></li>
         <li class="item-0"><a href="link5.html">fifth item</a></li>
     </ul>
 </div>
'''
# 查找子孙节点需要find()方法,传入的参数事CSS选择器
doc = pq(html)
items = doc(".list")
print(type(items), items, sep="\n")
lis = items.find("li")
print(type(lis), lis, sep="\n")
# 只查子节点用childre()方法 也可以传入CSS选择器
lis1 = items.children()
print(type(lis1), lis1, sep="\n")
# 查找父节点调用了 parents() 方法 也可以传入css选择器
# 兄弟节点 siblings() 参数css选择器
