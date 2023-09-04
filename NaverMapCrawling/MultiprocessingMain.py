# from multiprocessing import Pool as Pool
import time

from pathos.multiprocessing import ProcessPool as Pool

from NaverMapCrawling.GetBrandNameFromCSV import *
from NaverMapCrawling.PageAutomation import *
from NaverMapCrawling.WriteReviewOnFile import *


def crawling_multiprocessing(search_keywords):
    start_point_place_name_list = [493577]
    start_code = False
    driver = webdriver.Chrome()

    for search_keyword in search_keywords:

        place_number = search_keyword[3]
        if not start_code:
            if start_point_place_name_list.count(place_number) > 0:
                start_code = True
            else:
                continue

        error_list = []
        place_name = search_keyword[2]
        place_address = search_keyword[1]

        try:
            place_split = place_address.split(" ")
            place_gu = place_split[1]
            place_dong = place_split[2]
        except:
            # 지번주소가 없는 곳은 건너뜀
            print(f"{place_name} *** 지번주소 없음 - 종료")
            add_error_list(NO_ADDRESS, error_list)
            write_error(error_list, brand_name=place_name, brand_number=place_number, brand_address=place_address,
                        review_save_code=False)
            continue

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

            driver.quit()
            driver = driver_init()
            place_code = get_place_code(driver, search_url, error_list)

        # 장소코드가 숫자로 오지 않을 경우 스킵 - 없는 장소임
        if place_code.find("%") != -1:
            print(f"{place_name} *** 없는 장소 - 종료")
            add_error_list(PLACE_NOT_EXIST, error_list)
            write_error(error_list, brand_name=place_name, brand_number=place_number, brand_address=place_address,
                        review_save_code=False)
            continue

        # 장소 코드를 통하여 장소 naver place 리뷰 페이지로 이동
        if move_to_review_page(driver, place_code, place_name, error_list) == -1:
            write_error(error_list, brand_name=place_name, brand_number=place_number, brand_address=place_address,
                        review_save_code=False)
            continue

        # 리뷰 더보기 버튼 끝까지 클릭
        click_more_button(driver)

        # 모든 리뷰 긁어서 txt 파일로 저장
        review_write(place_gu + " " + place_dong + " " + place_name, place_number, place_address, driver, error_list)
        write_error(error_list, brand_name=place_name, brand_number=place_number, brand_address=place_address,
                    review_save_code=True)

    driver.quit()


if __name__ == "__main__":
    cut_1 = []
    cut_2 = []
    cut_3 = []
    cut_4 = []
    cut_5 = []
    cut_6 = []
    cut_7 = []
    cut_8 = []
    search_keywords_list = [cut_1, cut_2, cut_3, cut_4, cut_5, cut_6, cut_7, cut_8]

    # csv_file_path = f"/Users/pigmong0202/Downloads/서울시_공공데이터/일반음식점.csv"       # macOS version
    csv_file_path = f"../CSV/일반음식점.csv"  # windows version

    # 장소 리스트 가져오기 shape = ['영업코드', '지번주소', '상호명', '번호']
    place_name_list = load_csv(csv_file_path)

    count = 0
    list_num = 0
    for data in place_name_list:
        if data[0] == 1:
            if count >= (place_name_list.__len__() / 8):
                if list_num < 8:
                    count = 0
                    list_num += 1
            count += 1
            search_keywords_list[list_num].append(data)

    # pool = Pool(processes=8)
    # pool.map(crawling_multiprocessing, search_keywords_list)

    crawling_multiprocessing(search_keywords_list[7])
