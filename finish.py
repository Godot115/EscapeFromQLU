# -*- coding: utf-8 -*-
# @Time    : 2/21/23 22:44
# @Author  : godot
# @FileName: finish.py
# @Project : escapeFromQLU
# @Software: PyCharm
import datetime
import random
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.select import Select
from settings import *

user_agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36"
language = "zh-CN"
options = Options()
# options.add_argument('--headless')
# options.add_argument('--disable-gpu')
options.add_argument(f'user-agent={user_agent}')
options.add_argument(f'lang={language}')
options.add_argument("disable-blink-features=AutomationControlled")
driver = webdriver.Chrome(chrome_options=options)  # Chrome浏览器

# login qlu os
driver.get("http://os.qlu.edu.cn/")
sleep(10)
driver.find_element(by=By.NAME, value="username").send_keys(stu_no)
elems = driver.find_elements(by=By.TAG_NAME, value="input")
elems = list(filter(lambda x: x.get_attribute("type") == "password", elems))
password_elem = elems[0]
password_elem.send_keys(os_password)
driver.find_element(by=By.TAG_NAME, value="button").click()

driver.get("https://os.qlu.edu.cn/taskcenter/workflow/todo")

finishBtn1 = driver.find_element(by=By.CLASS_NAME, value="but_style1")
finishBtn1.click()
sleep(5)
handles = driver.window_handles
driver.switch_to.window(handles[1])
sleep(5)
finishBtn2 = driver.find_element(by=By.XPATH, value="/html/body/div[7]/ul/li[1]/a")
finishBtn2.click()
sleep(3)
elem = driver.find_element(by=By.CSS_SELECTOR, value="button.dialog_button.default.fr")
elem.click()
driver.close()
driver.switch_to.window(handles[0])