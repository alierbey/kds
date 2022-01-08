import dash_html_components as html
import style
import gauge2
import makroDegiskenler
import makroDegiskenlerIleTuketimKorelasyonlari
import kriterDegerlendirmesi
import barchart



pageDescriptive = html.Div(
    [
            html.H3("Descriptive"),
                html.Div([
                    html.Div([
                         html.Div([
                       # Makro Degiskenler ile Tuketim Korelasyonlari
                       makroDegiskenlerIleTuketimKorelasyonlari.makroDegiskenlerIleTuketimKorelasyonlari
                            ], style = {'background-color' : style.cardBackColor['back'],'box-shadow': '2px 5px 5px 1px rgba(30, 47, 123, .5)',"margin":"1rem"})            
                ],className="col-xl-4"),
                html.Div([
                        html.Div([
                       # Makro degiskenler gelecek
                            makroDegiskenler.grafMakroDegiskenler
                        ],style = {'background-color' : style.cardBackColor['back'], 'box-shadow': '2px 5px 5px 1px rgba(30, 47, 123, .5)',"margin":"1rem"})            
                ],className="col-xl-8",)
            ],className="row"),
            html.Hr(),

            html.Div([
                    html.Div([
                         html.Div([
                       # yeni grafik
                            barchart.grafKisiBasi
                            ], style = {'background-color' : style.cardBackColor['back'],'box-shadow': '2px 5px 5px 1px rgba(30, 47, 123, .5)',"margin":"1rem"})            
                ],className="col-xl-6"),
                html.Div([
                        html.Div([
                       # Makro degiskenler gelecek
                            kriterDegerlendirmesi.grafkriterDegerlendirmesi
                        ],style = {'background-color' : style.cardBackColor['back'], 'box-shadow': '2px 5px 5px 1px rgba(30, 47, 123, .5)',"margin":"1rem"})            
                ],className="col-xl-6",)
            ],className="row"),

            html.Hr(),
            html.Div([
                html.Div([
                    html.Div([
                                html.Div([
                                    html.H6("Elektrik Tüketiminde Yıllık Değişim Hızı", style = {"padding-top":20, "text-align":"center"}),
                                    gauge2.gauge2
                                ],style = {"margin":"1rem"})
                    ],style = {'background-color' : style.cardBackColor['back'],
            'box-shadow': '2px 5px 5px 1px rgba(30, 47, 123, .5)'})            
                ],className="col-xl-7",),
                html.Hr(),
                html.Div([
                    html.Div([
                        # kriter değerlendirmesi gelecek
                        
                    ],style = {'background-color' : style.cardBackColor['back'],
            'box-shadow': '2px 5px 5px 1px rgba(30, 47, 123, .5)'})            
                ],className="col-xl-5",)
            ],className="row"),
            html.Hr(),
    ], 
)






