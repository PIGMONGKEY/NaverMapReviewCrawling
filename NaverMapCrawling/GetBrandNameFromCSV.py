import pandas as pd


def load_csv(file):
    data = pd.read_csv(file, encoding="cp949")
    return data['업소명'].values.tolist()
