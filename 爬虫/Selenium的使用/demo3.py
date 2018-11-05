from selenium import webdriver
import time

brower = webdriver.Chrome()
brower.get("https://www.taobao.com")
input = brower.find_element_by_id("q")
input.send_keys("Iphone7")
time.sleep(5)
input.clear()
input.send_keys("小米")
button = brower.find_element_by_class_name("btn-search")
button.click()
