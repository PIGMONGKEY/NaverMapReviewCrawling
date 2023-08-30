import pandas as pd


def load_csv(file):
    #스킵할 행 수 - 오류로 인해 프로그램이 멈출 시, 크롤링을 재개할 인덱스
    skip_rows = 0

    try:
        csv_data = pd.read_csv(file, encoding="cp949", low_memory=False, skiprows=skip_rows)
    except:
        csv_data = pd.read_csv(file, low_memory=False, skiprows=skip_rows)

    open_place_list = []

    for temp in csv_data.iloc[:, [4, 15, 18, 44]].values.tolist():
        # 영업코드가 1 인 경우(영업중인 경우)만 리스트에 장소, 주소, 번호 추가
        if temp[0] == 1:
            open_place_list.append(temp)

    return open_place_list


############################################## 테스트 ###################################################################


if __name__ == "__main__":
    # csv = pd.read_csv(f"/Users/pigmong0202/Downloads/서울시_공공데이터/일반음식점.csv", low_memory=False)      # macOS version
    # csv = pd.read_csv(f"../CSV/일반음식점.csv", encoding="cp949", low_memory=False)          # windows version
    # csv = csv.iloc[:, [4, 15, 18, 44]]
    # datas = csv.values.tolist()
    # # print(datas[0])
    #
    # count = 0
    # for data in datas:
    #     if data[0] == 1:
    #         count += 1
    #         print(data[1], data[2], data[3])
    #         # try:
    #         #     split_path = data[1].split(" ")
    #         #     print(split_path[1], split_path[2])
    #         # except:
    #         #     print("주소 정보 없음")
    #
    # print("count :", count)

    list = load_csv(f"../CSV/일반음식점.csv")
    cut_1 = []
    cut_2 = []
    cut_3 = []
    cut_4 = []
    cut_5 = []
    cut_6 = []
    cut_7 = []
    cut_8 = []
    cut_list = [cut_1, cut_2, cut_3, cut_4, cut_5, cut_6, cut_7, cut_8]
    count = 0
    list_num = 0

    for data in list:
        if data[0] == 1:
            if count >= (list.__len__() / 8):
                if list_num < 8:
                    count = 0
                    list_num += 1
            count += 1
            cut_list[list_num].append(data)

    for temp in cut_list:
        print(temp)

