# -*- coding: utf-8 -*-
"""
Created on Sun Jan  9 18:10:21 2022

@author: uzeyi
"""
import plotly.figure_factory as ff

data_matrix = [['Eğitim/Test', 'Değişken', 'MAPE', 'MAE', 'RMSE', 'rMAPE', 'rMAE', 'rRMSE'],
               ['Eğitim', 'Elektrik Tüketimi', 6.198, 2875.96, 3265.622, 0.00062, 0.028547, 0.032415],
               ['Eğitim', 'Sanayi Üretim E.', 31.792, 11.7757, 14.2277, 0.856922, 0.317406, 0.383497],
               ['Eğitim', 'Nüfus', 0.6504, 347.52, 395.9647, 0.002808, 0.015005, 0.017097],
               ['Eğitim', 'GSYİH (TL)', 13.4531, 60.4739, 76.6534, 0.023315, 0.104805, 0.132844],               
               ['Eğitim', 'GSYİH (Dolar)', 32.5109, 49.2407, 67.1975, 0.093185, 0.141137, 0.192606],
               ['Test', 'Elektrik Tüketimi', 3.072, 6412.294, 8497.137, 0.00020, 0.041665, 0.055212],
               ['Test', 'Sanayi Üretim E.', 13.5961, 9.7533, 12.0816, 0.243658, 0.174791, 0.216517],
               ['Test', 'Nüfus', 0.4446, 333.0625, 378.4602, 0.00297, 0.022278, 0.025315],
               ['Test', 'GSYİH (TL)', 10.5277, 173.3447, 198.5164, 0.002407, 0.039635, 0.045391],
               ['Test', 'GSYİH (Dolar)', 16.3917, 129.0359, 151.0679, 0.036307, 0.28581, 0.33461]               
               ]

fig =  ff.create_table(data_matrix, height_constant=20)


# import dash
# import dash_core_components as dcc
# import dash_html_components as html

# app = dash.Dash()
# app.layout = html.Div([
#     dcc.Graph(figure=fig)
# ])

# app.run_server(debug=True, use_reloader=False)  # Turn off reloader if inside Jupyter