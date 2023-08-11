from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

from NaverMapCrawling.FileIO import *
from NaverMapCrawling.PageAutomation import *

search_keyword = "의정부 미술도서관"

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get(f"https://map.naver.com/v5/search/{search_keyword}/place")

time.sleep(2)

change_frame(driver, "searchIframe")

try:
    driver.execute_script('document.querySelector("#_pcmap_list_scroll_container > ul > li > div.CHC5F > a '
                          '> div").click()')
except:
    driver.execute_script('document.querySelector("#_pcmap_list_scroll_container > ul > li:nth-child(1) > '
                          'div.qbGlu > div.ouxiq.icT4K > a:nth-child(1) > div").click()')

time.sleep(3)

change_frame(driver, "entryIframe")

driver.execute_script('document.querySelector("#app-root > div > div > div > div.place_fixed_maintab > div > div > div'
                      ' > div > a:nth-child(3) > span").click()')

place_code = driver.current_url.split("/")[-1].split("?")[0]
place_url = f"https://pcmap.place.naver.com/restaurant/{place_code}/review/visitor"

driver.get(place_url)

time.sleep(3)

driver.switch_to.default_content()

while 1:
    try:
        more_button = driver.find_element(By.CSS_SELECTOR, "a.fvwqf")
        more_button.click()
        time.sleep(1)
    except:
        break

review_write(search_keyword, driver)

driver.close()
