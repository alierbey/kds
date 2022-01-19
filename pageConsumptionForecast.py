import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
# from bootdash import app
from app import app
import style
import dataGlobals as dataGlobal


txtContent1 = """
Elektrik tüketim tahmini temelde bir zaman serisi problemidir. Zaman serileri ile yapılacak tahmin çalışmalarında çok sayıda yöntem kullanılabilmektedir. Kullanmakta olduğunuz KDS’de LSTM (Long Short Term Memory) algoritması kullanılmıştır. Bu bölümde hangi yıla kadar tahmin yapılacağını belirlemeniz yeterli olmaktadır. 
"""
txtContent2 = """
Karar verme problemi çözümünde ise en temel gereksinimlerden biri kriterlerin ağırlıklandırılmasıdır. Kullanmakta olduğunuz Web Tabanlı Karar Destek Sistemi’nde (WTKDS) sizin seçiminizle uygulanacak Çok Kriterli Karar Verme Yöntemleri (ÇKKVY) için ağırlık belirleme süreci farklı şekillerde uygulanabilmektedir. 
"""
txtContent3 = """
Bu bölümde hem tahmin probleminin hem de karar probleminin çözümünde kullanılacak parametrelerin belirlenmesi gerekmektedir.
"""

pageConsumptionForecast = html.Div(
    [
        html.H3("Tahmin Parametreleri"),
              html.Div([
                html.Div([
                    html.Div([
                         html.P(txtContent1,style = {'padding':"1rem"}),
                     
                         html.Hr(),
                          html.Div([
                         html.Table([
                             html.Tr([
                                html.Td([html.P("Elektrik tüketim tahmini için yıl seçiniz",style={"text-align": "left","vertical-align":"middle", "margin":"1rem","padding":"8px"})],),
                                dcc.Dropdown(
                                    id='slct_cat_year1', 
                                    value='2021', 
                                    options=[{'value': x, 'label': x} 
                                            for x in range(2021,2041)],
                                    clearable=False
                                ),

                                html.Td([]),
                                html.Td([]),
                             ]),
                            #  html.Tr([
                            #     html.Td([html.P("Elektrik tüketim tahmini için kullanılacak algoritmayı seçiniz.",style={"text-align": "left","vertical-align":"middle", "margin":"1rem","padding":"8px"})]),
                            #     html.Td([]),
                            #     html.Td([]),
                            #     html.Td([]),
                            #  ],style={"text-align": "center","vertical-align":"middle", "margin":"1rem","padding":"8px"}),
                            # html.Tr([
                            #     html.Td([]),
                            #     html.Td([html.Div(
                            #         dcc.RadioItems(
                            #                 options=[
                            #                     {'label': 'Doğrusal Regresyon', 'value': 'NYC'},
                            #                      {'label': 'Çok Değişkenli Doğrusal Regresyon', 'value': 'dsf'},
                            #                       {'label': 'Yinelenen Sinir Ağı (RNN)', 'value': 'gdfg'},
                            #                       {'label': 'Uzun Kısa Süreli Bellek (LSTM)', 'value': 'dfg'},
                            #                 ],
                            #                 value='MTL',
                            #                 labelStyle={'display': 'block'}
                            #             )  
                            #     )]),
                            #     html.Td([]),
                            #     html.Td([]),
                            # ],style={"text-align": "left","vertical-align":"middle", "margin":"1rem","padding":"8px"}),
                           
                              html.Td([html.Div(dcc.Input(id='yeap_output1', value = 0, type='text', className="form-control", style={"color": "gray",'display': 'none'} )),]),
                              #  html.Td([html.Div(dcc.Input(id='yeap_input1', value = 0, type='text', className="form-control", style={"color": "gray"} )),]),
                              
                         ],style={"text-align": "center","vertical-align":"middle", "margin":"1rem","padding":"8px"}),

],className="row justify-content-md-center"),

                         
                    ],style = {'background-color' : style.cardBackColor['back'],'box-shadow': '2px 5px 5px 1px rgba(30, 47, 123, .5)',"vertical-align":"middle"})            
                ],className="col-xl-12"),
              ],className="row",style={"height":"100vh"}),
      
    ], 
)



@app.callback(
    dash.dependencies.Output('yeap_output1', 'value'),
    dash.dependencies.Input("slct_cat_year1", "value"),
    #  dash.dependencies.State('yeap_input1', 'value'),
    )
def update_output(value1):
    print(value1)
    dataGlobal.seciliTarih = int(value1)
    print(dataGlobal.seciliTarih)
    # prs_card1.fig
    return ""
    