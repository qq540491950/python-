from lxml import etree

html = etree.parse("test.html", etree.HTMLParser())
# result = html.xpath("//ul//a")
# / 是获取直接子节点，而在 ul 节点下没有直接的 a 子节点，只有 li 节点，所以无法获取任何匹配结果
result = html.xpath("//ul/a")

print(result)
