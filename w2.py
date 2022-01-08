#Entropi ağırlık
#Fayda maliyet dönüşümü yapılmazsa,
#entropi dışarıdan veri almadan alternatiflerin ağırlıklarını hesaplar.

import numpy as np
import pandas as pd

data = pd.read_excel('veri2.xlsx', date_parser=[0])

def normalize(data):
    result = data.copy()
    for feature_name in data.columns:
        s_value = data[feature_name].sum()
        result[feature_name] = (data[feature_name]) / (s_value)
    return result

A = normalize(data)
A_v = A.values 

'''ENTROPI Hesapla''' 
for t in A_v:
    A_log = [np.log(i) for i in A_v]
    A_P = A_v*A_log
    entropi = (-1/np.log(7))*sum(A_P)

A_df = 1 - entropi
w = A_df / sum(A_df) 



AA = A*w
w_son = AA.sum(axis=1)