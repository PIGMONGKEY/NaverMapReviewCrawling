# 구동 환경 : 맥북 m1 pro / pycharm / conda python=3.10
# Installed library
#       selenium : 4.11.2
#       webdriver-manager : 4.0.0
#       pandas : 2.0.3
# Chrome Version : 115.0.5790.170(공식 빌드) (arm64)
# Chrome Driver Version : 115.0.5790.170 (arm64)


from NaverMapCrawling.WriteReviewOnFile import *
from NaverMapCrawling.PageAutomation import *
from NaverMapCrawling.GetBrandNameFromCSV import *

if __name__ == '__main__':

    # csv_file_path = f"/Users/pigmong0202/Downloads/서울시_공공데이터/일반음식점.csv"       # macOS version
    csv_file_path = f"../CSV/일반음식점.csv"                                              # windows version

    # Chrome Driver Setting
    driver = driver_init()
    place_name_list = load_csv(csv_file_path)

    for search_keyword in place_name_list:
        place_name = search_keyword[2]
        place_address = search_keyword[1]

        try:
            place_split = place_address.split(" ")
            place_gu = place_split[1]
            place_dong = place_split[2]
        except:
            print(place_name, ": 지번 주소 없음")
            continue

        print("검색어 :", place_gu, place_dong, place_name)
        search_url = f"https://map.naver.com/v5/search/{place_gu} {place_dong} {place_name}"

        # Selenium 을 이용한 페이지 이동을 통해 장소 코드 return
        place_code = get_place_code(driver, search_url)
        if not place_code:
            continue

        # 장소 코드를 통하여 장소 naver place 리뷰 페이지로 이동
        move_to_review_page(driver, place_code)

        driver.switch_to.default_content()

        # 리뷰 더보기 버튼 끝까지 클릭
        click_more_button(driver)

        # 모든 리뷰 긁어서 txt 파일로 저장
        review_write(place_gu + " " + place_dong + " " + place_name, driver)
    driver.close()
