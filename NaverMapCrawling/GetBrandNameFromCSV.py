import pandas as pd


def load_csv(file):
    data = pd.read_csv(file, encoding="cp949")
    return data['명칭'].values.tolist()
