import pandas as pd


def load_csv(file):
    #스킵할 행 수 - 오류로 인해 프로그램이 멈출 시, 크롤링을 재개할 인덱스
    skip_rows = 282

    try:
        csv_data = pd.read_csv(file, encoding="cp949", low_memory=False, skiprows=skip_rows)
    except:
        csv_data = pd.read_csv(file, low_memory=False, skiprows=skip_rows)

    open_place_list = []

    for temp in csv_data.iloc[:, [4, 15, 18]].values.tolist():
        if temp[0] == 1:
            open_place_list.append(temp)

    return open_place_list


############################################## 테스트 ###################################################################


if __name__ == "__main__":
    # csv = pd.read_csv(f"/Users/pigmong0202/Downloads/서울시_공공데이터/일반음식점.csv", low_memory=False)      # macOS version
    csv = pd.read_csv(f"../CSV/일반음식점.csv", encoding="cp949", low_memory=False, skiprows=400000)          # windows version
    csv = csv.iloc[:, [4, 15, 18]]
    datas = csv.values.tolist()
    # print(datas)

    count = 0
    for data in datas:
        count += 1
        if data[0] == 1:
            print(data[1], data[2])
            try:
                split_path = data[1].split(" ")
                print(split_path[1], split_path[2])
            except:
                print("주소 정보 없음")

    print("count :", count)
