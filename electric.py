#Bu dosyada lstm modeli oluşturulacak şu an hazır sonuçlar kullanılıyor.
from math import sqrt
from numpy import concatenate
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import mean_squared_error
from keras.models import Sequential
from keras.layers import Dense, Dropout, Activation
from keras.layers import LSTM, Bidirectional, GRU
import plotly.offline as py
import matplotlib.pyplot as plt
from pandas import DataFrame
from pandas import concat
from pandas import read_csv
import numpy as np
import pandas as pd
import numpy as np
import keras
import tensorflow as tf
from keras.preprocessing.sequence import TimeseriesGenerator
import plotly.graph_objs as go
from pandas import DataFrame
import dash
import dash_core_components as dcc
import dash_html_components as html
import random


b1 =  56731.23065
b0 = -404968.6117
ss = 975241
son = 5000000
sure = 120
rn = []

l = list(range(sure))
lt = np.array(l)+409

for i in range(sure):
    rn.append(random.randrange(-3,3))

rnn = np.array(rn)

fonk = b0 + b1*lt + rnn *ss + son

fonk = pd.DataFrame(fonk, columns=['Tahmin'])
##--------------------------------------------------------------------------##
# Datayı Yükleyelim
data1 = pd.read_excel('veri_tahminler.xlsx', sheet_name='Sheet2', date_parser=[0])

# #Datetime Haline Getirilmesi
# #data['tarih'] = pd.to_datetime(data.tarih, format='%Y-%m')
# data1['Tarih'] = data1['Tarih'].dt.strftime('%Y-%m')



# #Tarih sütununun index'e Alınması
fonk.index = data1.Tarih

# #Dataframe den istenmeyen sütunlar kaldırıldı
# data1.drop('Tarih', axis=1, inplace=True)
# data1.drop('SUE',axis=1, inplace=True)
# data1.drop('GSD', axis=1, inplace=True)
# data1.drop('GSTL',axis=1, inplace=True)
# data1.drop('Nufus',axis=1, inplace=True)

# tahmin = data1
##--------------------------------------------------------------------------##


ham1 = pd.read_excel('veri_tahminler.xlsx', sheet_name='Sheet1', date_parser=[0])
ham1['Tarih'] = ham1['Tarih'].dt.strftime('%Y-%m')
ham1.index = ham1.Tarih

#Dataframe den istenmeyen sütunlar kaldırıldı
ham1.drop('Tarih', axis=1, inplace=True)
ham1.drop('Periyot', axis=1, inplace=True)
ham1.drop('SUE',axis=1, inplace=True)
ham1.drop('GSD', axis=1, inplace=True)
ham1.drop('GSTL',axis=1, inplace=True)
ham1.drop('Nufus',axis=1, inplace=True)

ham = ham1

trace1 = go.Scatter(
    x = fonk.index,
    y = fonk.Tahmin,
    mode = 'lines',
    name = 'Eğitim Verileri'
)
trace2 = go.Scatter(
    x = ham1.index,
    y = ham1.Tuketim,
    mode = 'lines',
    name = 'Tahmin Verileri'
)
# trace3 = go.Scatter(
#     x = date_test,
#     y = sue_test,
#     mode='lines',
#     name = 'Kontrol Verileri'
# )
# trace4 = go.Scatter(
#     x = forecast_dates,
#     y = forecast,
#     mode='lines',
#     name = 'Tahmin Verileri'
# )
layout = go.Layout(
    title = "Elektrik Tüketim Tahmini",
    xaxis = {'title' : "Tarih"},
    yaxis = {'title' : "MWh"}
)


fig = go.Figure(data=[trace1, trace2], layout=layout)
fig.update_layout({
     "height": 335,
"plot_bgcolor": "rgba(0, 0, 0, 0)",
"paper_bgcolor": "rgba(0, 0, 0, 0)",
})




