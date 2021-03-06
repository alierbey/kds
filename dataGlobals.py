print("data Globals")

import pandas as pd
import numpy as np


df = pd.read_excel("veri1.xlsx")

# df['Tarih']=df['Tarih'].dt.year
# df_tarih = df.groupby('Tarih')


df_manipule = df
df_manipule_tarih = df.groupby('Tarih')

# def reset():
#     # df = pd.read_excel("veri1.xlsx")
#     # df['Tarih']=df['Tarih'].dt.year
#     # df_tarih = df.groupby('Tarih')

# reset()

def veriEdit(gelenDergerler):
    df['Tuketim'] = df['Tuketim'] * gelenDergerler[0]
    df['GSD'] = df['GSD'] * gelenDergerler[1]
    df['GSTL'] = df['GSTL'] * gelenDergerler[2]
    df['Nufus'] = df['Nufus'] * gelenDergerler[3]
    df['SUE'] = df['SUE'] * gelenDergerler[4]
    print(df['Tuketim'])

def getDataWithYear(yil):

    index = int(yil) -  1980
    print(df_manipule.iloc[[index]])
    # print(df_manipule.loc[index,'Tuketim'])
    # print(df_manipule.loc[index,'GSD'])
    verim = []
    verim.append(df_manipule.loc[index,'Tuketim'])
    verim.append(df_manipule.loc[index,'GSD'])
    verim.append(df_manipule.loc[index,'GSTL'])
    verim.append(df_manipule.loc[index,'Nufus'])
    verim.append(df_manipule.loc[index,'SUE'])

    return verim




def reset_manipule():
    df = pd.read_excel("veri1.xlsx")
    df['Tarih']=df['Tarih'].dt.year
    df_tarih = df.groupby('Tarih')
    global df_manipule
    df_manipule =  df
    global df_manipule_tarih
    df_manipule_tarih =  df.groupby('Tarih')
    print("----> veriler resetlendi")


# w_son global değişkeni decision sayfasındaki seçime bağlı olarak değişmektedir.
w_son = np.array([0.1, 0.05, 0.15, 0.25, 0.05, 0.25, 0.1])
wi = 1/14
w_ham = np.array([wi, wi, wi, wi, wi, wi, wi, wi, wi, wi, wi, wi, wi, wi])

seciliTarih = 2021

goalSeekingVeri1 = 0.436
goalSeekingVeri2 = 0.4
goalSeekingVeri3 = 0.75


tuketim_d = 0
gsd_d = 0
gstl_d = 0
nufus_d = 0
sue_d = 0