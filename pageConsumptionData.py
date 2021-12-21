import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
# from bootdash import app
from app import app
import style
import dataGlobals
import numpy as np

txtContent = """
Elektrik tüketim tahmini ve bu tahmin doğrultusunda santral dağılımının yeniden belirlenmesi sürecinde çok sayıda veri kullanılmaktadır. Elde edilen sonucun duyarlılığının belirlenebilmesi için kullanılan tüm verilerde yüzdesel değişiklikler yapılması gerekebilmektedir. 
Bu bölümde hem tahmin probleminin hem de karar probleminin çözümünde kullanılacak parametrelerde istenen değişikliklerin yapılabilmesi için bir alan oluşturulmuştur.
Herhangi bir değişiklik yapmak istemezseniz bu bölümü geçebilirsiniz.  
"""

pageConsumptionData = html.Div(
    [
        html.H3("What - If"),
              html.Div([
                html.Div([
                    html.Div([
                         html.P(txtContent,style = {'padding':"1rem"}),
                         html.Hr(),
                          html.Div([
                         html.Table([
                             html.Tr([
                                html.Td([html.P("Elektrik tüketim verileri",style={"text-align": "left","vertical-align":"middle", "margin":"1rem","padding":"8px"})],),
                                html.Td([html.P("%",style={"text-align": "right","vertical-align":"right", "margin":"1rem","padding":"8px"})]),
                                html.Td([html.Div(dcc.Input(id='input-tuketim-on-submit', value = 0, type='text', className="form-control", style={"color": "white"} )),]),
                                
                                  html.Td([html.Div(
                                    dcc.RadioItems(
                                            id='tuketimRadio',
                                            options=[
                                                {'label': 'Artır', 'value': 1},
                                                {'label': 'Azalt', 'value': -1},
                                            ],
                                            value=0,
                                            labelStyle={'display': 'inline-block'}
                                        )  
                                )]),

                                
                                
                             ]),

                             html.Tr([
                                html.Td([html.P("gsd",style={"text-align": "left","vertical-align":"middle", "margin":"1rem","padding":"8px"})],),
                                html.Td([html.P("%",style={"text-align": "right","vertical-align":"right", "margin":"1rem","padding":"8px"})]),
                                html.Td([html.Div(dcc.Input(id='input-gsd-on-submit', value = 0,type='text', className="form-control", style={"color": "white"} )),]),
                                  html.Td([html.Div(
                                    dcc.RadioItems(
                                            id='gsdRadio',
                                            options=[
                                                {'label': 'Artır', 'value': 1},
                                                {'label': 'Azalt', 'value': -1},
                                            ],
                                            value=0,
                                            labelStyle={'display': 'inline-block'}
                                        )  
                                )]), 
                             ]),

                              html.Tr([
                                html.Td([html.P("gstl",style={"text-align": "left","vertical-align":"middle", "margin":"1rem","padding":"8px"})],),
                                html.Td([html.P("%",style={"text-align": "right","vertical-align":"right", "margin":"1rem","padding":"8px"})]),
                                html.Td([html.Div(dcc.Input(id='input-gstl-on-submit', value = 0,type='text', className="form-control", style={"color": "white"} )),]),
                                  html.Td([html.Div(
                                    dcc.RadioItems(
                                            id='gstlRadio',
                                            options=[
                                                {'label': 'Artır', 'value': 1},
                                                {'label': 'Azalt', 'value': -1},
                                            ],
                                            value=0,
                                            labelStyle={'display': 'inline-block'}
                                        )  
                                )]), 
                             ]),

 html.Tr([
                                html.Td([html.P("nufus",style={"text-align": "left","vertical-align":"middle", "margin":"1rem","padding":"8px"})],),
                                html.Td([html.P("%",style={"text-align": "right","vertical-align":"right", "margin":"1rem","padding":"8px"})]),
                                html.Td([html.Div(dcc.Input(id='input-nufus-on-submit', value = 0, type='text', className="form-control", style={"color": "white"} )),]),
                                  html.Td([html.Div(
                                    dcc.RadioItems(
                                            id='nufusRadio',
                                            options=[
                                                {'label': 'Artır', 'value': 1},
                                                {'label': 'Azalt', 'value': -1},
                                            ],
                                            value=0,
                                            labelStyle={'display': 'inline-block'}
                                        )  
                                )]), 
                             ]),



 html.Tr([
                                html.Td([html.P("sue",style={"text-align": "left","vertical-align":"middle", "margin":"1rem","padding":"8px"})],),
                                html.Td([html.P("%",style={"text-align": "right","vertical-align":"right", "margin":"1rem","padding":"8px"})]),
                                html.Td([html.Div(dcc.Input(id='input-sue-on-submit', value = 0,type='text', className="form-control", style={"color": "white"} )),]),
                                  html.Td([html.Div(
                                    dcc.RadioItems(
                                            id='sueRadio',
                                            options=[
                                                {'label': 'Artır', 'value': 1},
                                                {'label': 'Azalt', 'value': -1},
                                            ],
                                            value=0,
                                            labelStyle={'display': 'inline-block'}
                                        )  
                                )]), 
                             ]),


                            #  html.Tr([
                            #     html.Td([html.P("Gayri Safi Yurtiçi Hasıla (Dolar)",style={"text-align": "left","vertical-align":"middle", "margin":"1rem","padding":"8px"})]),
                            #     html.Td([html.P("%",style={"text-align": "right","vertical-align":"right", "margin":"1rem","padding":"8px"})]),
                            #     html.Td([html.Div(dcc.Input(id='app1-gsd-input-on-submit', type='text', className="form-control", style={"color": "white"} )),]),
                            #     html.Td([html.Button('Artır', id='app1-gsd-submit-val-plus',  n_clicks=0, className = "btn btn-warning")]),
                            #     html.Td([html.Button('Azalt', id='app1-gsd-submit-val-minus',  n_clicks=0,  className = "btn btn-danger"),]),
                            #  ],style={"text-align": "center","vertical-align":"middle", "margin":"1rem","padding":"8px"}),
                            #   html.Tr([
                            #     html.Td([html.P("Gayri Safi Yurtiçi Hasıla (Türk Lirası)",style={"text-align": "left","vertical-align":"middle", "margin":"1rem","padding":"8px"})]),
                            #     html.Td([html.P("%",style={"text-align": "right","vertical-align":"right", "margin":"1rem","padding":"8px"})]),
                            #     html.Td([html.Div(dcc.Input(id='app1-input-on-submit', type='text', className="form-control", style={"color": "white"} )),]),
                            #     html.Td([html.Button('Artır', id='app1-submit-val-plus', n_clicks=0, className = "btn btn-warning")]),
                            #     html.Td([html.Button('Azalt', id='app1-submit-val-minus', n_clicks=0,  className = "btn btn-danger"),]),
                            #  ],style={"text-align": "center","vertical-align":"middle", "margin":"1rem","padding":"8px"}),
                            #   html.Tr([
                            #     html.Td([html.P("Sanayi Üretim Endeksi",style={"text-align": "left","vertical-align":"middle", "margin":"1rem","padding":"8px"})]),
                            #     html.Td([html.P("%",style={"text-align": "right","vertical-align":"right", "margin":"1rem","padding":"8px"})]),
                            #     html.Td([html.Div(dcc.Input(id='app1-input-on-submit', type='text', className="form-control", style={"color": "white"} )),]),
                            #     html.Td([html.Button('Artır', id='app1-submit-val-plus', n_clicks=0, className = "btn btn-warning")]),
                            #     html.Td([html.Button('Azalt', id='app1-submit-val-minus', n_clicks=0,  className = "btn btn-danger"),]),
                            #  ],style={"text-align": "center","vertical-align":"middle", "margin":"1rem","padding":"8px"}),
                            #   html.Tr([
                            #     html.Td([html.P("Nüfus",style={"text-align": "left","vertical-align":"middle", "margin":"1rem","padding":"8px"})]),
                            #     html.Td([html.P("%",style={"text-align": "right","vertical-align":"right", "margin":"1rem","padding":"8px"})]),
                            #     html.Td([html.Div(dcc.Input(id='app1-input-on-submit', type='text', className="form-control", style={"color": "white"} )),]),
                            #     html.Td([html.Button('Artır', id='app1-submit-val-plus', n_clicks=0, className = "btn btn-warning")]),
                            #     html.Td([html.Button('Azalt', id='app1-submit-val-minus', n_clicks=0,  className = "btn btn-danger"),]),
                            #  ],style={"text-align": "center","vertical-align":"middle", "margin":"1rem","padding":"8px"}),

                             html.Tr([
                                html.Td([]),
                                html.Td([]),
                                html.Td([]),
                                html.Td([]),

                                html.Td([html.Button('Uygula', id='submit-val', n_clicks=0, className = "btn btn-warning")]),
                                html.Td([html.Button('RESET', id='submit-val-res',  n_clicks=0, className = "btn btn-danger")]),
                                html.Div(id='container-button-basic',children='Enter a value and press submit')
                                
                             ]),
                         ],style={"text-align": "center","vertical-align":"middle", "margin":"1rem","padding":"8px"}),

],className="row justify-content-md-center"),

                         
                    ],style = {'background-color' : style.cardBackColor['back'],'box-shadow': '2px 5px 5px 1px rgba(30, 47, 123, .5)',"vertical-align":"middle"})            
                ],className="col-xl-12"),
              ],className="row",style={"height":"100vh"}),
        html.Hr(),
    ], 
)



