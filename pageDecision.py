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

pageDecision = html.Div(
    [
        html.H3("Decision"),
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
                                html.Td([html.P("Santral seçiminde kullanılan kriterlerin ağırlıklarını belirlemek için yöntem seçiniz.",style={"text-align": "left","vertical-align":"middle", "margin":"1rem","padding":"8px"})]),
                                html.Td([]),
                                html.Td([]),
                                html.Td([]),
                             ],style={"text-align": "center","vertical-align":"middle", "margin":"1rem","padding":"8px"}),
                            html.Tr([
                                html.Td([]),
                                html.Td([html.Div(
                                    dcc.RadioItems(
                                            options=[
                                                {'label': 'Tüm kriterleri eşit ağırlıkta kabul ederek devam etmek istiyorum', 'value': 'NYC'},
                                                 {'label': 'Tüm kriterlerin ağırlıklarını kendim girmek istiyorum.', 'value': 'dsf'},
                                                  {'label': 'Tüm kriterlerin ağırlıklarını objektif yöntemlerle belirlemek istiyorum.', 'value': 'gdfg'},
                                               
                                            ],
                                            value='MTL',
                                            labelStyle={'display': 'block'}
                                        )  
                                )]),
                                html.Td([]),
                                html.Td([]),
                            ],style={"text-align": "left","vertical-align":"middle", "margin":"1rem","padding":"8px"}),
                           
                            html.Tr([
                                html.Td([]),
                                html.Td([html.Div(
                                    dcc.RadioItems(
                                            options=[
                                                {'label': 'Entropi', 'value': 'NYC'},
                                                 {'label': 'Critic', 'value': 'dsf'},
                                                  
                                               
                                            ],
                                            value='MTL',
                                            labelStyle={'display': 'inline-block'}
                                        )  
                                )]),
                                html.Td([]),
                                html.Td([]),
                            ],style={"text-align": "center","vertical-align":"middle", "margin":"1rem","padding":"8px"}),
                              html.Tr([
                                html.Td([]),
                                html.Td([html.Div(
                                    dcc.RadioItems(
                                            options=[
                                                {'label': 'Tüm kriterlerin ağırlıklarını sübjektif yöntemlerle belirlemek istiyorum.', 'value': 'NYC'},
                                            
                                               
                                            ],
                                            value='MTL',
                                            labelStyle={'display': 'block'}
                                        )  
                                )]),
                                html.Td([]),
                                html.Td([]),
                            ],style={"text-align": "left","vertical-align":"middle", "margin":"1rem","padding":"8px"}),
                            html.Tr([
                                html.Td([]),
                                html.Td([html.Div(
                                    dcc.RadioItems(
                                            options=[
                                                {'label': 'Swara', 'value': 'NYC'},
                                                 {'label': 'Fucom', 'value': 'dsf'},
                                                  
                                               
                                            ],
                                            value='MTL',
                                            labelStyle={'display': 'inline-block'}
                                        )  
                                )]),
                                html.Td([]),
                                html.Td([]),
                            ],style={"text-align": "center","vertical-align":"middle", "margin":"1rem","padding":"8px"}),
                              
                         ],style={"text-align": "center","vertical-align":"middle", "margin":"1rem","padding":"8px"}),

],className="row justify-content-md-center"),

                         
                    ],style = {'background-color' : style.cardBackColor['back'],'box-shadow': '2px 5px 5px 1px rgba(30, 47, 123, .5)',"vertical-align":"middle"})            
                ],className="col-xl-12"),
              ],className="row",style={"height":"100vh"}),
        html.Hr(),
    ], 
)



@app.callback(
    dash.dependencies.Output('app4-input-on-submit', 'value'),
    [dash.dependencies.Input('app4-submit-val-plus', 'n_clicks')],
    [dash.dependencies.Input('app4-submit-val-minus', 'n_clicks')],
    [dash.dependencies.State('app4-input-on-submit', 'value')])
def update_output(value,n_clicks,nclicks):
    print(value, n_clicks)
    if value==None:
        value=0
    value = value+1
    return '{}'.format(value)