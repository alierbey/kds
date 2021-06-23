import pandas as pd
import numpy as np
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.graph_objects as go
import plotly.express as px
import plotly.io as pio
from plotly.subplots import make_subplots
from scipy import stats
import scipy as sp
import random
import style
##################  PREDICTIVE #####################


import keras
import tensorflow as tf
from keras.preprocessing.sequence import TimeseriesGenerator
df = pd.read_excel('veri1.xlsx', date_parser=[0])
df['Tarih'] = df['Tarih'].dt.strftime('%Y-%m')
df['Tarih'] = pd.to_datetime(df['Tarih'])
df.set_axis(df['Tarih'], inplace=True)

#Tarih sütununun index'e Alınması
df.index = df.Tarih

# df.drop(columns=['Periyot', 'Tuketim', 'Nufus', 
#                   'GSD', 'GSTL', 'GSDp', 'GSTLp', 'kbTuketim'], inplace=True)

sue_data = df['SUE'].values
sue_data = sue_data.reshape((-1,1))

split_percent = 0.80
split = int(split_percent*len(sue_data))

sue_train = sue_data[:split]
sue_test = sue_data[split:]

date_train = df['Tarih'][:split]
date_test = df['Tarih'][split:]

print(len(sue_train))
print(len(sue_test))

look_back = 11

train_generator = TimeseriesGenerator(sue_train, sue_train, length=look_back, batch_size=32)     
test_generator = TimeseriesGenerator(sue_test, sue_test, length=look_back, batch_size=1)

from keras.models import Sequential
from keras.layers import LSTM, Dense
model = Sequential()
model.add(
    LSTM(16,
        activation='relu',
        input_shape=(look_back,1))
)

model.add(Dense(1))
model.compile(optimizer='adam', loss='mse')

num_epochs = 50
model.fit_generator(train_generator, epochs=num_epochs, verbose=1)

prediction = model.predict_generator(test_generator)

sue_train = sue_train.reshape((-1))
sue_test = sue_test.reshape((-1))
prediction = prediction.reshape((-1))

sue_data = sue_data.reshape((-1))

def predict(num_prediction, model):
    prediction_list = sue_data[-look_back:]
    
    for _ in range(num_prediction):
        x = prediction_list[-look_back:]
        x = x.reshape((1, look_back, 1))
        out = model.predict(x)[0][0]
        prediction_list = np.append(prediction_list, out)
    prediction_list = prediction_list[look_back-1:]
        
    return prediction_list
    
def predict_dates(num_prediction):
    last_date = df['Tarih'].values[-1]
    prediction_dates = pd.date_range(last_date, periods=num_prediction+1, freq='M').tolist()
    return prediction_dates

num_prediction = 120
forecast = predict(num_prediction, model)
forecast_dates = predict_dates(num_prediction)

trace1 = go.Scatter(
    x = date_train,
    y = sue_train,
    mode = 'lines',
    name = 'Eğitim Verileri'
)
trace2 = go.Scatter(
    x = date_test,
    y = prediction,
    mode = 'lines',
    name = 'Test Verileri'
)
trace3 = go.Scatter(
    x = date_test,
    y = sue_test,
    mode='lines',
    name = 'Kontrol Verileri'
)
trace4 = go.Scatter(
    x = forecast_dates,
    y = forecast,
    mode='lines',
    name = 'Tahmin Verileri'
)
layout = go.Layout(
    title = "Sanayi Üretim Endeksi Tahmini",
    xaxis = {'title' : "Tarih"},
    yaxis = {'title' : "Sanayi Üretim Endeksi"}
)


fig_sue = go.Figure(data=[trace1, trace2, trace3, trace4], layout=layout)
fig_sue.update_layout({
    "font_color":"white",
    "plot_bgcolor": "rgba(0, 0, 0, 0)",
    "paper_bgcolor": "rgba(0, 0, 0, 0)",
})

################# nufus pre #####################################

nufus_data = df['Nufus'].values
nufus_data = nufus_data.reshape((-1,1))

split_percent = 0.80
split = int(split_percent*len(nufus_data))

nufus_train = nufus_data[:split]
nufus_test = nufus_data[split:]

date_train = df['Tarih'][:split]
date_test = df['Tarih'][split:]

print(len(nufus_train))
print(len(nufus_test))

look_back = 3

train_generator = TimeseriesGenerator(nufus_train, nufus_train, length=look_back, batch_size=20)     
test_generator = TimeseriesGenerator(nufus_test, nufus_test, length=look_back, batch_size=1)

from keras.models import Sequential
from keras.layers import LSTM, Dense

model = Sequential()
model.add(
    LSTM(32,
        activation='relu',
        input_shape=(look_back,1))
)

model.add(Dense(1))
model.compile(optimizer='adam', loss='mse')

num_epochs = 50
model.fit_generator(train_generator, epochs=num_epochs, verbose=1)

prediction = model.predict_generator(test_generator)

nufus_train = nufus_train.reshape((-1))
nufus_test = nufus_test.reshape((-1))
prediction = prediction.reshape((-1))




nufus_data = nufus_data.reshape((-1))

