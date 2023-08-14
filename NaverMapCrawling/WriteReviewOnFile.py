from selenium.webdriver.common.by import By


# 검색어 명으로 파일 생성
def open_file(brand_name):
    return open(f"../Reviews/서울특별시/호텔/{brand_name}.txt", "w")


# 리뷰를 txt 파일에 작성
def write_file(file, review):
    file.write(review + "\n\n")


# 파일 닫기
def close_file(file):
    file.close()


# 모든 리뷰를 불러와서 파일에 작성
def review_write(brand_name, driver):
    file = open_file(brand_name)

    for s in driver.find_elements(By.CSS_SELECTOR, "span.zPfVt"):
        if s.text.__len__() >= 5:
            write_file(file, s.text)

    close_file(file)
