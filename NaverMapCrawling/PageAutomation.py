from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time


def driver_init():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()
    return driver


def change_frame(driver, frame_id):
    driver.switch_to.default_content()
    driver.switch_to.frame(frame_id)


def search_and_move_to_naver_place_page(driver, search_url):
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
