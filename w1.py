#Eşit ağırlık

import numpy as np
import pandas as pd
import dataGlobals as dataGlobals

wi = 1/14
w = np.array([wi, wi, wi, wi, wi, wi, wi, wi, wi, wi, wi, wi, wi, wi])
data = pd.read_excel('veri2.xlsx', date_parser=[0])


def normalize(data):
    result = data.copy()
    for feature_name in data.columns:
        s_value = data[feature_name].sum()
        result[feature_name] = (data[feature_name]) / (s_value)
    return result



def secim1Uygula():
    data1 = np.divide(1,data.iloc[:,0:8])
    data.iloc[:,0:8] = data1.iloc[:,0:8]
    A = normalize(data)
    AA = A*w
    dataGlobals.w_son = AA.sum(axis=1)
    print(dataGlobals.w_son)

def secim2Uygula():
    data1 = np.divide(1,data.iloc[:,0:8])
    data.iloc[:,0:8] = data1.iloc[:,0:8]
    A = normalize(data)
    A_v = A.values 

    for t in A_v:
        A_log = [np.log(i) for i in A_v]
        A_P = A_v*A_log
        entropi = (-1/np.log(7))*sum(A_P)

    A_df = 1 - entropi
    w = A_df / sum(A_df) 
    AA = A*w
    dataGlobals.w_son = AA.sum(axis=1)
    print(dataGlobals.w_son)


def secim3Uygula(w):
    data1 = np.divide(1,data.iloc[:,0:8])
    data.iloc[:,0:8] = data1.iloc[:,0:8]
    A = normalize(data)
    AA = A*w
    dataGlobals.w_son = AA.sum(axis=1)
    print(dataGlobals.w_son)


def secim4Uygula(sj, re):
    data1 = np.divide(1,data.iloc[:,0:8])
    data.iloc[:,0:8] = data1.iloc[:,0:8]
    print("secim4 uygulandı")
    print(type(sj))
    kj = 1 + sj
    qj = []
    t = 1

    for i in range(14):
        q = t/kj[i]
        t = q
        qj.append(q)

    qj = np.array(qj)
    w = qj/qj.sum()
    print("w", w)
    print("re", re)
    son_agirlik = [i for i in range(14)]
    for i in range(14):
         son_agirlik[i] = w[re[i]-1]

    w = np.array(son_agirlik)
    A = normalize(data)
    AA = A*w
    dataGlobals.w_son = AA.sum(axis=1)

    print(dataGlobals.w_son)

         
