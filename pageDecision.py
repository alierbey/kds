import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
# from bootdash import app
from app import app
import style
import w1 as w1
import numpy as np

# txtContent1 = """
# Elektrik tahmini temelde bir 

# zaman serisi problemidir. Zaman serileri ile yapılacak tahmin çalışmalarında çok sayıda yöntem kullanılabilmektedir. Her yöntemin için verilerin bir dizi ön işleme tabi tutulması gerekmektedir. Bu sebeple verilere bir dizi ön işlem uygulanarak seçtiğiniz algoritmaya uygun hale getirilecektir. Bu bölümde öncelikle tahmin problemi için belirtmeniz gereken bazı parametreler bulunmaktadır. 

# """
# txtContent2 = """
# Karar verme problemi çözümünde ise en temel gereksinimlerden biri kriterlerin ağırlıklandırılmasıdır. Kullanmakta olduğunuz Web Tabanlı Karar Destek Sistemi’nde (WTKDS) sizin seçiminizle uygulanacak Çok Kriterli Karar Verme Yöntemleri (ÇKKVY) için ağırlık belirleme süreci farklı şekillerde uygulanabilmektedir. 
# """
# txtContent3 = """
# Bu bölümde hem tahmin probleminin hem de karar probleminin çözümünde kullanılacak parametrelerin belirlenmesi gerekmektedir.
# """

