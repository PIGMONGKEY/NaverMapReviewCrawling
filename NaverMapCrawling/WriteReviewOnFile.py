from selenium.webdriver.common.by import By
import os


# 검색어 명으로 파일 생성
def open_file(brand_name):
    if brand_name.find("?") != -1 or brand_name.find('"') != -1 or brand_name.find("/") != -1 or brand_name.find(":") != -1 or brand_name.find("<") != -1 or brand_name.find(">") != -1 or brand_name.find("*") != -1 or brand_name.find("|"):
        brand_name = brand_name.replace("?", "")
        brand_name = brand_name.replace('"', "")
        brand_name = brand_name.replace("/", "")
        brand_name = brand_name.replace(":", "")
        brand_name = brand_name.replace("<", "")
        brand_name = brand_name.replace(">", "")
        brand_name = brand_name.replace("*", "")
        brand_name = brand_name.replace("|", "")

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
def review_write(brand_name, place_address, driver):
    file = open_file(brand_name)

    file.write(brand_name + "\n")
    file.write(place_address + "\n\n")

    count = 0

    review = ""

    try:
        try:
            review = driver.find_elements(By.CSS_SELECTOR, "span.zPfVt")
        except:
            for i in range(10):
                review = driver.find_elements(By.CSS_SELECTOR, "span.zPfVt")
    except:
        print("span 에러가 발생했습니다.")
        temp_file = open(f"../Reviews/서울특별시/오류장소목록.txt", "a", encoding="UTF-8")
        temp_file.write(brand_name + "\n")
        close_file(temp_file)
        return

    for s in review:
        if s.text.__len__() >= 5:
            write_file(file, s.text)
            count += 1

    if count == 0:
        print("리뷰가 없거나, 장소가 없습니다.")
        temp_file = open(f"../Reviews/서울특별시/오류장소목록.txt", "a", encoding="UTF-8")
        temp_file.write(brand_name + "\n")
        close_file(temp_file)

    close_file(file)


############################################## 테스트 ###################################################################


if __name__ == "__main__":
    try:
        os.mkdir("../Reviews/서울특별시/일반음식점")
    except:
        print("Directory is already exist")

    file_name = "?abcdefg?"
    if file_name.find("?") != -1:
        print(file_name.find("?"))
        file_name = file_name.replace("!", "")
        print(file_name)

    f = open("../Reviews/서울특별시/일반음식점/test().txt", "a")
    f.close()
