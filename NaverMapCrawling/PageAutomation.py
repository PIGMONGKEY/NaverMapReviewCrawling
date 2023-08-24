from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time
import os


# 설치된 크롬 드라이버를 불러온 후 리턴
def driver_init():
    # driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver = webdriver.Chrome()
    driver.maximize_window()
    return driver


# Selenium이 작동할 창 변경(iframe, 등)
def change_frame(driver, frame_id):
    driver.switch_to.default_content()
    driver.switch_to.frame(frame_id)


# 네이버 지도에서 검색어로 검색 후 첫 번째 검색 결과로 진입하여 장소 코드 추출, 리턴
def get_place_code(driver, search_url):
    one_result_click_js = 'document.querySelector("#_pcmap_list_scroll_container > ul > li > div.CHC5F > a ' \
                          '> div").click()'

    many_result_click_js = 'document.querySelector("#_pcmap_list_scroll_container > ul > li:nth-child(1) > ' \
                           'div.qbGlu > div > a:nth-child(1) > div").click()'

    # 검색 결과 iframe으로 시점 변경
    while 1:
        try:
            # 페이지 열기
            driver.get(search_url)
            time.sleep(2)
            change_frame(driver, "searchIframe")
            time.sleep(2)
        except:
            continue
        break

    try:
        try:
            driver.execute_script(one_result_click_js)
        except:
            driver.execute_script(many_result_click_js)
    except:
        return driver.current_url.split("/")[-1].split("?")[0]

    time.sleep(3)

    try:
        change_frame(driver, "entryIframe")
    except:
        print("entryIframe 진입 실패")
    # driver.execute_script('document.querySelector("#app-root > div > div > div > div.place_fixed_maintab > div > div'
    #                       ' > div > div > a:nth-child(3) > span").click()')

    return driver.current_url.split("/")[-1].split("?")[0]


# 장소 코드를 이용해서 장소 naver place 리뷰 페이지로 이동
def move_to_review_page(driver, place_code):
    place_url = f"https://pcmap.place.naver.com/restaurant/{place_code}/review/visitor"

    driver.get(place_url)
    time.sleep(3)


# 더보기 버튼을 끝까지 누름
def click_more_button(driver):
    more_button_css = "a.fvwqf"

    while 1:
        try:
            more_button = driver.find_element(By.CSS_SELECTOR, more_button_css)
            more_button.click()
            time.sleep(1)
        except:
            break


if __name__ == "__main__":
    print(os.getcwd())