import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
# from bootdash import app
from app import app
import style

txtContent = """
Bu sayfada Hedef Arama analizleri doğrultusunda dışa bağımlılık, yenilenebilir enerji kullanımı ve enerji çeşitliliğiyle ilgili senaryolar oluşturulmuştur. 
"""

pageEnergyMixData = html.Div(
    [
        html.H3("Goal Seeking"),
              html.Div([
                html.Div([
                    html.Div([
                         
                         html.Hr(),
                          html.Div([
                                html.Div([
                         html.Div(html.Img(src=("assets/images/goal.jpeg"), style={"max-width":"100%", "height":"auto"})),
                    ],style = {'background-color' : style.cardBackColor['back'],'box-shadow': '2px 5px 5px 1px rgba(30, 47, 123, .5)',"vertical-align":"middle"}) ,           
                     
                     html.P(txtContent,style = {'padding':"1rem"}),

                     html.P("SENARYO 1:Dışa bağımlılık oranı istediğiniz bir değerde sabit tutarak enerji karmasının nasıl planlanması gerektiğiniz bulabilirsiniz."),

                     html.P("Elektrik üretimi için kullanılan kaynaklarda 2020 yılı itibariyle dışa bağımlılık oranı %43,6’dır."),
                            html.Table([
                              html.Tr([
                                html.Td([html.P("Lütfen planladığınız dışa bağımlılık oranını giriniz.",style={"text-align": "left","vertical-align":"middle", "margin":"1rem","padding":"2px"})],),
                                html.Td([html.P("%",style={"text-align": "right","vertical-align":"right", "margin":"1rem","padding":"8px"})]),
                                html.Td([html.Div(dcc.Input(id='input-senaryo1-on-submit', value = 0,type='text', className="form-control", style={"color": "white"} )),]),
                                html.Td([html.Button('Hesapla', id='submit-btn1-val', n_clicks=0, className = "btn btn-warning")]),
                              #   html.Div(id='container-button-basic',children='Enter a value and press submit')
                             ]),

                    ],style={"text-align": "center","vertical-align":"middle", "margin":"1rem","padding":"8px"}),

                    html.Hr(),


                     html.P("SENARYO 2:Dışa bağımlılık oranı istediğiniz bir değerde sabit tutarak enerji karmasının nasıl planlanması gerektiğiniz bulabilirsiniz."),

                     html.P("Elektrik üretimi için kullanılan kaynaklarda 2020 yılı itibariyle dışa bağımlılık oranı %43,6’dır."),
                            html.Table([
                              html.Tr([
                                html.Td([html.P("Lütfen planladığınız dışa bağımlılık oranını giriniz.",style={"text-align": "left","vertical-align":"middle", "margin":"1rem","padding":"2px"})],),
                                html.Td([html.P("%",style={"text-align": "right","vertical-align":"right", "margin":"1rem","padding":"8px"})]),
                                html.Td([html.Div(dcc.Input(id='input-senaryo2-on-submit', value = 0,type='text', className="form-control", style={"color": "white"} )),]),
                                html.Td([html.Button('Hesapla', id='submit-btn2-val', n_clicks=0, className = "btn btn-warning")]),
                              #   html.Div(id='container-button-basic',children='Enter a value and press submit')
                             ]),

                    ],style={"text-align": "center","vertical-align":"middle", "margin":"1rem","padding":"8px"}),

                    html.Hr(),


                     html.P("SENARYO 3:Dışa bağımlılık oranı istediğiniz bir değerde sabit tutarak enerji karmasının nasıl planlanması gerektiğiniz bulabilirsiniz."),

                     html.P("Elektrik üretimi için kullanılan kaynaklarda 2020 yılı itibariyle dışa bağımlılık oranı %43,6’dır."),
                            html.Table([
                              html.Tr([
                                html.Td([html.P("Lütfen planladığınız dışa bağımlılık oranını giriniz.",style={"text-align": "left","vertical-align":"middle", "margin":"1rem","padding":"2px"})],),
                                html.Td([html.P("%",style={"text-align": "right","vertical-align":"right", "margin":"1rem","padding":"8px"})]),
                                html.Td([html.Div(dcc.Input(id='input-senaryo3-on-submit', value = 0,type='text', className="form-control", style={"color": "white"} )),]),
                                html.Td([html.Button('Hesapla', id='submit-btn3-val', n_clicks=0, className = "btn btn-warning")]),
                              #   html.Div(id='container-button-basic',children='Enter a value and press submit')
                             ]),

                    ],style={"text-align": "center","vertical-align":"middle", "margin":"1rem","padding":"8px"}),




],className="row justify-content-md-center"),



                         
                    ],style = {'background-color' : style.cardBackColor['back'],'box-shadow': '2px 5px 5px 1px rgba(30, 47, 123, .5)',"vertical-align":"middle"})            
                ],className="col-xl-12"),
              ],className="row"),
        html.Hr(),
    ], 
)



@app.callback(
    dash.dependencies.Output('input-senaryo1-on-submit', 'value'),
    dash.dependencies.Input('submit-btn1-val', 'n_clicks'),
    dash.dependencies.Input('submit-btn2-val', 'n_clicks'),
    dash.dependencies.Input('submit-btn3-val', 'n_clicks'),
    dash.dependencies.State('input-senaryo1-on-submit', 'value'),
    dash.dependencies.State('input-senaryo2-on-submit', 'value'),
    dash.dependencies.State('input-senaryo3-on-submit', 'value'),
    )
def update_output(n_clicks1,n_clicks2,n_clicks3, value1, value2, value3):
    print(n_clicks1,n_clicks2,n_clicks3,value1,value2,value3)
    return '{}'.format(value1)