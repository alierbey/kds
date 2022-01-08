print("data Globals")

import pandas as pd


df = pd.read_excel("veri1.xlsx")
df['Tarih']=df['Tarih'].dt.year
df_tarih = df.groupby('Tarih')


df_manipule = df
df_manipule_tarih = df.groupby('Tarih')

def reset():
    df = pd.read_excel("veri1.xlsx")
    df['Tarih']=df['Tarih'].dt.year
    df_tarih = df.groupby('Tarih')

reset()

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
w_son = 0