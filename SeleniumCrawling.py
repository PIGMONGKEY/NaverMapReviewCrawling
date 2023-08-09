from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.ie.options import Options
import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://pcmap.place.naver.com/restaurant/1231684190/review/visitor?entry=bmp&from=map&fromPanelNum="
           "1&ts=1691500494146")

time.sleep(5)

driver.close()