pageDecision = html.Div(
    [
        html.H3("Decision"),
              html.Div([
                html.Div([
                    html.Div([
                         html.Div(html.Img(src=("assets/images/decision.jpeg"), style={"max-width":"100%", "height":"auto"})),
                    ],style = {'background-color' : style.cardBackColor['back'],'box-shadow': '2px 5px 5px 1px rgba(30, 47, 123, .5)',"vertical-align":"middle"})            
                ],className="col-xl-12"),
              ],className="row"),
        html.Hr(),
        html.Div(id='my-output'),
        html.Div([
                html.Div([
                    html.Div([
                       html.P('Tüm kriterleri eşit aralıkta kabul ederek devam etmek istiyorum', style = {"font-size": "18px", "padding": "20px", "color": "white","height":"80px", 'background-color' : "rgba(72, 82, 105)","vertical-align":"middle"}),
                        html.Div([
 html.P('Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.', style = {"font-size": "16px", "padding": "20px", "color": "white"}),
                           html.Center([
                              
html.Button('Uygula', id='submit-btn1-val', n_clicks=0 , className = "btn btn-info", style = {"margin":"20px","font-size": "18px", "color": "white", "vertical-align":"middle"})
                           ]),
                            
                         ] ),
                    ],style = {'background-color' : style.cardBackColor['back'],'box-shadow': '2px 5px 5px 1px rgba(30, 47, 123, .5)',"vertical-align":"middle"})            
                ],className="col-xl-6"),              
                    html.Div([
                        html.P('Tüm kriter ağırlıklarını ENTROPİ yöntemi ile belirlemek istiyorum.', style = {"font-size": "18px", "padding": "20px", "color": "white","height":"80px", 'background-color' : "rgba(72, 82, 105)","vertical-align":"middle"}),
                        html.Div([
                           html.P('Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.', style = {"font-size": "16px", "padding": "20px", "color": "white"}),
                         html.Center([   html.Button('Uygula', id='submit-btn2-val', n_clicks=0, className = "btn btn-info", style = {"margin":"20px","font-size": "18px", "color": "white", "vertical-align":"middle"})
                         ]),
                    ],style = {'background-color' : style.cardBackColor['back'],'box-shadow': '2px 5px 5px 1px rgba(30, 47, 123, .5)',"vertical-align":"middle"})            
                ],className="col-xl-6"),
              ],className="row"),

  html.Hr(),
               html.Div([
                html.Div([
                    html.Div([
                        html.Div([


html.P('Tüm kriter ağırlıklarını kendim girmek istiyorum.', style = {"font-size": "18px", "padding": "20px", "color": "white","height":"80px", 'background-color' : "rgba(72, 82, 105)","vertical-align":"middle"}),
                           html.Table([
                               html.Tr(
                                    [
                                   html.Td(html.P("Kriterler")),
                                    html.Td(html.P("W")),
                                    ]),
                                    html.Tr(
                                    [
                                   html.Td(html.P("Üretim")),
                                    html.Td([html.Div(dcc.Input(id='input-uretim-on-submit', value = 0, type='text', className="form-control",style={"color": "gray"} )),]),
                                    ]),
                                html.Tr([
                                   html.Td(html.P("Kurulu Güç")),
                                   html.Td([html.Div(dcc.Input(id='input-kuruluGuc-on-submit', value = 0, type='text', className="form-control",style={"color": "gray"} )),]),
                                ]),
                                html.Tr([
                                   html.Td(html.P("İşletme Ömrü")),
                                   html.Td([html.Div(dcc.Input(id='input-isletmeOmru-on-submit', value = 0, type='text', className="form-control",style={"color": "gray"} )),]),
                                ]),
                                html.Tr([
                                   html.Td(html.P("Verimlilik")),
                                   html.Td([html.Div(dcc.Input(id='input-verimlilik-on-submit', value = 0, type='text', className="form-control",style={"color": "gray"} )),]),
                                ]),
                                html.Tr([
                                   html.Td(html.P("Kapasite Faktörü")),
                                   html.Td([html.Div(dcc.Input(id='input-kapasiteFaktoru-on-submit', value = 0, type='text', className="form-control",style={"color": "gray"} )),]),
                                ]),
                                html.Tr([
                                   html.Td(html.P("Yatırım Maliyeti")),
                                   html.Td([html.Div(dcc.Input(id='input-yatirimMaliyeti-on-submit', value = 0, type='text', className="form-control",style={"color": "gray"} )),]),
                                ]),
                                html.Tr([
                                   html.Td(html.P("İşletme Maliyeti")),
                                   html.Td([html.Div(dcc.Input(id='input-isletmeMaliyeti-on-submit', value = 0, type='text', className="form-control",style={"color": "gray"} )),]),
                                ]),
                                html.Tr([
                                   html.Td(html.P("İstihdam")),
                                   html.Td([html.Div(dcc.Input(id='input-istihdam-on-submit', value = 0, type='text', className="form-control",style={"color": "gray"} )),]),
                                ]),
                                html.Tr([
                                   html.Td(html.P("Geri Ödeme Süresi")),
                                   html.Td([html.Div(dcc.Input(id='input-geriOdemeSuresi-on-submit', value = 0, type='text', className="form-control",style={"color": "gray"} )),]),
                                ]),
                                html.Tr([
                                   html.Td(
                                       html.Div(
                                      children=[
                                            html.P(['CO', html.Sub('2')])
                                         ]
                                      )
                                   ),
                                   html.Td([html.Div(dcc.Input(id='input-CO2-on-submit', value = 0, type='text', className="form-control",style={"color": "gray"} )),]),
                                ]),
                                     html.Tr([
                                   html.Td(
                                       html.Div(
                                      children=[
                                            html.P(['CO'])
                                         ]
                                      )
                                   ),
                                   html.Td([html.Div(dcc.Input(id='input-CO-on-submit', value = 0, type='text', className="form-control",style={"color": "gray"} )),]),
                                ]),
                                     html.Tr([
                                   html.Td(
                                       html.Div(
                                      children=[
                                            html.P(['NO', html.Sub('x')])
                                         ]
                                      )
                                   ),
                                   html.Td([html.Div(dcc.Input(id='input-NOX-on-submit', value = 0, type='text', className="form-control",style={"color": "gray"} )),]),
                                ]),
                                     html.Tr([
                                   html.Td(
                                       html.Div(
                                      children=[
                                            html.P(['SO', html.Sub('2')])
                                         ]
                                      )
                                   ),
                                   html.Td([html.Div(dcc.Input(id='input-SO2-on-submit', value = 0, type='text', className="form-control",style={"color": "gray"} )),]),
                                ]),
                                html.Tr([
                                   html.Td(html.P("Arazi Kullanımı")),
                                   html.Td([html.Div(dcc.Input(id='input-araziKullanimi-on-submit', value = 0, type='text', className="form-control",style={"color": "gray"} )),]),
                                ]),
                           ]),
                            html.Button('Uygula', id='submit-btn3-val', n_clicks=0, className = "btn btn-info", style = {"margin":"20px","font-size": "18px", "color": "white", "vertical-align":"middle"}),
                            html.Div(id='my-output2'),
                            
                     ] ),
                    ],style = {'background-color' : style.cardBackColor['back'],'box-shadow': '2px 5px 5px 1px rgba(30, 47, 123, .5)',"vertical-align":"middle"})            
                ],className="col-xl-6"),              
                    html.Div([
                        html.Div([
                           html.P('Tüm kriter ağırlıklarını SWARA yöntemi ile belirlemek istiyorum.', style = {"font-size": "18px", "padding": "20px", "color": "white","height":"80px", 'background-color' : "rgba(72, 82, 105)","vertical-align":"middle"}),
                              html.Table([
                               html.Tr(
                                    [
                                       html.Td(html.P("Kriterler")),
                                       html.Td(html.P("Sıra")),
                                    ]),
                                    html.Tr(
                                    [
                                       html.Td(html.P("Üretim")),
                                       html.Td([html.Div(dcc.Input(id='input-uretim-sira-on-submit', value = 0, type='text', className="form-control", style={"width":"55px","color": "gray"} )),]),
                                       html.Td(html.P(id = "my-sira1", children = "")),
                                       html.Td([html.Div(dcc.Input(id='input-sira1-on-submit', value = 0, type='text', className="form-control",style={"color": "gray"} )),]),
                                    ]),
                                html.Tr([
                                   html.Td(html.P("Kurulu Güç")),
                                   html.Td([html.Div(dcc.Input(id='input-kuruluGuc-sira-on-submit', value = 0, type='text', className="form-control", style={"width":"55px","color": "gray"} )),]),
                                   html.Td(html.P(id = "my-sira2", children = "")),
                                   html.Td([html.Div(dcc.Input(id='input-sira2-on-submit', value = 0, type='text', className="form-control",style={"color": "gray"} )),]),
                                ]),
                                html.Tr([
                                   html.Td(html.P("İşletme Ömrü")),
                                   html.Td([html.Div(dcc.Input(id='input-isletmeOmru-sira-on-submit', value = 0, type='text', className="form-control", style={"width":"55px","color": "gray"} )),]),
                                   html.Td(html.P(id = "my-sira3", children = "")),
                                   html.Td([html.Div(dcc.Input(id='input-sira3-on-submit', value = 0, type='text', className="form-control",style={"color": "gray"} )),]),
                                ]),
                                html.Tr([
                                   html.Td(html.P("Verimlilik")),
                                   html.Td([html.Div(dcc.Input(id='input-verimlilik-sira-on-submit', value = 0, type='text', className="form-control", style={"width":"55px","color": "gray"} )),]),
                                   html.Td(html.P(id = "my-sira4", children = "")),
                                   html.Td([html.Div(dcc.Input(id='input-sira4-on-submit', value = 0, type='text', className="form-control",style={"color": "gray"} )),]),
                                ]),
                                html.Tr([
                                   html.Td(html.P("Kapasite Faktörü")),
                                   html.Td([html.Div(dcc.Input(id='input-kapasiteFaktoru-sira-on-submit', value = 0, type='text', className="form-control", style={"width":"55px","color": "gray"} )),]),
                                   html.Td(html.P(id = "my-sira5", children = "")),
                                   html.Td([html.Div(dcc.Input(id='input-sira5-on-submit', value = 0, type='text', className="form-control",style={"color": "gray"} )),]),
                                ]),
                                html.Tr([
                                   html.Td(html.P("Yatırım Maliyeti")),
                                   html.Td([html.Div(dcc.Input(id='input-yatirimMaliyeti-sira-on-submit', value = 0, type='text', className="form-control", style={"width":"55px","color": "gray"} )),]),
                                   html.Td(html.P(id = "my-sira6", children = "")),
                                   html.Td([html.Div(dcc.Input(id='input-sira6-on-submit', value = 0, type='text', className="form-control",style={"color": "gray"} )),]),
                                ]),
                                html.Tr([
                                   html.Td(html.P("İşletme Maliyeti")),
                                   html.Td([html.Div(dcc.Input(id='input-isletmeMaliyeti-sira-on-submit', value = 0, type='text', className="form-control", style={"width":"55px","color": "gray"} )),]),
                                   html.Td(html.P(id = "my-sira7", children = "")),
                                   html.Td([html.Div(dcc.Input(id='input-sira7-on-submit', value = 0, type='text', className="form-control",style={"color": "gray"} )),]),
                                ]),
                                html.Tr([
                                   html.Td(html.P("İstihdam")),
                                   html.Td([html.Div(dcc.Input(id='input-istihdam-sira-on-submit', value = 0, type='text', className="form-control", style={"width":"55px","color": "gray"} )),]),
                                   html.Td(html.P(id = "my-sira8", children = "")),
                                   html.Td([html.Div(dcc.Input(id='input-sira8-on-submit', value = 0, type='text', className="form-control",style={"color": "gray"} )),]),
                                ]),
                                html.Tr([
                                   html.Td(html.P("Geri Ödeme Süresi")),
                                   html.Td([html.Div(dcc.Input(id='input-geriOdemeSuresi-sira-on-submit', value = 0, type='text', className="form-control", style={"width":"55px","color": "gray"} )),]),
                                   html.Td(html.P(id = "my-sira9", children = "")),
                                   html.Td([html.Div(dcc.Input(id='input-sira9-on-submit', value = 0, type='text', className="form-control",style={"color": "gray"} )),]),
                                ]),
                                html.Tr([
                                   html.Td(
                                       html.Div(
                                      children=[
                                            html.P(['CO', html.Sub('2')])
                                         ]
                                      )
                                   ),
                                   html.Td([html.Div(dcc.Input(id='input-CO2-sira-on-submit', value = 0, type='text', className="form-control", style={"width":"55px","color": "gray"} )),]),
                                   html.Td(html.P(id = "my-sira10", children = "")),
                                   html.Td([html.Div(dcc.Input(id='input-sira10-on-submit', value = 0, type='text', className="form-control",style={"color": "gray"} )),]),
                                ]),
                                     html.Tr([
                                   html.Td(
                                       html.Div(
                                      children=[
                                            html.P(['CO'])
                                         ]
                                      )
                                   ),
                                   html.Td([html.Div(dcc.Input(id='input-CO-sira-on-submit', value = 0, type='text', className="form-control", style={"width":"55px","color": "gray"} )),]),
                                   html.Td(html.P(id = "my-sira11", children = "")),
                                   html.Td([html.Div(dcc.Input(id='input-sira11-on-submit', value = 0, type='text', className="form-control",style={"color": "gray"} )),]),
                                ]),
                                     html.Tr([
                                   html.Td(
                                       html.Div(
                                      children=[
                                            html.P(['NO', html.Sub('x')])
                                         ]
                                      )
                                   ),
                                   html.Td([html.Div(dcc.Input(id='input-NOX-sira-on-submit', value = 0, type='text', className="form-control", style={"width":"55px","color": "gray"} )),]),
                                   html.Td(html.P(id = "my-sira12", children = "")),
                                   html.Td([html.Div(dcc.Input(id='input-sira12-on-submit', value = 0, type='text', className="form-control",style={"color": "gray"} )),]),
                                ]),
                                     html.Tr([
                                   html.Td(
                                       html.Div(
                                      children=[
                                            html.P(['SO', html.Sub('2')])
                                         ]
                                      )
                                   ),
                                   html.Td([html.Div(dcc.Input(id='input-SO2-sira-on-submit', value = 0, type='text', className="form-control", style={"width":"55px","color": "gray"} )),]),
                                   html.Td(html.P(id = "my-sira13", children = "")),
                                   html.Td([html.Div(dcc.Input(id='input-sira13-on-submit', value = 0, type='text', className="form-control",style={"color": "gray"} )),]),
                                ]),
                                html.Tr([
                                   html.Td(html.P("Arazi Kullanımı")),
                                   html.Td([html.Div(dcc.Input(id='input-araziKullanimi-sira-on-submit', value = 0, type='text', className="form-control", style={"width":"55px","color": "gray"} )),]),
                                   html.Td(html.P(id = "my-sira14", children = "")),
                                   html.Td([html.Div(dcc.Input(id='input-sira14-on-submit', value = 0, type='text', className="form-control",style={"color": "gray"} )),]),
                                ]),
                           ]),
                            html.Button('Sırala', id='submit-btn4-val', n_clicks=0, className = "btn btn-secondary", style = {"margin":"20px","font-size": "18px", "color": "white", "vertical-align":"middle"}),
                            html.Button('Uygula', id='submit-btn5-val', n_clicks=0, className = "btn btn-info", style = {"margin":"20px","font-size": "18px", "color": "white", "vertical-align":"middle"}),
                            html.Div(id='my-output3'),
                            
                     
                            
                    ],style = {'background-color' : style.cardBackColor['back'],'box-shadow': '2px 5px 5px 1px rgba(30, 47, 123, .5)',"vertical-align":"middle"})            
                ],className="col-xl-6"),
              ],className="row"),
     ], 
  )

