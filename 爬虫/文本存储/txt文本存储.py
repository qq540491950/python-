from pyquery import PyQuery as pq
import requests
# 本节我们要保存知乎发现页面的热门问题部分，将其问题和答案统一保存成文本形式

headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.67 Safari/537.36"
}
html = requests.get("https://www.zhihu.com/explore", headers=headers).text
doc = pq(html)
# 获取问题的集合
items = doc(".explore-tab .feed-item").items()
for item in items:
    question = item.find("h2").text()
    author = item.find('.author-link-line').text()
    answer = pq(item.find('.content').html()).text()
    with open("./zhifu.txt", "a", encoding="utf-8") as f:
        f.write("\n".join([question, author, answer]))
        f.write("\n" + "=" * 50 + "\n")
