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

pio.templates.default = "plotly_dark"

app = dash.Dash(external_stylesheets=[dbc.themes.DARKLY])

# the style arguments for the sidebar. We use position:fixed and a fixed width
SIDEBAR_STYLE = {
    "position": "fixed",
    "top": 0,
    "left": 0,
    "bottom": 0,
    "width": "16rem",
    "padding": "2rem 1rem",
    "background-color": "#030303",
}

# the styles for the main content position it to the right of the sidebar and
# add some padding.
CONTENT_STYLE = {
    "margin-left": "15rem",
    "margin-right": "2rem",
    "padding": "2rem 1rem",
    "background-color": "#2A1D33",
   
}

colors = {
    'background': '#111111',
    'text': '#7FDBFF'
}

sidebar = html.Div(
    [
        html.H2("KDS", className="display-4"),
        html.Hr(),
        html.P(
            "Karar Destek Sistemleri"
        ),
        dbc.Nav(
            [
                dbc.NavLink("Home", href="/", active="exact"),
                dbc.NavLink("Descriptive", href="/page-1", active="exact"),
                dbc.NavLink("Predictive", href="/page-2", active="exact"),
                dbc.NavLink("Integrative", href="/page-3", active="exact"),
                dbc.NavLink("Prescriptive", href="/page-4", active="exact"),
           
            ],
            vertical=True,
            pills=True,
        ),
    ],
    style=SIDEBAR_STYLE,
)



pageHome = html.Div(
    [
        html.H3("Home"),
              html.Div([
                html.Div([
                    html.Div([],className="card-header",)            
                ],className="col-xl-12",),
              ],className="row"),
        html.Hr(),
    ], 
)





###################  DESCRIPTIVE #####################
df = pd.read_excel("veri1.xlsx")

df['Tarih']=df['Tarih'].dt.year
df_tarih = df.groupby('Tarih')

fig = go.Figure()

pageDescriptive = html.Div(
    [
            html.H3("Descriptive"),
            html.Div([
                html.Div([
                    html.Div([
                            html.H6("Makro Değişkenler ile Tüketim Korelasyonları", style={'text-align': 'center'}),
                               dcc.Dropdown(
                                    id="ticker",
                                    options=[{"label": x, "value": x} 
                                            for x in df.columns[3:]],
                                    value=df.columns[3],
                                    clearable=False,
                                ),
                                dcc.Graph(id="time-series-chart"),
                    ],className="card-header")            
                ],className="col-xl-4"),
                html.Div([
                    html.Div([
                        html.Div([
                            html.H6("Makro Değişkenler", style={'text-align': 'center'}),
                            dcc.Dropdown(id="graf2",
                                options=[{"label": x, "value": x} 
                                            for x in df.columns[2:]],
                                value=df.columns[2],
                                clearable=False,
                                ),
                            dcc.Graph(id="time-series-chart-graf2"),
                        ])
                    ],className="card-header",)            
                ],className="col-xl-8",)
            ],className="row"),
            html.Hr(),
            html.Div([
                html.Div([
                    html.Div([
                                html.Div([
                                    html.H4("Kişibaşı Elektrik Tüketim Raporu", style={'text-align': 'center'}),
                                    dcc.Dropdown(id="slct_year",
                                                options=[{"label": x, "value": x} 
                                                        for x in df_tarih.groups.keys()],
                                                clearable=False,
                                                multi=False,
                                                value=1986,
                                                style={'width': "40%"}
                                                ),

                                    dcc.Graph(id='map')
                                ])
                    ],className="card-header",)            
                ],className="col-xl-7",),
                html.Div([
                    html.Div([
                        html.Div([
                                html.H4("Kişibaşı Elektrik Tüketim Raporu", style={'text-align': 'center'}),
                                html.P("Kategori:"),
                                dcc.Dropdown(
                                    id='slct_cat', 
                                    value='Teknik', 
                                    options=[{'value': x, 'label': x} 
                                            for x in ['Teknik', 'Cevre', 'Ekonomi']],
                                    clearable=False
                                ),
                                html.P("Tür"),
                                dcc.Dropdown(id='slct_tur', value='Uretim'),
                                html.Hr(),
                                dcc.Graph(id="pie-chart",figure=fig),
                            ])
                    ],className="card-header",)            
                ],className="col-xl-5",)
            ],className="row"),
            html.Hr(),
    ], 
)


