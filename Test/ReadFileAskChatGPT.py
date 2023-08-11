import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

file = open("../Reviews/CrawlingTest.txt", "r")

while True:
    temp_string = file.read(5000)
    print(file.read(5000))
    if temp_string == '':
        break
    time.sleep(0.5)
