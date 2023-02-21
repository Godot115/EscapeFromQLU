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


sleep(3)
driver.get("https://os.qlu.edu.cn/infoplus/form/XSQJ/start")

sleep(10)
teacher_names = [mentor_name_Pinyin, communist_ideological_assistant_name_Pinyin]
teacher_ranks = [mentor_rank, communist_ideological_assistant_rank]

driver.find_element(by=By.NAME, value="fieldBJ").send_keys(stu_class)
# select mentor and IA
spans = driver.find_elements(by=By.TAG_NAME, value="span")
spans = list(
    filter(lambda x: x.get_attribute("class") == "select2 select2-container select2-container--default", spans))
for idx in range(2):
    span = spans[idx]
    driver.execute_script("arguments[0].scrollIntoView();", span)
    span.click()
    sleep(0.5)
    driver.find_element(by=By.CLASS_NAME, value="select2-search__field").send_keys(teacher_names[idx])
    sleep(5)
    elems = driver.find_element(by=By.CLASS_NAME, value="select2-results__options").find_elements(by=By.XPATH,
                                                                                                  value=".//*")
    elems[teacher_ranks[idx] - 1].click()
    sleep(0.5)

# select campus
campus = driver.find_element(by=By.NAME, value="fieldXQA")
select = Select(campus)
select.select_by_value(campus_id)
sleep(0.5)

# select leave type
leave_type = driver.find_element(by=By.NAME, value="fieldQJLX")
type_selector = Select(leave_type)
type_selector.select_by_value("1")
sleep(0.5)

# basic information
now = datetime.datetime.utcfromtimestamp(datetime.datetime.timestamp(datetime.datetime.now())) + datetime.timedelta(
    hours=8)
date = now.strftime("%Y-%m-%d")
driver.find_element(by=By.NAME, value="fieldRQFrom").send_keys(date)
driver.find_element(by=By.NAME, value="fieldSJFrom").send_keys("05:00")
driver.find_element(by=By.NAME, value="fieldRQTo").send_keys(date)
driver.find_element(by=By.TAG_NAME, value="body").click()
driver.find_element(by=By.NAME, value="fieldSJTo").send_keys(end_times[random.randint(0, len(end_times) - 1)])
driver.find_element(by=By.NAME, value="fieldJKZK").send_keys(health_status)
driver.find_element(by=By.NAME, value="fieldJTLXR").send_keys(family_contact)
driver.find_element(by=By.NAME, value="fieldLXRDH").send_keys(family_contact_phone)
driver.find_element(by=By.NAME, value="fieldQJYY").send_keys(excuses[random.randint(0, len(excuses) - 1)])
driver.find_element(by=By.ID, value="V1_CTRL139").send_keys(
    target_locations[random.randint(0, len(target_locations) - 1)])
driver.find_element(by=By.TAG_NAME, value="body").click()
checkbox = list(filter(lambda x: len(x.text) > 10, driver.find_elements(by=By.TAG_NAME, value="label")))[0]
driver.execute_script("arguments[0].scrollIntoView();", checkbox)
checkbox.click()
sleep(1)
btns = driver.find_elements(by=By.CLASS_NAME, value="command_button_content")
btns = list(filter(lambda x: x.text == "提交", btns))
btns[0].click()
sleep(3)
elem = driver.find_element(by=By.XPATH, value="/html/body/div[9]/div/div[2]/button[1]")
elem.click()
dialog = driver.find_element(by=By.CLASS_NAME, value="dialog_content").text
print(dialog)
