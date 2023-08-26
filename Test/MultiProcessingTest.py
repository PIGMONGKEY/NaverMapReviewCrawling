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


def func1(driver):
    driver.get("https://www.google.com")
    time.sleep(3)

def func2(driver):
    driver.get("https://www.google.com")
    time.sleep(3)

def func3(driver, page, count):
    driver.get(page)
    time.sleep(3)
    print(count, "finish")


if __name__ == "__main__":
    driver = webdriver.Chrome()

    page_list = ["https://www.google.com", "https://www.naver.com", "https://www.google.com", "https://www.naver.com",
                 "https://www.google.com", "https://www.naver.com", "https://www.google.com", "https://www.naver.com",
                 "https://www.google.com", "https://www.naver.com", "https://www.google.com", "https://www.naver.com",
                 "https://www.google.com", "https://www.naver.com", "https://www.google.com", "https://www.naver.com",
                 "https://www.google.com", "https://www.naver.com", "https://www.google.com", "https://www.naver.com",
                 "https://www.google.com", "https://www.naver.com", "https://www.google.com", "https://www.naver.com",
                 "https://www.google.com", "https://www.naver.com", "https://www.google.com", "https://www.naver.com",
                 "https://www.google.com", "https://www.naver.com", "https://www.google.com", "https://www.naver.com",
                 "https://www.google.com", "https://www.naver.com", "https://www.google.com", "https://www.naver.com",
                 "https://www.google.com", "https://www.naver.com", "https://www.google.com", "https://www.naver.com", ]

    result = []

    with ThreadPoolExecutor() as executor:
        works = []
        count = 0
        for page in page_list:
            count += 1
            works.append(executor.submit(func3, driver, page, count))

        for work in concurrent.futures.as_completed(works):
            result.append(work.result())

    driver.close()

    print(result)