tuketimDegisim = 0
gsdDegisim  = 0
gstlDegisim = 0
sueDegisim = 0
nufusDegisim = 0 

@app.callback(
        dash.dependencies.Output('container-button-basic', 'children'),
        [dash.dependencies.Input('submit-val', 'n_clicks')],
        [dash.dependencies.State('input-tuketim-on-submit', 'value'),
        dash.dependencies.State('tuketimRadio', 'value'),
        dash.dependencies.State('input-gsd-on-submit', 'value'),
        dash.dependencies.State('gsdRadio', 'value'),
        dash.dependencies.State('input-gstl-on-submit', 'value'),
        dash.dependencies.State('gstlRadio', 'value'),
        dash.dependencies.State('input-nufus-on-submit', 'value'),
        dash.dependencies.State('nufusRadio', 'value'),
        dash.dependencies.State('input-sue-on-submit', 'value'),
        dash.dependencies.State('sueRadio', 'value')]
    )
    
def update_output(n_clicks, tuketimValue, tuketimDurum, gsdValue, gsdDurum, gstlValue, gstlDurum, nufusValue, nufusDurum, sueValue, sueDurum):
    print('Elektrik tüketim verisi %{} {}'.format(tuketimValue,tuketimDurum))
    print('gsd  verisi %{} {}'.format(gsdValue,gsdDurum))
    print('gstl  verisi %{} {}'.format(gstlValue,gstlDurum))
    print('nufus  verisi %{} {}'.format(nufusValue,nufusDurum))
    print('sue  verisi %{} {}'.format(sueValue,sueDurum))

    yuzdeler = [float(tuketimValue), float(gsdValue), float(gstlValue), float(nufusValue), float(sueValue)]
    durum = [tuketimDurum, gsdDurum, gstlDurum, nufusDurum, sueDurum]

    yuzdeler = np.array(yuzdeler)
    durum = np.array(durum)

    print(yuzdeler * durum)

    hesap = (yuzdeler * durum + 100) / 100

    dataGlobals.veriEdit(hesap)

    return '{}{}'.format(
        tuketimValue,
        n_clicks
    )



