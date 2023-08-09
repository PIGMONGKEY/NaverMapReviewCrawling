from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.ie.options import Options
from bs4 import BeautifulSoup as bs
import time

try:
    file = open("./CrawlingTest.txt", "w")
except:
    print("There is no such file...")
    exit(-1)

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get(
    "https://pcmap.place.naver.com/restaurant/1231684190/review?"
    "entry=bmp&from=map&fromPanelNum=%22%20%5C%20%221&ts=1691500494146")

time.sleep(5)

# review_button = driver.find_element(By.CSS_SELECTOR, "span.veBoZ")
# review_button.click()
# time.sleep(1)

while 1:
    try:
        more_button = driver.find_element(By.CSS_SELECTOR, "a.fvwqf")
        more_button.click()
        time.sleep(1)
    except:
        break

for s in driver.find_elements(By.CSS_SELECTOR, "span.zPfVt"):
    print(s.text)
    if s.text.__len__() > 20:
        file.write(s.text + "\n\n")

file.close()
driver.close()
