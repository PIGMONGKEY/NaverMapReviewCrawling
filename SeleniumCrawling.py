from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.ie.options import Options
import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://pcmap.place.naver.com/restaurant/1231684190/home?entry=bmp&from=map&fromPanelNum=1&ts=1691500494146")

time.sleep(5)

review_button = driver.find_element(By.XPATH, "/html/body/div[3]/div/div/div/div[5]/div/div/div/div/a[4]/span")
review_button.click()
time.sleep(1)

more_button = driver.find_element(By.XPATH, "/html/body/div[3]/div/div/div/div[7]/div[3]/div[3]/div[2]/a")
more_button.click()

time.sleep(50)

