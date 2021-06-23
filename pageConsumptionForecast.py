import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
# from bootdash import app
from app import app
import style

txtContent1 = """
Elektrik tahmini temelde bir 

zaman serisi problemidir. Zaman serileri ile yapılacak tahmin çalışmalarında çok sayıda yöntem kullanılabilmektedir. Her yöntemin için verilerin bir dizi ön işleme tabi tutulması gerekmektedir. Bu sebeple verilere bir dizi ön işlem uygulanarak seçtiğiniz algoritmaya uygun hale getirilecektir. Bu bölümde öncelikle tahmin problemi için belirtmeniz gereken bazı parametreler bulunmaktadır. 

"""
txtContent2 = """
Karar verme problemi çözümünde ise en temel gereksinimlerden biri kriterlerin ağırlıklandırılmasıdır. Kullanmakta olduğunuz Web Tabanlı Karar Destek Sistemi’nde (WTKDS) sizin seçiminizle uygulanacak Çok Kriterli Karar Verme Yöntemleri (ÇKKVY) için ağırlık belirleme süreci farklı şekillerde uygulanabilmektedir. 
"""
txtContent3 = """
Bu bölümde hem tahmin probleminin hem de karar probleminin çözümünde kullanılacak parametrelerin belirlenmesi gerekmektedir.
"""

pageConsumptionForecast = html.Div(
    [
        html.H3("Consumption Forecast"),
              html.Div([
                html.Div([
                    html.Div([
                         html.P(txtContent1,style = {'padding':"1rem"}),
                         html.P(txtContent2,style = {'padding':"1rem"}),
                         html.P(txtContent3,style = {'padding':"1rem"}),
                         html.Hr(),
                          html.Div([
                         html.Table([
                             html.Tr([
                                html.Td([html.P("Elektrik tüketim tahmini için süre giriniz(Ay)",style={"text-align": "left","vertical-align":"middle", "margin":"1rem","padding":"8px"})],),
                                html.Td([html.Div(dcc.Input(id='app1-input-on-submit', type='text', className="form-control",)),]),
                                html.Td([]),
                                html.Td([]),
                             ]),
                             html.Tr([
                                html.Td([html.P("Elektrik tüketim tahmini için kullanılacak algoritmayı seçiniz.",style={"text-align": "left","vertical-align":"middle", "margin":"1rem","padding":"8px"})]),
                                html.Td([]),
                                html.Td([]),
                                html.Td([]),
                             ],style={"text-align": "center","vertical-align":"middle", "margin":"1rem","padding":"8px"}),
                            html.Tr([
                                html.Td([]),
                                html.Td([html.Div(
                                    dcc.RadioItems(
                                            options=[
                                                {'label': 'Doğrusal Regresyon', 'value': 'NYC'},
                                                 {'label': 'Çok Değişkenli Doğrusal Regresyon', 'value': 'dsf'},
                                                  {'label': 'Yinelenen Sinir Ağı (RNN)', 'value': 'gdfg'},
                                                  {'label': 'Uzun Kısa Süreli Bellek (LSTM)', 'value': 'dfg'},
                                            ],
                                            value='MTL',
                                            labelStyle={'display': 'block'}
                                        )  
                                )]),
                                html.Td([]),
                                html.Td([]),
                            ],style={"text-align": "left","vertical-align":"middle", "margin":"1rem","padding":"8px"}),
                           
                            
                              
                              
                         ],style={"text-align": "center","vertical-align":"middle", "margin":"1rem","padding":"8px"}),

],className="row justify-content-md-center"),

                         
                    ],style = {'background-color' : style.cardBackColor['back'],'box-shadow': '2px 5px 5px 1px rgba(30, 47, 123, .5)',"vertical-align":"middle"})            
                ],className="col-xl-12"),
              ],className="row"),
        html.Hr(),
    ], 
)



@app.callback(
    dash.dependencies.Output('app3-input-on-submit', 'value'),
    [dash.dependencies.Input('app3-submit-val-plus', 'n_clicks')],
    [dash.dependencies.Input('app3-submit-val-minus', 'n_clicks')],
    [dash.dependencies.State('app3-input-on-submit', 'value')])
def update_output(value,n_clicks,nclicks):
    print(value, n_clicks)
    if value==None:
        value=0
    value = value+1
    return '{}'.format(value)