######### graf 1 #########

@app.callback(
    Output("time-series-chart", "figure"), 
    [Input("ticker", "value")])
def display_time_series(ticker):
    print(ticker)
    #fig = px.line(df, x='Tarih', y=ticker, template="plotly_dark")
    X = np.array(df['Tuketim'])
    y = np.array(df[ticker])
    r = sp.stats.pearsonr(X, y) 
    
    fig = go.Figure(go.Indicator(
    mode = "gauge+number",
    value = r[0],
    domain = {'x': [0, 1], 'y': [0, 1]},
    title = {'text': 'Tüketim & ' + ticker},
    
    gauge = {
        'axis': {'range': [-1, 1], 'tickwidth': 1, 'tickcolor': "darkblue"},
        'bar': {'color': "darkblue"},
        'bgcolor': "white",
        'borderwidth': 2,
        'bordercolor': "gray",
        # 'steps': [
        #     {'range': [-1, 0], 'color': 'gray'},
        #     {'range': [0, r[0]], 'color': 'royalblue'}]
        }))
    return fig
######### graf 4


df2 = pd.read_excel("veri2.xlsx")

df_tur = df2.groupby(['Kategori','Tur'])
#print(df_tur.groups) 

yeap  = {"Teknik": [], "Cevre": [], "Ekonomi":[]}


for kat,tur in df_tur:
    print(kat)
    if kat[0] == 'Teknik':
        yeap["Teknik"].append(kat[1])
    if kat[0] == 'Cevre':
        yeap["Cevre"].append(kat[1])
    if kat[0] == 'Ekonomi':
        yeap["Ekonomi"].append(kat[1])
        #print(kat[1])


###### pie #####


@app.callback(
    Output("time-series-chart2", "figure"), 
    [Input("graf2", "value")])
def display_time_series(graf2):
    #fig = px.line(df, x='Tarih', y=ticker, template="plotly_dark")
    X = np.array(df['Tuketim'])
    y = np.array(df[graf2])
    r = sp.stats.pearsonr(X, y) 

    fig = go.Figure(go.Indicator(
    mode = "number+gauge+delta",
    gauge = {'shape': "bullet"},
    delta = {'reference': 300},
    value = r[0]*100,
    domain = {'x': [0.1, 1], 'y': [0.2, 0.9]},
    title = {'text': "Avg order size"}))
    return fig



@app.callback(
    Output('map', 'figure'),
    [Input('slct_year', 'value')]
)


def display_time_series(slct_year):
    fig = go.Figure(data=[go.Bar(
            x=df_tarih.get_group(slct_year).Periyot, y=df_tarih.get_group(slct_year).kbTuketim,
            textposition='auto'
        )])
    fig.update_traces(marker_color='rgb(158,202,225)', marker_line_color='rgb(8,48,107)',
                  marker_line_width=1.5, opacity=0.6,)
    fig.update_layout(title_text= 'Aylara göre kişibaşı elektrik tüketimi',template="plotly_dark" )
    return fig


@app.callback(
    Output("pie-chart", "figure"), 
    Input('slct_tur', 'value'),
    Input('slct_cat', 'value'),
)
def set_fig(slct_tur,slct_cat):
    print(slct_tur + " " + slct_cat )

    df_cat = df2.groupby('Kategori')
    df_tur = df_cat.get_group(slct_cat)
    df_son = df_tur.groupby('Tur')
    df_filter = df_son.get_group(slct_tur)

    fig = px.pie(df_filter, values='Deger', names='Santral', template="plotly_dark")
    fig.update_layout(title_text= 'Aylara göre kişibaşı elektrik tüketimi' )
    return fig

@app.callback(
    Output("slct_tur", "options"), 
    Input('slct_cat', 'value'),
)
def set_cat(x):
    print("secildi 1")
    return [{'label': i, 'value': i} for i in yeap[x]]

@app.callback(
    Output("time-series-chart-graf2", "figure"), 
    [Input("graf2", "value")])
def display_time_series(graf2):
    fig = px.line(df, x='Tarih', y=graf2, template="plotly_dark")
    return fig





###################  PREDICTIVE #####################

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

