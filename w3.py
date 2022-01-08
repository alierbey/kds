#Manuel ağırlık 
# wi sabit değer, w değerleri dışardan alınacak.

import numpy as np
import pandas as pd

wi = 1/14
w = np.array([wi, wi, wi, wi, wi, wi, wi, wi, wi, wi, wi, wi, wi, wi])

data = pd.read_excel('veri2.xlsx', date_parser=[0])


def normalize(data):
    result = data.copy()
    for feature_name in data.columns:
        s_value = data[feature_name].sum()
        result[feature_name] = (data[feature_name]) / (s_value)
    return result

A = normalize(data)
AA = A*w
w_son = AA.sum(axis=1)