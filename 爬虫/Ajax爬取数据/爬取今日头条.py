import requests
import os
from urllib.parse import urlencode
from hashlib import md5
from multiprocessing.pool import Pool

headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.67 Safari/537.36"
}


def get_page(offset):
    params = {
        "offset": offset,
        "format": "json",
        "keyword": "街拍",
        "autoload": "true",
        "count": 20,
        "cur_tab": 1,
        "from": "search_tab"

    }
    url = "http://www.toutiao.com/search_content/?" + urlencode(params)
    try:
        res = requests.get(url, headers=headers)
        if res.status_code == 200:
            return res.json()
    except requests.ConnectionError as e:
        return None


def get_images(json):
    if json.get("data"):
        for item in json.get("data"):
            title = item.get("title")
            if item.get("image_list"):
                images = item.get("image_list")
                for image in images:
                    yield {
                        "image": image.get("url"),
                        "title": title
                    }

# 保存图片


def save_image(item):
    if not os.path.exists(item.get("image")):
        os.mkdir(item.get("title"))
    try:
        res = requests.get(item.get("image"))
        if res.status_code == 200:
            # file_path = "{0}/{1}.{2}".format(item.get("title"), md5(res.content).hexdigest(), "jpg")
            file_path = '{0}/{1}.{2}'.format(item.get('title'), md5(res.content).hexdigest(), 'jpg')
            if not os.path.exists(file_path):
                with open(file_path, "wb") as f:
                    f.write(res.content)
        else:
            print("Already Downloaded", file_path)
    except requests.ConnectionError as e:
        print("Failed to save Image")


def main(offset):
    json = get_page(offset)
    for item in get_images(json):
        print(item)
        save_image(item)


GROUP_START = 1
GROUP_END = 20

if __name__ == '__main__':
    pool = Pool()
    groups = ([x * 20 for x in range(GROUP_START, GROUP_END + 1)])
    pool.map(main, groups)
    pool.close()
    pool.join()
