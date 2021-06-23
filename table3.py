import dash
from dash.dependencies import Input, Output
import dash_table
import dash_html_components as html


import pandas as pd
import numpy as np
from app import app
import style


kriterler = np.array(["Üretim", "Kapasite Faktörü", "Kurulu Güç", "CO2", "CH4", 
                       "NOx", "SO2", "Arazi Kullanımı", "Yatırım Maliyeti", 
                       "İsletme Maliyeti", "Yakıt Maliyeti", "Geri Odeme_S.", "İstihdam"])

w = np.array([0.193066, 0.175514, 0.152621, 0.127184, 0.101747, 0.0782672, 0.0579757,
           0.0414112, 0.0285595, 0.0190397, 0.0122836, 0.00767728, 0.0046529])
fm = np.array(['Fayda', 'Fayda','Fayda','Maliyet','Maliyet','Maliyet','Maliyet','Maliyet',
               'Maliyet','Maliyet','Maliyet','Maliyet','Fayda'])

X1 = pd.DataFrame(kriterler)
X2 = pd.DataFrame(fm)
X3 = pd.DataFrame(w)

x = pd.concat([X1, X2, X3], axis=1)
x.columns =['Kriterler', 'Etki', 'Ağırlık']
# x.index = x.Kriterler
# x.drop('Kriterler', axis=1, inplace=True)



table3 = dash_table.DataTable(
    
    id='table-filtering-be',
    columns=[
        {"name": i, "id": i} for i in (x.columns)
    ],
    page_current=0,
    page_size=15,
    page_action='native',
    filter_action='native',
    filter_query='',
    data=x.to_dict('records'),
    
  
    style_data={
       
        'overflow': 'hidden',
        'textOverflow': 'ellipsis',
       
    },
    style_header={'backgroundColor': 'rgb(30, 30, 30)'},
    style_cell={
        'backgroundColor': style.cardBackColor['back'],
        'color': 'white'
    },
)



@app.callback(
    Output('table-filtering-be', 'data'),
    Input('table-filtering-be', "page_current"),
    Input('table-filtering-be', "page_size"))
def update_table(page_current,page_size):
    return x.iloc[
        page_current*page_size:(page_current+ 1)*page_size
    ].to_dict('records')


