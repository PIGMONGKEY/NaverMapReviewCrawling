from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time


def driver_init():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()
    return driver


def change_frame(driver, frame_id):
    driver.switch_to.default_content()
    driver.switch_to.frame(frame_id)


def get_place_code(driver, search_url):
    one_result_click_js = 'document.querySelector("#_pcmap_list_scroll_container > ul > li > div.CHC5F > a ' \
                          '> div").click()'
    many_result_click_js = 'document.querySelector("#_pcmap_list_scroll_container > ul > li:nth-child(1) > ' \
                           'div.qbGlu > div.ouxiq.icT4K > a:nth-child(1) > div").click()'

    driver.get(search_url)
    time.sleep(2)

    change_frame(driver, "searchIframe")
    try:
        driver.execute_script(one_result_click_js)
    except:
        driver.execute_script(many_result_click_js)

    time.sleep(3)

    change_frame(driver, "entryIframe")
    driver.execute_script('document.querySelector("#app-root > div > div > div > div.place_fixed_maintab > div > div'
                          ' > div > div > a:nth-child(3) > span").click()')

    return driver.current_url.split("/")[-1].split("?")[0]


def move_to_review_page(driver, place_code):
    place_url = f"https://pcmap.place.naver.com/restaurant/{place_code}/review/visitor"

    driver.get(place_url)
    time.sleep(3)


def click_more_button(driver):
    more_button_css = "a.fvwqf"

    while 1:
        try:
            more_button = driver.find_element(By.CSS_SELECTOR, more_button_css)
            more_button.click()
            time.sleep(1)
        except:
            break
