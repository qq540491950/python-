from pyquery import PyQuery as pq

doc = pq(url="http://cuiqingcai.com")
print(doc("title"))
# 文本初始化
doc1 = pq(filename="demo.html")
# 与字符串初始化类似
html = '''
<div>
    <ul>
         <li class="item-0">first item</li>
         <li class="item-1"><a href="link2.html">second item</a></li>
         <li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
         <li class="item-1 active"><a href="link4.html">fourth item</a></li>
         <li class="item-0"><a href="link5.html">fifth item</a></li>
     </ul>
 </div>
'''
doc2 = pq(html)
# 打印li节点的HTML文本
print(doc2("li"))