def predict(num_prediction, model):
    prediction_list = nufus_data[-look_back:]
    
    for _ in range(num_prediction):
        x = prediction_list[-look_back:]
        x = x.reshape((1, look_back, 1))
        out = model.predict(x)[0][0]
        prediction_list = np.append(prediction_list, out)
    prediction_list = prediction_list[look_back-1:]
        
    return prediction_list
    
def predict_dates(num_prediction):
    last_date = df['Tarih'].values[-1]
    prediction_dates = pd.date_range(last_date, periods=num_prediction+1, freq='M').tolist()
    return prediction_dates

num_prediction = 120
forecast = predict(num_prediction, model)
forecast_dates = predict_dates(num_prediction)

trace1 = go.Scatter(
    x = date_train,
    y = nufus_train,
    mode = 'lines',
    name = 'Eğitim verileri'
)
trace2 = go.Scatter(
    x = date_test,
    y = prediction,
    mode = 'lines',
    name = 'Test verileri'
)
trace3 = go.Scatter(
    x = date_test,
    y = nufus_test,
    mode='lines',
    name = 'Kontrol verileri'
)
trace4 = go.Scatter(
    x = forecast_dates,
    y = forecast,
    mode='lines',
    name = 'Tahmin verileri'
)
layout = go.Layout(
    title = "Nüfus Tahmini",
    xaxis = {'title' : "Tarih"},
    yaxis = {'title' : "Nüfus"}
)


fig_nufus = go.Figure(data=[trace1, trace2, trace3, trace4], layout=layout)
fig_nufus.update_layout({
    
    "font_color":"white",
    "plot_bgcolor": "rgba(0, 0, 0, 0)",
    "paper_bgcolor": "rgba(0, 0, 0, 0)",
})


######################### gsd #####################

gsd_data = df['GSD'].values
gsd_data = gsd_data.reshape((-1,1))

split_percent = 0.80
split = int(split_percent*len(gsd_data))

gsd_train = gsd_data[:split]
gsd_test = gsd_data[split:]

date_train = df['Tarih'][:split]
date_test = df['Tarih'][split:]

print(len(gsd_train))
print(len(gsd_test))

look_back = 6

train_generator = TimeseriesGenerator(gsd_train, gsd_train, length=look_back, batch_size=20)     
test_generator = TimeseriesGenerator(gsd_test, gsd_test, length=look_back, batch_size=1)

from keras.models import Sequential
from keras.layers import LSTM, Dense

model = Sequential()
model.add(
    LSTM(16,
        activation='relu',
        input_shape=(look_back,1))
)

model.add(Dense(1))
model.compile(optimizer='adam', loss='mse')

num_epochs = 50
model.fit_generator(train_generator, epochs=num_epochs, verbose=1)

prediction = model.predict_generator(test_generator)

gsd_train = gsd_train.reshape((-1))
gsd_test = gsd_test.reshape((-1))
prediction = prediction.reshape((-1))



gsd_data = gsd_data.reshape((-1))

def predict(num_prediction, model):
    prediction_list = gsd_data[-look_back:]
    
    for _ in range(num_prediction):
        x = prediction_list[-look_back:]
        x = x.reshape((1, look_back, 1))
        out = model.predict(x)[0][0]
        prediction_list = np.append(prediction_list, out)
    prediction_list = prediction_list[look_back-1:]
        
    return prediction_list
    
def predict_dates(num_prediction):
    last_date = df['Tarih'].values[-1]
    prediction_dates = pd.date_range(last_date, periods=num_prediction+1, freq='M').tolist()
    return prediction_dates

num_prediction = 120
forecast = predict(num_prediction, model)
forecast_dates = predict_dates(num_prediction)

trace1 = go.Scatter(
    x = date_train,
    y = gsd_train,
    mode = 'lines',
    name = 'Eğitim Verileri'
)
trace2 = go.Scatter(
    x = date_test,
    y = prediction,
    mode = 'lines',
    name = 'Test Verileri'
)
trace3 = go.Scatter(
    x = date_test,
    y = gsd_test,
    mode='lines',
    name = 'Kontrol Verileri'
)
trace4 = go.Scatter(
    x = forecast_dates,
    y = forecast,
    mode='lines',
    name = 'Tahmin Verileri'
)
layout = go.Layout(
    title = "GSYH (Dolar Bazlı) Tahmini",
    xaxis = {'title' : "Tarih"},
    yaxis = {'title' : "Gayri Safi Yurtiçi Hasıla (Dolar)"}
)


fig_gsd = go.Figure(data=[trace1, trace2, trace3, trace4], layout=layout)
fig_gsd.update_layout({
    "font_color":"white",
    "plot_bgcolor": "rgba(0, 0, 0, 0)",
    "paper_bgcolor": "rgba(0, 0, 0, 0)",
})


########################### gstl ########################

gstl_data = df['GSTL'].values
gstl_data = gstl_data.reshape((-1,1))

split_percent = 0.80
split = int(split_percent*len(gstl_data))

gstl_train = gstl_data[:split]
gstl_test = gstl_data[split:]

date_train = df['Tarih'][:split]
date_test = df['Tarih'][split:]

