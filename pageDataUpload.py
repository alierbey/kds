import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import style

txtContent = """
Oluşturulan Karar Destek Sisteminde çok sayıda veri kullanılmakta olup, bu veriler üzerinde çok sayıda veri önişleme yöntemi uygulanmaktadır. Ayrıca uygulanan analitik yöntemlerin çoğu verinin formatına bağlı olarak çalışmaktadır. Bu sebeple yeni veri yüklenebilmesi için aşağıdaki şartların sağlanması gerekmektedir. 
"""

pageDataUpload = html.Div(
    [
        html.H3("Data Upload"),
              html.Div([
                html.Div([
                    html.Div([
                         html.P(txtContent, style = {'padding':"1rem"}),

                         html.Ul([
                             html.Li("Zaman serisi tahmini için eklenecek veriler; ay zaman periyodunda yer alması, elektrik tüketim miktarı, Gayri Safi yurtiçi Hâsıla, Sanayi Üretim Endeksi gibi teorik olarak elektrik tüketimini etkileyecek verileri içermelidir. "),
                             html.Li("Santral seçimi için eklenecek veriler; Kurulu güç, Yıllık üretim miktarı, Kapasite faktörü, Yatırım maliyetleri, İşletme ve bakım maliyetleri, Yakıt maliyetleri, Geri ödeme süresi, CO2, CH4, NOX ve SO2 Emisyonları, Arazi kullanımı, İstihdam oluşturma potansiyeli gibi teorik olarak santral seçimini etkileyen verileri içermelidir."),
                         ]),

                         html.P("Belirtilen şartları sağlayan .xls uzantılı dosyalar veri tabanına eklenirse sistem yeni yüklenen veriler üzerinde çalışacaktır. ", style = {'padding':"1rem"}),
                         html.Hr(),
                         html.Div([
                             html.Div([
                                    html.Div([
                                        html.Div([
                                            html.P("Tüketim verilerine ekleme yapmak istiyorum",style={"text-align": "center"}),
                                                    dcc.Upload(
                                                        id='upload-data',
                                                        children=html.Div([
                                                            'Drag and Drop or ',
                                                            html.A('Select Files')
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