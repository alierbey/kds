#Swara ağırlık 
# alınan sj değerleri 

import numpy as np
import pandas as pd


#KV'den alınan değerler (ilk değer 0 olarak ayarlanmalı)
sj = np.array([0, 0.1, 0.15, 0.2, 0.25, 0.20, 0.15, 0.1, 0.05, 0.1, 0.2, 0.2, 0.15, 0.25])

kj = 1 + sj
qj = []
t = 1


for i in range(14):
    q = t/kj[i]
    t = q
    qj.append(q)

qj = np.array(qj)
w = qj/qj.sum()

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

