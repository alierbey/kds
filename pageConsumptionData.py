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
import dataGlobals

txtContent = """
Elektrik tüketim tahmini ve bu tahmin doğrultusunda santral dağılımının yeniden belirlenmesi sürecinde çok sayıda veri kullanılmaktadır. Elde edilen sonucun duyarlılığının belirlenebilmesi için kullanılan tüm verilerde yüzdesel değişiklikler yapılması gerekebilmektedir. Bu bölümde tahmin probleminin çözümünde kullanılacak parametrelerde istenen değişikliklerin yapılabilmesi için bir alan oluşturulmuştur. Herhangi bir değişiklik yapmak istemezseniz bu bölümü geçebilirsiniz.  
"""

pageConsumptionData = html.Div(
    [
        html.H3("Eğer - Ne"),
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
                                html.Td([html.Div(dcc.Input(id='input-tuketim-on-submit', value = 0, type='text', className="form-control", style={"color": "gray"} )),]),
                                
                                  html.Td([html.Div(
                                    dcc.RadioItems(
                                            id='tuketimRadio',
                                            options=[
                                                {'label': 'Artır', 'value': 1},
                                                {'label': 'Azalt', 'value': -1},
                                            ],
                                            value=0,
                                            labelStyle={'display': 'inline-block', 'padding': 15, }
                                        )  
                                )]),

                                
                                
                             ]),

                             html.Tr([
                                html.Td([html.P("GSD",style={"text-align": "left","vertical-align":"middle", "margin":"1rem","padding":"8px"})],),
                                html.Td([html.P("%",style={"text-align": "right","vertical-align":"right", "margin":"1rem","padding":"8px"})]),
                                html.Td([html.Div(dcc.Input(id='input-gsd-on-submit', value = 0,type='text', className="form-control", style={"color": "gray"} )),]),
                                  html.Td([html.Div(
                                    dcc.RadioItems(
                                            id='gsdRadio',
                                            options=[
                                                {'label': 'Artır', 'value': 1},
                                                {'label': 'Azalt', 'value': -1},
                                            ],
                                            value=0,
                                            labelStyle={'display': 'inline-block', 'padding': 15, }
                                        )  
                                )]), 
                             ]),

                              html.Tr([
                                html.Td([html.P("GSTL",style={"text-align": "left","vertical-align":"middle", "margin":"1rem","padding":"8px"})],),
                                html.Td([html.P("%",style={"text-align": "right","vertical-align":"right", "margin":"1rem","padding":"8px"})]),
                                html.Td([html.Div(dcc.Input(id='input-gstl-on-submit', value = 0,type='text', className="form-control", style={"color": "gray"} )),]),
                                  html.Td([html.Div(
                                    dcc.RadioItems(
                                            id='gstlRadio',
                                            options=[
                                                {'label': 'Artır', 'value': 1},
                                                {'label': 'Azalt', 'value': -1},
                                            ],
                                            value=0,
                                            labelStyle={'display': 'inline-block', 'padding': 15, }
                                        )  
                                )]), 
                             ]),

 html.Tr([
                                html.Td([html.P("Nüfus",style={"text-align": "left","vertical-align":"middle", "margin":"1rem","padding":"8px"})],),
                                html.Td([html.P("%",style={"text-align": "right","vertical-align":"right", "margin":"1rem","padding":"8px"})]),
                                html.Td([html.Div(dcc.Input(id='input-nufus-on-submit', value = 0, type='text', className="form-control", style={"color": "gray"} )),]),
                                  html.Td([html.Div(
                                    dcc.RadioItems(
                                            id='nufusRadio',
                                            options=[
                                                {'label': 'Artır', 'value': 1},
                                                {'label': 'Azalt', 'value': -1},
                                            ],
                                            value=0,
                                            labelStyle={'display': 'inline-block', 'padding': 15, }
                                        )  
                                )]), 
                             ]),



 html.Tr([
                                html.Td([html.P("SUE",style={"text-align": "left","vertical-align":"middle", "margin":"1rem","padding":"8px"})],),
                                html.Td([html.P("%",style={"text-align": "right","vertical-align":"right", "margin":"1rem","padding":"8px"})]),
                                html.Td([html.Div(dcc.Input(id='input-sue-on-submit', value = 0,type='text', className="form-control", style={"color": "gray"} )),]),
                                  html.Td([html.Div(
                                    dcc.RadioItems(
                                            id='sueRadio',
                                            options=[
                                                {'label': 'Artır', 'value': 1},
                                                {'label': 'Azalt', 'value': -1},
                                            ],
                                            value=0,
                                            labelStyle={'display': 'inline-block', 'padding': 15, }
                                        )  
                                )]), 
                             ]),


                           

                             html.Tr([
                                html.Td([]),
                                html.Td([]),
                                html.Td([]),
                                html.Td([]),

                                html.Td([html.Button('Uygula', id='submit-val', n_clicks=0, className = "btn btn-warning")]),
                                html.Td([html.Button('RESET', id='submit-val-res',  n_clicks=0, className = "btn btn-danger")]),
                                html.Div(id='container-button-basic',children='')
                                
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

    tuketimValue = int(tuketimValue)
    gsdValue = int(gsdValue)
    gstlValue = int(gstlValue)
    nufusValue = int(nufusValue)
    sueValue = int(sueValue)

    if tuketimDurum == 0:
      tuketimValue = tuketimValue * (-1)

    if gsdDurum == 0:
      gsdValue = gsdValue * (-1)

    if gstlDurum == 0:
      gstlValue = gstlValue * (-1)

    if nufusDurum == 0:
      nufusValue = nufusValue * (-1)

    if sueDurum == 0:
      sueValue = sueValue * (-1)

    dataGlobals.tuketim_d = tuketimValue
    dataGlobals.gsd_d = gsdValue
    dataGlobals.gstl_d = gstlValue
    dataGlobals.nufus_d = nufusValue
    dataGlobals.sue_d = sueValue

    print('Elektrik tüketim verisi %{} {}'.format(tuketimValue,tuketimDurum))
    print('gsd  verisi %{} {}'.format(gsdValue,gsdDurum))
    print('gstl  verisi %{} {}'.format(gstlValue,gstlDurum))
    print('nufus  verisi %{} {}'.format(nufusValue,nufusDurum))
    print('sue  verisi %{} {}'.format(sueValue,sueDurum))

    # yuzdeler = np.array(yuzdeler)
    # durum = np.array(durum)

    # print(yuzdeler * durum)

    # hesap = (yuzdeler * durum + 100) / 100

    # dataGlobals.veriEdit(hesap)

    return ""