button1Tiklandi = 0
button2Tiklandi = 0
button3Tiklandi = 0
button4Tiklandi = 0
button5Tiklandi = 0
y = {}
reelListe = []
reelListem = [i for i in range(14)]
tempListem = [i for i in range(14)]


@app.callback(
    dash.dependencies.Output('my-output', component_property='children'),
    dash.dependencies.Output('my-output2', component_property='children'),
    dash.dependencies.Output('my-output3', component_property='children'),
    dash.dependencies.Output('my-sira1', component_property='children'),
    dash.dependencies.Output('my-sira2', component_property='children'),
    dash.dependencies.Output('my-sira3', component_property='children'),
    dash.dependencies.Output('my-sira4', component_property='children'),
    dash.dependencies.Output('my-sira5', component_property='children'),
    dash.dependencies.Output('my-sira6', component_property='children'),
    dash.dependencies.Output('my-sira7', component_property='children'),
    dash.dependencies.Output('my-sira8', component_property='children'),
    dash.dependencies.Output('my-sira9', component_property='children'),
    dash.dependencies.Output('my-sira10', component_property='children'),
    dash.dependencies.Output('my-sira11', component_property='children'),
    dash.dependencies.Output('my-sira12', component_property='children'),
    dash.dependencies.Output('my-sira13', component_property='children'),
    dash.dependencies.Output('my-sira14', component_property='children'),
    dash.dependencies.Input('submit-btn1-val', 'n_clicks'),
    dash.dependencies.Input('submit-btn2-val', 'n_clicks'),
    dash.dependencies.Input('submit-btn3-val', 'n_clicks'),
    dash.dependencies.Input('submit-btn4-val', 'n_clicks'),
    dash.dependencies.Input('submit-btn5-val', 'n_clicks'),
    dash.dependencies.State('input-uretim-on-submit', 'value'),
    dash.dependencies.State('input-kuruluGuc-on-submit', 'value'),
    dash.dependencies.State('input-isletmeOmru-on-submit', 'value'),
    dash.dependencies.State('input-verimlilik-on-submit', 'value'),
    dash.dependencies.State('input-kapasiteFaktoru-on-submit', 'value'),
    dash.dependencies.State('input-yatirimMaliyeti-on-submit', 'value'),
    dash.dependencies.State('input-isletmeMaliyeti-on-submit', 'value'),
    dash.dependencies.State('input-istihdam-on-submit', 'value'),
    dash.dependencies.State('input-geriOdemeSuresi-on-submit', 'value'),
    dash.dependencies.State('input-CO2-on-submit', 'value'),
    dash.dependencies.State('input-CO-on-submit', 'value'),
    dash.dependencies.State('input-NOX-on-submit', 'value'),
    dash.dependencies.State('input-SO2-on-submit', 'value'),
    dash.dependencies.State('input-araziKullanimi-on-submit', 'value'),
    dash.dependencies.State('input-uretim-sira-on-submit', 'value'),
    dash.dependencies.State('input-kuruluGuc-sira-on-submit', 'value'),
    dash.dependencies.State('input-isletmeOmru-sira-on-submit', 'value'),
    dash.dependencies.State('input-verimlilik-sira-on-submit', 'value'),
    dash.dependencies.State('input-kapasiteFaktoru-sira-on-submit', 'value'),
    dash.dependencies.State('input-yatirimMaliyeti-sira-on-submit', 'value'),
    dash.dependencies.State('input-isletmeMaliyeti-sira-on-submit', 'value'),
    dash.dependencies.State('input-istihdam-sira-on-submit', 'value'),
    dash.dependencies.State('input-geriOdemeSuresi-sira-on-submit', 'value'),
    dash.dependencies.State('input-CO2-sira-on-submit', 'value'),
    dash.dependencies.State('input-CO-sira-on-submit', 'value'),
    dash.dependencies.State('input-NOX-sira-on-submit', 'value'),
    dash.dependencies.State('input-SO2-sira-on-submit', 'value'),
    dash.dependencies.State('input-araziKullanimi-sira-on-submit', 'value'),
    dash.dependencies.State('input-sira1-on-submit', 'value'),
    dash.dependencies.State('input-sira2-on-submit', 'value'),
    dash.dependencies.State('input-sira3-on-submit', 'value'),
    dash.dependencies.State('input-sira4-on-submit', 'value'),
    dash.dependencies.State('input-sira5-on-submit', 'value'),
    dash.dependencies.State('input-sira6-on-submit', 'value'),
    dash.dependencies.State('input-sira7-on-submit', 'value'),
    dash.dependencies.State('input-sira8-on-submit', 'value'),
    dash.dependencies.State('input-sira9-on-submit', 'value'),
    dash.dependencies.State('input-sira10-on-submit', 'value'),
    dash.dependencies.State('input-sira11-on-submit', 'value'),
    dash.dependencies.State('input-sira12-on-submit', 'value'),
    dash.dependencies.State('input-sira13-on-submit', 'value'),
    dash.dependencies.State('input-sira14-on-submit', 'value'),
    )
