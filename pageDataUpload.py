import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import style

txtContent = """
Oluşturulan Karar Destek Sisteminde çok sayıda veri kullanılmakta olup, bu veriler üzerinde çok sayıda veri önişleme yöntemi uygulanmaktadır. Ayrıca uygulanan analitik yöntemlerin çoğu verinin formatına bağlı olarak çalışmaktadır. Bu sebeple yeni veri yüklenebilmesi için aşağıdaki şartların sağlanması gerekmektedir.
"""

pageDataUpload = html.Div(
    [
        html.H3("Veri yükleme"),
              html.Div([
                html.Div([
                    html.Div([
                         html.P(txtContent, style = {'padding':"1rem"}),

                         html.Ul([
                             html.Li("Zaman serisi tahmini için eklenecek veriler; yıl zaman periyodunda yer alması gerekmektedir. Teorik olarak elektrik tüketimini etkileyeceği kabul edilen sırasıyla, Elektrik tüketim miktarı, Gayri Safi yurtiçi Hâsıla (Dolar), Gayri Safi yurtiçi Hâsıla (TL) Sanayi Üretim Endeksi ve nüfus verileri içermelidir. "),
                            
                         ]),

                         html.P("Belirtilen şartları sağlayan .xls uzantılı dosyalar veri tabanına eklenirse sistem yeni yüklenen veriler üzerinde çalışacaktır.", style = {'padding':"1rem"}),
                         html.Hr(),
                         html.Div([
                             html.Div([
                                    html.Div([
                                        html.Div([
                                            html.P("",style={"text-align": "center"}),
                                                    dcc.Upload(
                                                        id='upload-data',
                                                        children=html.Div([
                                                            'Sürükle Bırak',
                                                            html.A(' Dosyaları Seç')
                                                        ]),
                                                        style={
                                                            'width': '100%',
                                                            'height': '60px',
                                                            'lineHeight': '60px',
                                                            'borderWidth': '1px',
                                                            'borderStyle': 'dashed',
                                                            'borderRadius': '5px',
                                                            'textAlign': 'center',
                                                            'margin': '10px'
                                                        },
                                                        # Allow multiple files to be uploaded
                                                        multiple=True
                                                    ),
                                                    html.Div(id='output-data-upload'),



                                        ], className="card-body"),
                                    ], className="card text-white bg-primary mb-3",style={"text-align": "center", "margin":"1rem"}),
                              ],className="col-m-12",),
                         ],className="row justify-content-md-center"),
                    ],style = {'background-color' : style.cardBackColor['back'],'box-shadow': '2px 5px 5px 1px rgba(30, 47, 123, .5)',"vertical-align":"middle"})            
                ],className="col-xl-12"),
              ],className="row",style={"height":"100vh"}),
        html.Hr(),
    ], 
)