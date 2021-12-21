import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from app import app
import style
import dataGlobals
import numpy as np
import pandas as pd
import time



txtContent = """
Karar Destek Sisteminde çok sayıda veri kullanılmakta olup, bu veriler üzerinde çok sayıda veri önişleme yöntemi uygulanmaktadır. Ayrıca uygulanan analitik yöntemlerin çoğu verinin formatına bağlı olarak çalışmaktadır. Bu sebeple yeni veri yüklenebilmesi için aşağıdaki şartların sağlanması gerekmektedir.
"""
pageAddingData = html.Div(
    [
        html.H3("Adding Data"),
              html.Div([
                html.Div([
                    html.Div([
                        html.P(txtContent, style = {'padding':"1rem"}),
                        html.Ul([
                             html.Li("Öncelikle hangi veri türüne ekleme/silme işlemi uygulanacağı seçimi yapılmalıdır. "),
                             html.Li("Tüketim verileri ay bazlı zaman serisi verileri olduğu için veritabanında yer alan verilerin bir kısmını silebilir veya değiştirebilirsiniz."),
                             html.Li("Santral seçim kriterleri ile ilgili santral türü bazlı veriler yer aldığı için ilgili kriterle ilgili verileri değiştirebilir, bu verileri silebilir veya ekleyebilirsiniz."),
                             html.Li("•	Eksik veri tanımlanması durumunda Veri Madenciliği yöntemleriyle eksik veriler tamamlanacaktır. Bu sebeple sonuçların gerçeğe daha yakın olması için eksik veri bırakmamanız önemlidir."),     
                        ]),
                        html.Table([
                            html.Tr([
                                 html.Td([html.P('Yıl')]),
                                 html.Td([html.P('Tuketim')]),
                                 html.Td([html.P('GSD')]),
                                 html.Td([html.P('GSTL')]),
                                 html.Td([html.P('Nufus')]),
                                 html.Td([html.P('SUE')]), 
                            ]),      
                        html.Tr([
                                html.Td([dcc.Dropdown(
                                    id='select-year', 
                                    value='1980', 
                                    options=[{'value': x, 'label': x} 
                                            for x in range(1980,2021)],
                                    clearable=False,style={'width': "80%","font_color":style.cardBackColor['back'],"padding-left":60},
                                ),],),
                                 html.Td([html.Div(dcc.Input(id='input-tuketim-on-submit', value = 0, type='text', className="form-control", style={"color": "white"} )),]),
                                 html.Td([html.Div(dcc.Input(id='input-gsd-on-submit', value = 0, type='text', className="form-control", style={"color": "white"} )),]),
                                 html.Td([html.Div(dcc.Input(id='input-gstl-on-submit', value = 0, type='text', className="form-control", style={"color": "white"} )),]),
                                 html.Td([html.Div(dcc.Input(id='input-nufus-on-submit', value = 0, type='text', className="form-control", style={"color": "white"} )),]),
                                 html.Td([html.Div(dcc.Input(id='input-sue-on-submit', value = 0, type='text', className="form-control", style={"color": "white"} )),]),
                            ]),      
                         ],style={"text-align": "center","vertical-align":"middle", "margin":"1rem","padding":"8px"}),
                        html.Div([
                             html.Div([
                                   
                                        html.Div([
                                           
                                            html.Button("Düzenle", n_clicks = 0, id = "submit-val-edit", className = "btn btn-warning", style={"text-align": "center","vertical-align":"middle", "margin":"10px"}),
                                            html.Button("Reset", n_clicks = 0, id = "submit-val-res", className = "btn btn-danger"),
                                            html.Div(id='container-button-basic',children=''),
                                        ],style={"text-align": "center","vertical-align":"middle", "margin":"1rem","padding":"8px"}),
                              ],className="col-m-6",),
                            
                        ],className="row justify-content-md-center"),
                    ],style = {'background-color' : style.cardBackColor['back'],'box-shadow': '2px 5px 5px 1px rgba(30, 47, 123, .5)',"vertical-align":"middle"})            
                ],className="col-xl-12"),
              ],className="row",style={"height":"100vh"}),
        html.Hr(),
    ], 
)

tiklama_edit = 0
tiklama_res = 0

@app.callback(
        Output('input-tuketim-on-submit', 'value'),
        Output('input-gsd-on-submit', 'value'),
        Output('input-gstl-on-submit', 'value'),
        Output('input-nufus-on-submit', 'value'),
        Output('input-sue-on-submit', 'value'),
        dash.dependencies.Input('submit-val-edit', 'n_clicks'),
        dash.dependencies.Input('submit-val-res', 'n_clicks'),
        Input("select-year", "value"),
        dash.dependencies.State('input-tuketim-on-submit', 'value'),
        dash.dependencies.State('input-gsd-on-submit', 'value'),
        dash.dependencies.State('input-gstl-on-submit', 'value'),
        dash.dependencies.State('input-nufus-on-submit', 'value'),
        dash.dependencies.State('input-sue-on-submit', 'value'),
)
def update_output(n_clicks1,n_clicks2, yearValue, tuketimValue, gsdValue, gstlValue, nufusValue, sueValue):
    print('N clicks {}'.format(n_clicks1))
    print('Secilen Yıl {}'.format(yearValue))
    print('Elektrik tüketim verisi {}'.format(tuketimValue))
    print('gsd  verisi {}'.format(gsdValue))
    print('gstl  verisi {}'.format(gstlValue))
    print('nufus  verisi {}'.format(nufusValue))
    print('sue  verisi {}'.format(sueValue))


    

    global tiklama_edit
    global tiklama_res

    if n_clicks1 == 0 and n_clicks2 == 0:
            tiklama_edit = 0 
            tiklama_res = 0 
            


    if n_clicks1 > tiklama_edit:
        index = int(yearValue) -  1980
        print("Ekle Tıklandı")
        # if int(yearValue) > 2020:
        #     print("Yıl Eklendi")
        #     df2 = pd.DataFrame([[1945,6,7,8,9,10]], columns=['Year', 'Tuketim', 'GSD', 'GSTL', 'Nufus', 'SUE'], index=['x'])
        #     dataGlobals.df_manipule.append(df2, ignore_index=True)
        # else:
        dataGlobals.df_manipule.loc[index,'Tuketim'] = tuketimValue
        dataGlobals.df_manipule.loc[index,'GSD'] = gsdValue
        dataGlobals.df_manipule.loc[index,'GSTL'] = gstlValue
        dataGlobals.df_manipule.loc[index,'Nufus'] = nufusValue
        dataGlobals.df_manipule.loc[index,'SUE'] = sueValue
        print("Veriler Eklendi")
        tiklama_edit += 1

    if n_clicks2 > tiklama_res:
        print("res")
        dataGlobals.reset_manipule()
        tiklama_res += 1
        time.sleep(0.5)
        

    

    print("verilerin guncellemesi gerek")
    getData = dataGlobals.getDataWithYear(yearValue)
    return getData[0], getData[1], getData[2],getData[3],getData[4]
