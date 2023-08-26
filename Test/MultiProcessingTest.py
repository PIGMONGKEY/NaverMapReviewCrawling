import concurrent.futures
import time
from multiprocessing import Process
import selenium.webdriver.support.wait
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

from concurrent.futures import ThreadPoolExecutor

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import WebDriverException
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from concurrent.futures import ThreadPoolExecutor
import pandas as pd

from pathos.multiprocessing import ProcessPool as Pool

from NaverMapCrawling.Main import *


def func1(driver):
    driver.get("https://www.google.com")
    time.sleep(3)

def func2(driver):
    driver.get("https://www.google.com")
    time.sleep(3)

def func3(driver, page, count):
    driver.get(page)
    time.sleep(3)
    driver.get("https://www.daum.net")
    print(count, "finish")

def test_crawling(driver, search_keyword):
    error_list = []
    place_name = search_keyword[2]
    place_address = search_keyword[1]
    place_number = search_keyword[3]

    try:
        place_split = place_address.split(" ")
        place_gu = place_split[1]
        place_dong = place_split[2]
    except:
        # 지번주소가 없는 곳은 건너뜀
        print(place_name)
        print(" *** 지번주소 없음")
        add_error_list(NO_ADDRESS, error_list)
        write_error(error_list, brand_name=place_name, brand_address=place_address, brand_number=place_number)
        return

    if place_name.find("?") != -1 or place_name.find('"') != -1 or place_name.find("/") != -1 or place_name.find(
            ":") != -1 or place_name.find("<") != -1 or place_name.find(">") != -1 or place_name.find(
        "*") != -1 or place_name.find("|"):
        place_name = place_name.replace("?", "")
        place_name = place_name.replace('"', "")
        place_name = place_name.replace("/", "")
        place_name = place_name.replace(":", "")
        place_name = place_name.replace("<", "")
        place_name = place_name.replace(">", "")
        place_name = place_name.replace("*", "")
        place_name = place_name.replace("|", "")

    print("검색어 :", place_gu, place_dong, place_name, "번호 :", place_number)
    search_url = f"https://map.naver.com/v5/search/{place_gu} {place_dong} {place_name}"

    temp_error_list = []
    for temp in error_list:
        temp_error_list.append(temp)
    # Selenium 을 이용한 페이지 이동을 통해 장소 코드 return
    place_code = get_place_code(driver, search_url, error_list)

    # 크롬 오류로 인해 네이버 지도 메인 화면만 계속 로딩되는 현상을 막기 위하여 예외처리
    while 1:
        if place_code != -1:
            break

        error_list = []
        for temp in temp_error_list:
            error_list.append(temp)

        driver.close()
        driver = driver_init()
        place_code = get_place_code(driver, search_url, error_list)
    print(place_name, driver.current_url)
    # 장소코드가 숫자로 오지 않을 경우 스킵 - 없는 장소임
    if place_code.find("%") != -1:
        print(" *** 없는 장소")
        add_error_list(PLACE_NOT_EXIST, error_list)
        write_error(error_list, brand_name=place_name, brand_address=place_address, brand_number=place_number)
        return

    # 장소 코드를 통하여 장소 naver place 리뷰 페이지로 이동
    if move_to_review_page(driver, place_code, place_name, error_list) == -1:
        write_error(error_list, brand_name=place_name, brand_address=place_address, brand_number=place_number)
        return

    # 리뷰 더보기 버튼 끝까지 클릭
    click_more_button(driver)

    # 모든 리뷰 긁어서 txt 파일로 저장
    review_write(place_gu + " " + place_dong + " " + place_name, place_address, driver, error_list)
    write_error(error_list, brand_name=place_name, brand_address=place_address, brand_number=place_number)


