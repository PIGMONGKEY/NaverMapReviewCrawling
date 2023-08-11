from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

from NaverMapCrawling.FileIO import *
from NaverMapCrawling.PageAutomation import *

search_keyword = "의정부 미술도서관"
search_url = f"https://map.naver.com/v5/search/{search_keyword}/place"

driver = driver_init()
place_code = get_place_code(driver, search_url)
move_to_review_page(driver, place_code)

driver.switch_to.default_content()

click_more_button(driver)

review_write(search_keyword, driver)

driver.close()