print(len(gstl_train))
print(len(gstl_test))

look_back = 6

train_generator = TimeseriesGenerator(gstl_train, gstl_train, length=look_back, batch_size=20)     
test_generator = TimeseriesGenerator(gstl_test, gstl_test, length=look_back, batch_size=1)

from keras.models import Sequential
from keras.layers import LSTM, Dense

model = Sequential()
model.add(
    LSTM(16,
        activation='relu',
        input_shape=(look_back,1))
)

model.add(Dense(1))
model.compile(optimizer='adam', loss='mse')

num_epochs = 50
model.fit_generator(train_generator, epochs=num_epochs, verbose=1)

prediction = model.predict_generator(test_generator)

gstl_train = gstl_train.reshape((-1))
gstl_test = gstl_test.reshape((-1))
prediction = prediction.reshape((-1))


gstl_data = gstl_data.reshape((-1))

def predict(num_prediction, model):
    prediction_list = gstl_data[-look_back:]
    
    for _ in range(num_prediction):
        x = prediction_list[-look_back:]
        x = x.reshape((1, look_back, 1))
        out = model.predict(x)[0][0]
        prediction_list = np.append(prediction_list, out)
    prediction_list = prediction_list[look_back-1:]
        
    return prediction_list
    
def predict_dates(num_prediction):
    last_date = df['Tarih'].values[-1]
    prediction_dates = pd.date_range(last_date, periods=num_prediction+1, freq='M').tolist()
    return prediction_dates

num_prediction = 120
forecast = predict(num_prediction, model)
forecast_dates = predict_dates(num_prediction)

trace1 = go.Scatter(
    x = date_train,
    y = gstl_train,
    mode = 'lines',
    name = 'Eğitim Verileri'
)
trace2 = go.Scatter(
    x = date_test,
    y = prediction,
    mode = 'lines',
    name = 'Test Verileri'
)
trace3 = go.Scatter(
    x = date_test,
    y = gstl_test,
    mode='lines',
    name = 'Kontrol Verileri'
)
trace4 = go.Scatter(
    x = forecast_dates,
    y = forecast,
    mode='lines',
    name = 'Tahmin Verileri'
)
layout = go.Layout(
    title = "GSYH (TL Bazlı) Tahmini",
    xaxis = {'title' : "Tarih"},
    yaxis = {'title' : "Gayri Safi Yurtiçi Hasıla (TL)"}
)


fig_gstl = go.Figure(data=[trace1, trace2, trace3, trace4], layout=layout)
fig_gstl.update_layout({
    "font_color":"white",
    "plot_bgcolor": "rgba(0, 0, 0, 0)",
    "paper_bgcolor": "rgba(0, 0, 0, 0)",
})

################ electric pre ################

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





# #Tarih sütununun index'e Alınması
fonk.index = data1.Tarih




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


layout = go.Layout(
    title = "Elektrik Tüketim Tahmini",
    xaxis = {'title' : "Tarih"},
    yaxis = {'title' : "MWh"}
)


fig_elect = go.Figure(data=[trace1, trace2], layout=layout)
fig_elect.update_layout({
    "font_color":"white",
    "plot_bgcolor": "rgba(0, 0, 0, 0)",
    "paper_bgcolor": "rgba(0, 0, 0, 0)",
})

pagePredictive = html.Div(
    [
        html.H3("Predictive"),
        html.Hr(),
        html.Div([
            html.Div([
                html.Div([
                    html.Div([
                        dcc.Graph(figure=fig_sue)
                    ])
                ],style = {'background-color' : style.cardBackColor['back'],
            'box-shadow': '2px 5px 5px 1px rgba(30, 47, 123, .5)'})            
            ],className="col-xl-6",),
            html.Div([
                html.Div([
                    html.Div([
                        dcc.Graph(figure=fig_nufus)
                    ])
                ],style = {'background-color' : style.cardBackColor['back'],
            'box-shadow': '2px 5px 5px 1px rgba(30, 47, 123, .5)'})            
            ],className="col-xl-6",)
        ],className="row"),
        html.Hr(),
                html.Div([
            html.Div([
                html.Div([
                    html.Div([
                        dcc.Graph(figure=fig_gsd)
                    ])
                ],style = {'background-color' : style.cardBackColor['back'],
            'box-shadow': '2px 5px 5px 1px rgba(30, 47, 123, .5)'})            
            ],className="col-xl-6",),
            html.Div([
                html.Div([
                    html.Div([
                         dcc.Graph(figure=fig_gstl)
                    ])
                ],style = {'background-color' : style.cardBackColor['back'],
            'box-shadow': '2px 5px 5px 1px rgba(30, 47, 123, .5)'})            
            ],className="col-xl-6",)
        ],className="row"),
        html.Hr(),
                html.Div([
            html.Div([
                html.Div([
                    html.Div([
                        dcc.Graph(figure=fig_elect)
                    ])
                ],style = {'background-color' : style.cardBackColor['back'],
            'box-shadow': '2px 5px 5px 1px rgba(30, 47, 123, .5)'})            
            ],className="col-xl-12",),
        ],className="row"),
    ], 
)