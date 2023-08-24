# 구동 환경 : 맥북 m1 pro / pycharm / conda python=3.10
# Installed library
#       selenium
#       webdriver-manager
#       pandas
# Chrome Version : 115.0.5790.170(공식 빌드) (arm64)
# Chrome Driver Version : 115.0.5790.170 (arm64)


from NaverMapCrawling.WriteReviewOnFile import *
from NaverMapCrawling.PageAutomation import *
from NaverMapCrawling.GetBrandNameFromCSV import *

if __name__ == '__main__':

    csv_file_path = f"/Users/pigmong0202/Downloads/서울시_공공데이터/일반음식점.csv"

    # Chrome Driver Setting
    driver = driver_init()
    # place_name_list = load_csv("../CSV/서울시 호텔리스트 현황 (한국어).csv")
    place_name_list = load_csv(csv_file_path)

    for search_keyword in place_name_list:
        place_name = search_keyword[18]
        place_address = search_keyword[15]
        try:
            place_gu = search_keyword[15].split(" ")[1]
        except:
            continue
        search_url = f"https://map.naver.com/v5/search/{place_gu} {place_name}/place"

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
        review_write(search_keyword[18], driver)

    driver.close()
