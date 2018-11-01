import requests
import re
import json
import time
import random
from requests.exceptions import RequestException

# 获取一页的页面


def get_one_page(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.67 Safari/537.36"
    }
    try:
        res = requests.get(url, headers=headers)
        if res.status_code == 200:
            return res.text
        return None
    except RequestException as e:
        return None


# 1获取排名序号
#  <dd>.*?board-index.*?>(.*?)</i>
# 2图片链接
# <dd>.*?board-index.*?>(.*?)</i>.*?data-src="(.*?)"
# 3电影名称、主演、上映时间、评分
# <dd>.*?board-index.*?>(.*?)</i>.*?data-src="(.*?)".*?name.*?a.*?>(.*?)</a>.*?star.*?>(.*?)</p>.*?releasetime.*?>(.*?)</p>.*?integer.*?>(.*?)</i>.*?fraction.*?>(.*?)</i>.*?</dd>
# 处理页面数据
def parse_one_page(html):
    pattern = re.compile(
        '<dd>.*?board-index.*?>(.*?)</i>.*?data-src="(.*?)".*?name.*?a.*?>(.*?)</a>.*?star.*?>(.*?)</p>.*?releasetime.*?>(.*?)</p>.*?integer.*?>(.*?)</i>.*?fraction.*?>(.*?)</i>.*?</dd>',
        re.S)
    items = re.findall(pattern, html)
    for item in items:
        yield {
            'index': item[0],
            'image': item[1],
            'title': item[2].strip(),
            'actor': item[3].strip()[3:],
            'time': item[4].strip()[5:],
            'score': item[5].strip() + item[6].strip()
        }


# 写入文件中
def write_to_file(content):
    with open("./result.txt", "a", encoding="utf-8") as f:
        f.write(json.dumps(content, ensure_ascii=False) + "\n")


def main(offset):
    url = "http://maoyan.com/board/4?offset=" + str(offset)
    html = get_one_page(url)
    for item in parse_one_page(html):
        print(item)
        write_to_file(item)


if __name__ == '__main__':
    print("爬取start...")
    for i in range(10):
        main(offset=i * 10)
        time.sleep(random.randint(1, 3))
    print("爬取end...")
