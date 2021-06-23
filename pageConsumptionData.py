import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
# from bootdash import app
from app import app
import style

txtContent = """
Elektrik tüketim tahmini ve bu tahmin doğrultusunda santral dağılımının yeniden belirlenmesi sürecinde çok sayıda veri kullanılmaktadır. Elde edilen sonucun duyarlılığının belirlenebilmesi için kullanılan tüm verilerde yüzdesel değişiklikler yapılması gerekebilmektedir. 
Bu bölümde hem tahmin probleminin hem de karar probleminin çözümünde kullanılacak parametrelerde istenen değişikliklerin yapılabilmesi için bir alan oluşturulmuştur.
Herhangi bir değişiklik yapmak istemezseniz bu bölümü geçebilirsiniz.  
"""

pageConsumptionData = html.Div(
    [
        html.H3("Consumption Data"),
              html.Div([
                html.Div([
                    html.Div([
                         html.P(txtContent,style = {'padding':"1rem"}),
                         html.Hr(),
                          html.Div([
                         html.Table([
                             html.Tr([
                                html.Td([html.P("Elektrik tüketim verileri",style={"text-align": "left","vertical-align":"middle", "margin":"1rem","padding":"8px"})],),
                                html.Td([html.Div(dcc.Input(id='app1-input-on-submit', type='text', className="form-control",)),]),
                                html.Td([html.Button('Artır', id='app1-submit-val-plus', n_clicks=0, className = "btn btn-warning")]),
                                html.Td([html.Button('Azalt', id='app1-submit-val-minus', n_clicks=0,  className = "btn btn-danger"),]),
                             ]),
                             html.Tr([
                                html.Td([html.P("Gayri Safi Yurtiçi Hasıla (Dolar)",style={"text-align": "left","vertical-align":"middle", "margin":"1rem","padding":"8px"})]),
                                html.Td([html.Div(dcc.Input(id='app1-input-on-submit', type='text', className="form-control")),]),
                                html.Td([html.Button('Artır', id='app1-submit-val-plus', n_clicks=0, className = "btn btn-warning")]),
                                html.Td([html.Button('Azalt', id='app1-submit-val-minus', n_clicks=0,  className = "btn btn-danger"),]),
                             ],style={"text-align": "center","vertical-align":"middle", "margin":"1rem","padding":"8px"}),
                              html.Tr([
                                html.Td([html.P("Gayri Safi Yurtiçi Hasıla (Türk Lirası)",style={"text-align": "left","vertical-align":"middle", "margin":"1rem","padding":"8px"})]),
                                html.Td([html.Div(dcc.Input(id='app1-input-on-submit', type='text', className="form-control")),]),
                                html.Td([html.Button('Artır', id='app1-submit-val-plus', n_clicks=0, className = "btn btn-warning")]),
                                html.Td([html.Button('Azalt', id='app1-submit-val-minus', n_clicks=0,  className = "btn btn-danger"),]),
                             ],style={"text-align": "center","vertical-align":"middle", "margin":"1rem","padding":"8px"}),
                              html.Tr([
                                html.Td([html.P("Sanayi Üretim Endeksi",style={"text-align": "left","vertical-align":"middle", "margin":"1rem","padding":"8px"})]),
                                html.Td([html.Div(dcc.Input(id='app1-input-on-submit', type='text', className="form-control")),]),
                                html.Td([html.Button('Artır', id='app1-submit-val-plus', n_clicks=0, className = "btn btn-warning")]),
                                html.Td([html.Button('Azalt', id='app1-submit-val-minus', n_clicks=0,  className = "btn btn-danger"),]),
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
    dash.dependencies.Output('app1-input-on-submit', 'value'),
    [dash.dependencies.Input('app1-submit-val-plus', 'n_clicks')],
    [dash.dependencies.Input('app1-submit-val-minus', 'n_clicks')],
    [dash.dependencies.State('app1-input-on-submit', 'value')])
def update_output(value,n_clicks,nclicks):
    print(value, n_clicks)
    if value==None:
        value=0
    value = " "
    return '{}'.format(value)