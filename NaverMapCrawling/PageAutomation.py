import selenium.webdriver.support.wait
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from difflib import SequenceMatcher
import time
import os
from NaverMapCrawling.WriteReviewOnFile import *


# 설치된 크롬 드라이버를 불러온 후 리턴
def driver_init():
    # driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))       # macOS
    driver = webdriver.Chrome()
    driver.maximize_window()
    return driver


# Selenium이 작동할 창 변경(iframe, 등)
def change_frame(driver, frame_id):
    driver.switch_to.default_content()
    driver.switch_to.frame(frame_id)


# 네이버 지도에서 검색어로 검색 후 첫 번째 검색 결과로 진입하여 장소 코드 추출, 리턴
def get_place_code(driver, search_url, error_list):
    one_result_click_js = 'document.querySelector("#_pcmap_list_scroll_container > ul > li > div.CHC5F > a ' \
                          '> div").click()'

    many_result_click_js = 'document.querySelector("#_pcmap_list_scroll_container > ul > li:nth-child(1) > ' \
                           'div.qbGlu > div > a:nth-child(1) > div").click()'

    # 검색 결과 iframe으로 시점 변경

    wait = WebDriverWait(driver, 3)

    # 페이지 열기
    driver.get(search_url)

    # 크롬 오류로 인해 네이버지도 메인화면이 무한 로딩되는 현상 방지
    if driver.current_url.find("search") == -1:
        return -1

    try:
        # searchIframe으로 변경 가능할 때까지 대기
        wait.until(EC.frame_to_be_available_and_switch_to_it((By.ID, "searchIframe")))
        change_frame(driver, "searchIframe")
    except:
        print(" *** searchIframe 진입 실패")
        add_error_list(FAIL_SEARCH_IFRAME, error_list)

    time.sleep(1)

    # 클릭 javascript 실행
    try:
        try:
            driver.execute_script(one_result_click_js)
        except:
            driver.execute_script(many_result_click_js)
    except:
        return driver.current_url.split("/")[-1].split("?")[0]

    driver.switch_to.default_content()
    time.sleep(3)

    try:
        # entryIfrmae으로 변경 가능할 때까지 대기
        wait.until(EC.frame_to_be_available_and_switch_to_it((By.ID, "entryIframe")))
        change_frame(driver, "entryIframe")
    except:
        print(" *** entryIframe 진입 실패")
        add_error_list(FAIL_ENTRY_IFRAME, error_list)

    return driver.current_url.split("/")[-1].split("?")[0]


# 장소 코드를 이용해서 장소 naver place 리뷰 페이지로 이동
def move_to_review_page(driver, place_code, place_name, error_list):
    place_url = f"https://pcmap.place.naver.com/restaurant/{place_code}/review/visitor"

    driver.get(place_url)

    driver.switch_to.default_content()


    try:
        title = driver.find_element(By.CSS_SELECTOR, "#_title > span.Fc1rA")
        ratio = SequenceMatcher(None, title.text, place_name).ratio() * 100
        if ratio < 39.0:
            print(" *** 다른장소-일치율 :", ratio)
            add_error_list(WRONG_PLACE, error_list)
            return -1
    except:
        print(" *** 없는장소")
        add_error_list(NAVER_PLACE_NOT_LOADED, error_list)
        return -1


# 더보기 버튼을 끝까지 누름
def click_more_button(driver):
    more_button_css = "a.fvwqf"

    wait = WebDriverWait(driver, 10)

    count = 0

    while 1:
        # 최대 100번까지 누름
        if count >= 100:
            break

        count += 1

        try:
            # 더보기 버튼이 누를 수 있을 때까지 기다린다.
            wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, more_button_css)))
            # 더보기 버튼 찾기
            more_button = driver.find_element(By.CSS_SELECTOR, more_button_css)
            # 더보기 버튼 클릭
            more_button.click()
        except:
            break

############################################## 테스트 ###################################################################


if __name__ == "__main__":
    one_result_click_js = 'document.querySelector("#_pcmap_list_scroll_container > ul > li > div.CHC5F > a ' \
                          '> div").click()'

    many_result_click_js = 'document.querySelector("#_pcmap_list_scroll_container > ul > li:nth-child(1) > ' \
                           'div.qbGlu > div > a:nth-child(1) > div").click()'

    driver = driver_init()
    driver.get(f"https://map.naver.com/v5/search/스시노칸도")

    wait = WebDriverWait(driver, 5)
    try:
        wait.until(EC.frame_to_be_available_and_switch_to_it((By.ID, "searchIframe")))
        change_frame(driver, "searchIframe")
    except:
        print("searchIframe failed")

    try:
        try:
            driver.execute_script(one_result_click_js)
        except:
            driver.execute_script(many_result_click_js)
    except:
        print("no javascript")

    time.sleep(2)

    driver.switch_to.default_content()

    try:
        wait.until(EC.frame_to_be_available_and_switch_to_it((By.ID, "entryIframe")))
        change_frame(driver, "entryIframe")
    except:
        print("entryIframe failed")

    time.sleep(20)

    driver.close()