def update_output(n_clicks1,n_clicks2, n_clicks3, n_clicks4, n_clicks5, 
            inputUretim, 
            inputKuruluGuc, 
            inputIsletmeOmru, 
            inputVerimlilik,
            inputKapasiteFaktoru,
            inputYatirimMaliyeti,
            inputIsletmeMaliyeti,
            inputIstihdam, 
            inputGeriOdemeSuresi,
            inputCO2,
            inputCO,
            inputNOX,
            inputSO2,
            inputAraziKullanimi,
            inputUretimSira, 
            inputKuruluGucSira, 
            inputIsletmeOmruSira, 
            inputVerimlilikSira,
            inputKapasiteFaktoruSira,
            inputYatirimMaliyetiSira,
            inputIsletmeMaliyetiSira,
            inputIstihdamSira, 
            inputGeriOdemeSuresiSira,
            inputCO2Sira,
            inputCOSira,
            inputNOXSira,
            inputSO2Sira,
            inputAraziKullanimiSira,
            sira1,
            sira2,
            sira3,
            sira4,
            sira5,
            sira6,
            sira7,
            sira8,
            sira9,
            sira10,
            sira11,
            sira12,
            sira13,
            sira14
            ):
   #  print("inputUretim", inputUretim)
   #  print("inputKuruluGuc", inputKuruluGuc)
   #  print("inputIsletmeOmru", inputIsletmeOmru) 
   #  print("inputVerimlilik", inputVerimlilik)
   #  print("inputKapasiteFaktoru", inputKapasiteFaktoru)
   #  print("inputYatirimMaliyeti", inputYatirimMaliyeti)
   #  print("inputIsletmeMaliyeti", inputIsletmeMaliyeti)
   #  print("inputIstihdam",  inputIstihdam) 
   #  print("inputGeriOdemeSuresi", inputGeriOdemeSuresi)
   #  print("inputCO2", inputCO2)
   #  print("inputCO", inputCO)
   #  print("inputNOX", inputNOX)
   #  print("inputSO2", inputSO2)
   #  print("inputAraziKullanimi", inputAraziKullanimi) 
    global button1Tiklandi
    global button2Tiklandi
    global button3Tiklandi
    global button4Tiklandi
    global button5Tiklandi
    global reelListe
    global reelListem
    global tempListem

    if n_clicks1 == 0 and n_clicks2 == 0 and n_clicks3 ==  0 and n_clicks4 == 0 and n_clicks5 == 0:
        button1Tiklandi = 0 
        button2Tiklandi = 0 
        button3Tiklandi = 0 
        button4Tiklandi = 0 
        button5Tiklandi = 0 
        reelListe = []
        reelListem = [i for i in range(14)]
        tempListem = [i for i in range(14)]


    print(n_clicks1, n_clicks2)
    print(button1Tiklandi, button2Tiklandi)

    if n_clicks1 >  button1Tiklandi:
        print("Button1 Tıklandı")
        w1.secim1Uygula()
        button1Tiklandi += 1
        return 'Button 1 seçildi', "", "","","","","","","","","","","","","","",""
    

    if n_clicks2 > button2Tiklandi:
        print("Button2 Tıklandı")
        w1.secim2Uygula()
        button2Tiklandi += 1
        return 'Button 2 seçildi', "", "","","","","","","","","","","","","","",""

    if n_clicks3 > button3Tiklandi:
        print("Button3 Tıklandı")
        button3Tiklandi += 1

        w = np.array([float(inputUretim) ,float(inputKuruluGuc) , float(inputIsletmeOmru) , float(inputVerimlilik) , float(inputKapasiteFaktoru) , float(inputYatirimMaliyeti) , float(inputIsletmeMaliyeti) , float(inputIstihdam) , float(inputGeriOdemeSuresi) , float(inputCO2) , float(inputCO) , float(inputNOX) , float(inputSO2) , float(inputAraziKullanimi) ])
        
        toplam = float(inputUretim) + float(inputKuruluGuc) + float(inputIsletmeOmru) + float(inputVerimlilik) + float(inputKapasiteFaktoru) + float(inputYatirimMaliyeti) + float(inputIsletmeMaliyeti) + float(inputIstihdam) + float(inputGeriOdemeSuresi) + float(inputCO2) + float(inputCO) + float(inputNOX) + float(inputSO2) + float(inputAraziKullanimi) 


        if toplam != 1:
            print()
            return '', "Toplam 1 olması gerekiyor", "","","","","","","","","","","","","","",""
        else:
           w1.secim3Uygula(w)

    
    

    global y
   #  global reelListe
   #  global reelListem

    if n_clicks4 > button4Tiklandi:
        reelListe = []

        print("-----yeap------")
        x = {"Üretim" :  int(inputUretimSira), 
        "Kurulu Güç" : int(inputKuruluGucSira), 
        "İşletme Ömrü" : int(inputIsletmeOmruSira),
        "Verimlilik" : int(inputVerimlilikSira),
        "Kapasite Faktörü" : int(inputKapasiteFaktoruSira),
        "Yatırım Maliyeti" : int(inputYatirimMaliyetiSira),
        "İşletme Maliyeti" : int(inputIsletmeMaliyetiSira),
        "İstihdam" : int(inputIstihdamSira),
        "Geri Ödeme Süresi" : int(inputGeriOdemeSuresiSira),
        "CO2" : int(inputCO2Sira),
        "CO" : int(inputCOSira),
        "NOX" : int(inputNOXSira),
        "SO2" : int(inputSO2Sira),
        "Arazi Kullanımı" : int(inputAraziKullanimiSira)
        }

        reelListe.append(int(inputUretimSira))
        reelListe.append(int(inputKuruluGucSira))
        reelListe.append(int(inputIsletmeOmruSira))
        reelListe.append(int(inputVerimlilikSira))
        reelListe.append(int(inputKapasiteFaktoruSira))
        reelListe.append(int(inputYatirimMaliyetiSira))
        reelListe.append(int(inputIsletmeMaliyetiSira))
        reelListe.append(int(inputIstihdamSira))
        reelListe.append(int(inputGeriOdemeSuresiSira))
        reelListe.append(int(inputCO2Sira))
        reelListe.append(int(inputCOSira))
        reelListe.append(int(inputNOXSira))
        reelListe.append(int(inputSO2Sira))
        reelListe.append(int(inputAraziKullanimiSira))
        


        y = {k: v for k, v in sorted(x.items(), key=lambda item: item[1])}
        print(y)
        print(type(y))
        print(list(y)[0])
        
      # reelListe.add(inputUretimSira)
        

        print(reelListe)
        print("Button4 Tıklandı")
        button4Tiklandi += 1
        return "", ""," Veriler Sıralandı ", list(y)[0], list(y)[1], list(y)[2], list(y)[3],list(y)[4], list(y)[5], list(y)[6], list(y)[7],list(y)[8], list(y)[9], list(y)[10], list(y)[11],list(y)[12], list(y)[13],
        #return "","","","","","","","","","","","","","","",""
      
   
    
        
    
    if n_clicks5 > button5Tiklandi:
         print("Button 5 Tıklandı")
         print(reelListe)

         tempListem[0] = float(sira1)
         tempListem[1] = float(sira2)
         tempListem[2] = float(sira3)
         tempListem[3] = float(sira4)
         tempListem[4] = float(sira5)
         tempListem[5] = float(sira6)
         tempListem[6] = float(sira7)
         tempListem[7] = float(sira8)
         tempListem[8] = float(sira9)
         tempListem[9] = float(sira10)
         tempListem[10] = float(sira11)
         tempListem[11] = float(sira12)
         tempListem[12] = float(sira13)
         tempListem[13] = float(sira14)


    
         w1.secim4Uygula(np.array(tempListem), reelListe)

         # for i in range(14):
         #    reelListem[i] = tempListem[reelListe[i]-1]

        
         print(reelListem)

         button5Tiklandi += 1
         return "", "", " Değerler Atandı ", list(y)[0], list(y)[1], list(y)[2], list(y)[3],list(y)[4], list(y)[5], list(y)[6], list(y)[7],list(y)[8], list(y)[9], list(y)[10], list(y)[11],list(y)[12], list(y)[13],
   

    return "","","","","","","","","","","","","","","","",""





 