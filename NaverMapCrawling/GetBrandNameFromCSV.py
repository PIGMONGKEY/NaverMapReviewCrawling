import pandas as pd


def load_csv(file):
    try:
        data = pd.read_csv(file, encoding="cp949", low_memory=False)
    except:
        data = pd.read_csv(file, low_memory=False)

    list = []

    for temp in data.values.tolist():
        if temp[4] == 1:
            list.append(temp)
    return list


if __name__ == "__main__":
    csv = pd.read_csv(f"/Users/pigmong0202/Downloads/서울시_공공데이터/일반음식점.csv", low_memory=False)
    datas = csv.values.tolist()
    for data in datas:
        if data[4] == 1:
            print(data[18])
