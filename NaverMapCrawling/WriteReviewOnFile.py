from selenium.webdriver.common.by import By
import os


# 검색어 명으로 파일 생성
def open_file(brand_name):
    return open(f"../Reviews/서울특별시/일반음식점/{brand_name}.txt", "w", encoding="UTF-8")


# 리뷰를 txt 파일에 작성
def write_file(file, review):
    try:
        file.write(review + "\n\n")
    except:
        return


# 파일 닫기
def close_file(file):
    file.close()


# 모든 리뷰를 불러와서 파일에 작성
def review_write(brand_name, driver):
    file = open_file(brand_name)

    count = 0
    for s in driver.find_elements(By.CSS_SELECTOR, "span.zPfVt"):
        if s.text.__len__() >= 5:
            write_file(file, s.text)
            count += 1

    if count == 0:
        print("리뷰가 없거나, 장소가 없습니다.")
        temp_file = open_file("오류장소목록")
        temp_file.write(brand_name + "\n")
        close_file(temp_file)

    close_file(file)


############################################## 테스트 ###################################################################


if __name__ == "__main__":
    try:
        os.mkdir("../Reviews/서울특별시/일반음식점")
    except:
        print("Directory is already exist")

    f = open("../Reviews/서울특별시/일반음식점/test.txt", "w")
    f.close()
