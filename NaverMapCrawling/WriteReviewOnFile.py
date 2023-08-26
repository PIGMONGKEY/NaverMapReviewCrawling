from selenium.webdriver.common.by import By
import os


NO_ADDRESS = 10
PLACE_NOT_EXIST = 20
FAIL_SEARCH_IFRAME = 30
FAIL_ENTRY_IFRAME = 40
WRONG_PLACE = 50
NO_REVIEWS = 60
FAIL_SPAN = 70
NAVER_PLACE_NOT_LOADED = 80


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
def review_write(brand_name, place_address, driver, error_list):
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
        print("span 에러가 발생했습니다. - 리뷰항목을 가져오지 못함")
        add_error_list(FAIL_SPAN, error_list)
        return

    for s in review:
        if s.text.__len__() >= 5:
            write_file(file, s.text)
            count += 1

    if count == 0:
        print("리뷰가 없거나, 장소가 없습니다.")
        add_error_list(NO_REVIEWS, error_list)

    close_file(file)


def add_error_list(error_code, error_list):
    error_list.append(error_code)


def write_error(error_list, brand_name, brand_number, brand_address):
    if error_list.__len__() < 1:
        return

    temp_file = open(f"../Reviews/서울특별시/오류장소목록.txt", "a", encoding="UTF-8")

    temp_file.write(brand_name + "||")
    temp_file.write(brand_address + "||")
    temp_file.write(f"{brand_name}")

    error_str = "\t"
    for error_code in error_list:
        if error_code == NO_ADDRESS:
            error_str += " 지번주소없음 "
        elif error_code == PLACE_NOT_EXIST:
            error_str += " 장소없음 "
        elif error_code == FAIL_SEARCH_IFRAME:
            error_str += " searchIframe "
        elif error_code == FAIL_ENTRY_IFRAME:
            error_str += " entryIframe "
        elif error_code == WRONG_PLACE:
            error_str += " 다른장소 "
        elif error_code == FAIL_SPAN:
            error_str += " span "
        elif error_code == NAVER_PLACE_NOT_LOADED:
            error_str += " 네이버플레이스로딩오류 "
        else:
            error_str += " 리뷰또는장소없음 "

    if error_list.count(NO_REVIEWS) == 0:
        error_str += " 리뷰저장됨 "

    temp_file.write(error_str + "\n")

    close_file(temp_file)


############################################## 테스트 ###################################################################


if __name__ == "__main__":
    # try:
    #     os.mkdir("../Reviews/서울특별시/일반음식점")
    # except:
    #     print("Directory is already exist")
    #
    # file_name = "?abcdefg?"
    # if file_name.find("?") != -1:
    #     print(file_name.find("?"))
    #     file_name = file_name.replace("!", "")
    #     print(file_name)
    #
    # f = open("../Reviews/서울특별시/일반음식점/test().txt", "a")
    # f.close()
    def test(a):
        a.append("d")

    l = ["a", "b", "c",]
    t = []
    for asdf in l:
        t.append(asdf)
    test(l)
    l.append(NO_ADDRESS)
    print(l, t)
    print(l.index(10))
    print(l.count(10))
