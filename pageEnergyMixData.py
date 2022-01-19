import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
# from bootdash import app
from app import app
import style
import dataGlobals

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

                             ],className="col-xl-12"),
              ],className="row"),

               html.Div([
                            html.Div([
                             
                    html.P("SENARYO 1:Dışa bağımlılık oranı istediğiniz bir değerde sabit tutarak enerji karmasının nasıl planlanması gerektiğiniz bulabilirsiniz."),
                    html.P("Elektrik üretimi için kullanılan kaynaklarda 2020 yılı itibariyle dışa bağımlılık oranı %43,6’dır."),
                            html.Table([
                              html.Tr([
                                html.Td([html.P("Lütfen planladığınız dışa bağımlılık oranını giriniz.",style={"text-align": "left","vertical-align":"middle", "margin":"10px"})],),
                                html.Td([html.P("%",style={"text-align": "right","vertical-align":"right", "margin":"1rem","padding":"8px"})]),
                                html.Td([html.Div(dcc.Input(id='input-senaryo1-on-submit', value = 0,type='text', className="form-control", style={"color": "white"} )),]),
                                html.Td([html.Button('Hesapla', id='submit-btn1-val', n_clicks=0, className = "btn btn-warning")]),

                              #   html.Div(id='container-button-basic',children='Enter a value and press submit')
                             ]),
                                 
                    ],style={"text-align": "center","vertical-align":"middle", "margin":"1rem","padding":"8px"}),
                    html.Div(id='my-outputum1'),
                    html.Hr(),

                     
                     html.P("SENARYO 2: Beklenen talebi karşılamak için hangi oranda yenilenebilir enerji kaynağı kullanılacağını belirleyerek yatırım yapılması gereken enerji karışımını belirleyebilirsiniz. "),
                     html.P("Elektrik üretimi için kullanılan kaynaklarda 2020 yılı itibariyle yenilenebilir oranı %40,51’dir."),
                            html.Table([
                              html.Tr([
                                html.Td([html.P("Lütfen planladığınız yenilenebilir enerji oranını giriniz.   ",style={"text-align": "left","vertical-align":"middle", "margin":"10px"})],),
                                html.Td([html.P("%",style={"text-align": "right","vertical-align":"right", "margin":"1rem","padding":"8px"})]),
                                html.Td([html.Div(dcc.Input(id='input-senaryo2-on-submit', value = 0,type='text', className="form-control", style={"color": "white"} )),]),
                                html.Td([html.Button('Hesapla', id='submit-btn2-val', n_clicks=0, className = "btn btn-warning")]),
                              #   html.Div(id='container-button-basic',children='Enter a value and press submit')
                             ]),
                             
                    ],style={"text-align": "center","vertical-align":"middle", "margin":"1rem","padding":"8px"}),
                    html.Div(id='my-outputum2'),
                              
                     html.Hr(),
                     html.P("SENARYO 3:Enerji arz güvenliğinin önemli göstergelerinden biri elektrik üretiminde kullanılan enerji çeşitliliğidir."),
                     html.P(" Mevcut durumda enerji çeşitliliği için hesaplanan entropi değeri 0,7533‘dür."),
                            html.Table([
                              html.Tr([
                                html.Td([html.P("Lütfen enerji çeşitliliğinin entropi değerini artırmak istediğiniz oranı giriniz. ",style={"text-align": "left","vertical-align":"middle", "margin":"10px"})],),
                                html.Td([html.P("%",style={"text-align": "right","vertical-align":"right", "margin":"1rem","padding":"8px"})]),
                                html.Td([html.Div(dcc.Input(id='input-senaryo3-on-submit', value = 0,type='text', className="form-control", style={"color": "white"} )),]),
                                html.Td([html.Button('Hesapla', id='submit-btn3-val', n_clicks=0, className = "btn btn-warning")]),
                              #   html.Div(id='container-button-basic',children='Enter a value and press submit')
                             ]),
                            
                    ],style={"text-align": "center","vertical-align":"middle", "margin":"1rem","padding":"8px"}),
                     html.Div(id='my-outputum3'),
                  ],className="row justify-content-md-center"),   
                 ],style = {'background-color' : style.cardBackColor['back'],'box-shadow': '2px 5px 5px 1px rgba(30, 47, 123, .5)',"vertical-align":"middle","padding":"30px"})            
                ],className="col-xl-12"),
              ],className="row"),
        html.Hr(),
    ], 
)

button1Tiklandi = 0
button2Tiklandi = 0
button3Tiklandi = 0

@app.callback(
    dash.dependencies.Output('my-outputum1', component_property='children'),
    dash.dependencies.Output('my-outputum2', component_property='children'),
    dash.dependencies.Output('my-outputum3', component_property='children'),
    dash.dependencies.Input('submit-btn1-val', 'n_clicks'),
    dash.dependencies.Input('submit-btn2-val', 'n_clicks'),
    dash.dependencies.Input('submit-btn3-val', 'n_clicks'),
    dash.dependencies.State('input-senaryo1-on-submit', 'value'),
    dash.dependencies.State('input-senaryo2-on-submit', 'value'),
    dash.dependencies.State('input-senaryo3-on-submit', 'value'),
    )
def update_output(n_clicks1,n_clicks2,n_clicks3, value1, value2, value3):
    print(n_clicks1,n_clicks2,n_clicks3,value1,value2,value3)

    global button1Tiklandi
    global button2Tiklandi
    global button3Tiklandi





    if n_clicks1 == 0 and n_clicks2 == 0 and n_clicks3 ==  0:
        button1Tiklandi = 0 
        button2Tiklandi = 0 
        button3Tiklandi = 0 

    if n_clicks1 > button1Tiklandi:
        dataGlobals.goalSeekingVeri1 = int(value1) / 100
        print("Button1 Tıklandı")
        button1Tiklandi += 1
        return "Değer işleme alındı","",""

    if n_clicks2 > button2Tiklandi:
        dataGlobals.goalSeekingVeri2 = int(value2) / 100
        print("Button2 Tıklandı")
        button2Tiklandi += 1
        return "","Değer işleme alındı",""

    if n_clicks3 > button3Tiklandi:
        dataGlobals.goalSeekingVeri3 = int(value3) / 100
        print("Button3 Tıklandı")
        button3Tiklandi += 1
        return "","","Değer işleme alındı"
        

    return "","",""