if __name__ == "__main__":
    class Parser():
        def __init__(self):
            self.pool = Pool(processes=8)

        def open_browser(self, site):
            driver = webdriver.Chrome()
            driver.get(site)
            print(site, driver.current_url)
            time.sleep(3)

        def multi_processing(self):
            sites = ["https://www.google.com", "https://www.naver.com", "https://www.google.com", "https://www.naver.com",
                     "https://www.google.com", "https://www.naver.com", "https://www.google.com", "https://www.naver.com",
                     "https://www.google.com", "https://www.naver.com", "https://www.google.com", "https://www.naver.com",
                     "https://www.google.com", "https://www.naver.com", "https://www.google.com", "https://www.naver.com",
                     "https://www.google.com", "https://www.naver.com", "https://www.google.com", "https://www.naver.com",
                     "https://www.google.com", "https://www.naver.com", "https://www.google.com", "https://www.naver.com",
                     "https://www.google.com", "https://www.naver.com", "https://www.google.com", "https://www.naver.com",
                     "https://www.google.com", "https://www.naver.com", "https://www.google.com", "https://www.naver.com",
                     "https://www.google.com", "https://www.naver.com", "https://www.google.com", "https://www.naver.com",
                     "https://www.google.com", "https://www.naver.com", "https://www.google.com", "https://www.naver.com"]
            self.pool.map(self.open_browser, sites)

    parser = Parser()
    parser.multi_processing()


# if __name__ == "__main__":
#
#     caps = DesiredCapabilities.CHROME
#     caps["pageLoadStrategy"] = "none"
#
#     options = webdriver.ChromeOptions()  # 크롬 옵션 객체 생성
#     options.add_argument('headless')  # headless 모드 설정
#     options.add_argument("window-size=1920x1080")  # 화면크기(전체화면)
#     options.add_argument("disable-gpu")
#     options.add_argument("disable-infobars")
#     options.add_argument("--disable-extensions")
#
#     # 속도 향상을 위한 옵션 해제
#     prefs = {'profile.default_content_setting_values': {'cookies': 2, 'images': 2, 'plugins': 2, 'popups': 2,
#                                                         'geolocation': 2, 'notifications': 2,
#                                                         'auto_select_certificate': 2, 'fullscreen': 2, 'mouselock': 2,
#                                                         'mixed_script': 2, 'media_stream': 2, 'media_stream_mic': 2,
#                                                         'media_stream_camera': 2, 'protocol_handlers': 2,
#                                                         'ppapi_broker': 2, 'automatic_downloads': 2, 'midi_sysex': 2,
#                                                         'push_messaging': 2, 'ssl_cert_decisions': 2,
#                                                         'metro_switch_to_desktop': 2, 'protected_media_identifier': 2,
#                                                         'app_banner': 2, 'site_engagement': 2, 'durable_storage': 2}}
#     options.add_experimental_option('prefs', prefs)
#
#     driver = webdriver.Chrome(options=options)
#     # csv_file_path = f"/Users/pigmong0202/Downloads/서울시_공공데이터/일반음식점.csv"       # macOS version
#     csv_file_path = f"../CSV/일반음식점.csv"  # windows version
#
#     # 장소 리스트 가져오기 shape = ['영업코드', '지번주소', '상호명', '번호']
#     place_name_list = load_csv(csv_file_path)
#
#     with ThreadPoolExecutor() as executor:
#         futures = []
#
#         for search_keyword in place_name_list:
#             futures.append(executor.submit(test_crawling, driver, search_keyword))


# if __name__ == "__main__":
#     driver = webdriver.Chrome()
#
#     page_list = ["https://www.google.com", "https://www.naver.com", "https://www.google.com", "https://www.naver.com",
#                  "https://www.google.com", "https://www.naver.com", "https://www.google.com", "https://www.naver.com",
#                  "https://www.google.com", "https://www.naver.com", "https://www.google.com", "https://www.naver.com",
#                  "https://www.google.com", "https://www.naver.com", "https://www.google.com", "https://www.naver.com",
#                  "https://www.google.com", "https://www.naver.com", "https://www.google.com", "https://www.naver.com",
#                  "https://www.google.com", "https://www.naver.com", "https://www.google.com", "https://www.naver.com",
#                  "https://www.google.com", "https://www.naver.com", "https://www.google.com", "https://www.naver.com",
#                  "https://www.google.com", "https://www.naver.com", "https://www.google.com", "https://www.naver.com",
#                  "https://www.google.com", "https://www.naver.com", "https://www.google.com", "https://www.naver.com",
#                  "https://www.google.com", "https://www.naver.com", "https://www.google.com", "https://www.naver.com", ]
#
#     result = []
#
#     with ThreadPoolExecutor() as executor:
#         works = []
#         count = 0
#         for page in page_list:
#             count += 1
#             works.append(executor.submit(func3, driver, page, count))
#
#         for work in concurrent.futures.as_completed(works):
#             result.append(work.result())
#
#     driver.close()
#
#     print(result)