# trace1 = go.Scatter(
#     x = date_train,
#     y = sue_train,
#     mode = 'lines',
#     name = 'Data'
# )
# trace2 = go.Scatter(
#     x = date_test,
#     y = prediction,
#     mode = 'lines',
#     name = 'Prediction'
# )
# trace3 = go.Scatter(
#     x = date_test,
#     y = sue_test,
#     mode='lines',
#     name = 'Ground Truth'
# )
# layout = go.Layout(
#     title = "Google Stock",
#     xaxis = {'title' : "Tarih"},
#     yaxis = {'title' : "Sanayi Üretim Endeksi"}
# )

#fig = go.Figure(data=[trace1, trace2, trace3], layout=layout)


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

# trace1 = go.Scatter(
#     x = date_train,
#     y = sue_train,
#     mode = 'lines',
#     name = 'Data'
# )
# trace2 = go.Scatter(
#     x = date_test,
#     y = prediction,
#     mode = 'lines',
#     name = 'Prediction'
# )
# trace3 = go.Scatter(
#     x = date_test,
#     y = sue_test,
#     mode='lines',
#     name = 'Ground Truth'
# )
# layout = go.Layout(
#     title = "Google Stock",
#     xaxis = {'title' : "Tarih"},
#     yaxis = {'title' : "Sanayi Üretim Endeksi"}
# )

#fig = go.Figure(data=[trace1, trace2, trace3], layout=layout)


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

# trace1 = go.Scatter(
#     x = date_train,
#     y = sue_train,
#     mode = 'lines',
#     name = 'Data'
# )
# trace2 = go.Scatter(
#     x = date_test,
#     y = prediction,
#     mode = 'lines',
#     name = 'Prediction'
# )
# trace3 = go.Scatter(
#     x = date_test,
#     y = sue_test,
#     mode='lines',
#     name = 'Ground Truth'
# )
# layout = go.Layout(
#     title = "Google Stock",
#     xaxis = {'title' : "Tarih"},
#     yaxis = {'title' : "Sanayi Üretim Endeksi"}
# )

#fig = go.Figure(data=[trace1, trace2, trace3], layout=layout)


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


fig_elect = go.Figure(data=[trace1, trace2], layout=layout)

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
                ],className="card-header",)            
            ],className="col-xl-6",),
            html.Div([
                html.Div([
                    html.Div([
                        dcc.Graph(figure=fig_nufus)
                    ])
                ],className="card-header",)            
            ],className="col-xl-6",)
        ],className="row"),
        html.Hr(),
                html.Div([
            html.Div([
                html.Div([
                    html.Div([
                        dcc.Graph(figure=fig_gsd)
                    ])
                ],className="card-header",)            
            ],className="col-xl-6",),
            html.Div([
                html.Div([
                    html.Div([
                         dcc.Graph(figure=fig_gstl)
                    ])
                ],className="card-header",)            
            ],className="col-xl-6",)
        ],className="row"),
        html.Hr(),
                html.Div([
            html.Div([
                html.Div([
                    html.Div([
                        dcc.Graph(figure=fig_elect)
                    ])
                ],className="card-header",)            
            ],className="col-xl-9",),
            html.Div([
                html.Div([
                    html.Div([
                       
                    ])
                ],className="card-header",)            
            ],className="col-xl-3",)
        ],className="row"),
    ], 
)

content = html.Div(id="page-content", style=CONTENT_STYLE)
app.layout = html.Div([dcc.Location(id="url"), sidebar, content])



############################## PAGES #####################

@app.callback(Output("page-content", "children"), [Input("url", "pathname")])
def render_page_content(pathname):
    if pathname == "/":
        return pageHome
    elif pathname == "/page-1":
        return pageDescriptive
    elif pathname == "/page-2":
        return pagePredictive
    # If the user tries to reach a different page, return a 404 message
    return dbc.Jumbotron(
        [
            html.H1("404: Not found", className="text-danger"),
            html.Hr(),
            html.P(f"The pathname {pathname} was not recognised..."),
        ]
    )

if __name__ == "__main__":
    app.run_server(host='127.0.0.1')
    # app.run_server(host='207.154.210.198')

yedek = html.Div(
    [
        html.H3("Predictive"),
        html.Hr(),
        html.Div([
            html.Div([
                html.Div([
                    html.Div([
                        
                    ])
                ],className="card-header",)            
            ],className="col-xl-6",),
            html.Div([
                html.Div([
                    html.Div([])
                ],className="card-header",)            
            ],className="col-xl-6",)
        ],className="row"),
        html.Hr(),
    ], 
)
