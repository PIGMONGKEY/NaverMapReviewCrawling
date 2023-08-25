import pandas as pd


def load_csv(file):
    try:
        csv_data = pd.read_csv(file, encoding="cp949", low_memory=False)
    except:
        csv_data = pd.read_csv(file, low_memory=False)

    open_place_list = []

    for temp in csv_data.values.tolist():
        if temp[4] == 1:
            open_place_list.append(temp)
    return open_place_list


############################################## 테스트 ###################################################################


if __name__ == "__main__":
    # csv = pd.read_csv(f"/Users/pigmong0202/Downloads/서울시_공공데이터/일반음식점.csv", low_memory=False)      # macOS version
    csv = pd.read_csv(f"../CSV/일반음식점.csv", encoding="cp949", low_memory=False)                           # windows version
    datas = csv.values.tolist()
    # print(datas)

    count = 0
    for data in datas:
        count += 1
        if data[4] == 1:
            print(data[15], data[18])
            try:
                split_path = data[15].split(" ")
                print(split_path[1], split_path[2])
            except:
                print("주소 정보 없음")

    print("count :", count)
