from selenium import webdriver
import time

brower = webdriver.Chrome()
brower.get("http://www.baidu.com")
time.sleep(10)
brower.close()
print("停止访问...")
