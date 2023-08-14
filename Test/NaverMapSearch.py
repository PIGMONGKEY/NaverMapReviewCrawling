from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

from NaverMapCrawling.WriteReviewOnFile import *
from NaverMapCrawling.PageAutomation import *
from NaverMapCrawling.GetBrandNameFromCSV import *

if __name__ == '__main__':

    place_name = load_csv("../CSV/경기도 의정부시_착한가격업소 현황_20230101.csv")

    for search_keyword in place_name:
        search_url = f"https://map.naver.com/v5/search/의정부 {search_keyword}/place"

        # Chrome Driver Setting
        driver = driver_init()

        # Selenium 을 이용한 페이지 이동을 통해 장소 코드 return
        place_code = get_place_code(driver, search_url)

        # 장소 코드를 통하여 장소 naver place 리뷰 페이지로 이동
        move_to_review_page(driver, place_code)

        driver.switch_to.default_content()

        # 리뷰 더보기 버튼 끝까지 클릭
        click_more_button(driver)

        # 모든 리뷰 긁어서 txt 파일로 저장
        review_write(search_keyword, driver)

        driver.close()
