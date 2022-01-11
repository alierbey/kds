import dash_html_components as html

import dash_bootstrap_components as dbc
import dash_core_components as dcc
import style
import gauge2
import makroDegiskenler
import makroDegiskenlerIleTuketimKorelasyonlari
import kriterDegerlendirmesi
import barchart
import desc_card1
import desc_card2
import desc_pie1
import desc_pie2
import descUretim
import descUretim1


pageDescriptive = html.Div(
    [
            html.H3("Descriptive"),
                html.Div([
                    html.Div([
                         html.Div([
                       # Makro Degiskenler ile Tuketim Korelasyonlari
                       makroDegiskenlerIleTuketimKorelasyonlari.makroDegiskenlerIleTuketimKorelasyonlari
                            ], style = {'background-color' : style.cardBackColor['back'],'box-shadow': '2px 5px 5px 1px rgba(30, 47, 123, .5)',"margin":"1rem","padding":"20px"})            
                ],className="col-xl-4"),
                html.Div([
                        html.Div([
                       # Makro degiskenler gelecek
                            makroDegiskenler.grafMakroDegiskenler
                        ],style = {'background-color' : style.cardBackColor['back'], 'box-shadow': '2px 5px 5px 1px rgba(30, 47, 123, .5)',"margin":"1rem","padding":"20px"})            
                ],className="col-xl-8",)
            ],className="row"),
            html.Hr(),

            html.Div([
                    html.Div([
                         html.Div([
                       # yeni grafik
                            barchart.grafKisiBasi
                            ], style = {'background-color' : style.cardBackColor['back'],'box-shadow': '2px 5px 5px 1px rgba(30, 47, 123, .5)',"margin":"1rem","padding":"20px"})            
                ],className="col-xl-12"),
                
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
                ],className="col-xl-5",),
            
                html.Div([
                    html.Div([
                        # kriter değerlendirmesi gelecek
                            kriterDegerlendirmesi.grafkriterDegerlendirmesi
                    ],style = {'background-color' : style.cardBackColor['back'],
            'box-shadow': '2px 5px 5px 1px rgba(30, 47, 123, .5)'})            
                ],className="col-xl-7",)
            ],className="row"),
            
           



            html.Div([
                    html.Div([
                         html.Div([
                       # Makro Degiskenler ile Tuketim Korelasyonlari
                        dcc.Graph(figure=desc_card1.fig)
                            ], style = {'background-color' : style.cardBackColor['back'],'box-shadow': '2px 5px 5px 1px rgba(30, 47, 123, .5)',"margin":"1rem","padding":"20px"})            
                ],className="col-xl-5"),
                html.Div([
                        html.Div([
                       # Makro degiskenler gelecek
                            dcc.Graph(figure=desc_pie1.fig)
                        ],style = {'background-color' : style.cardBackColor['back'], 'box-shadow': '2px 5px 5px 1px rgba(30, 47, 123, .5)',"margin":"1rem","padding":"20px"})            
                ],className="col-xl-7",)
            ],className="row"),

            html.Div([
                    html.Div([
                         html.Div([
                       # Makro Degiskenler ile Tuketim Korelasyonlari
                       dcc.Graph(figure=desc_pie2.fig)
                        
                            ], style = {'background-color' : style.cardBackColor['back'],'box-shadow': '2px 5px 5px 1px rgba(30, 47, 123, .5)',"margin":"1rem","padding":"20px"})            
                ],className="col-xl-7"),
                html.Div([
                        html.Div([
                       # Makro degiskenler gelecek
                            dcc.Graph(figure=desc_card2.fig)
                        ],style = {'background-color' : style.cardBackColor['back'], 'box-shadow': '2px 5px 5px 1px rgba(30, 47, 123, .5)',"margin":"1rem","padding":"20px"})            
                ],className="col-xl-5",)
            ],className="row"),

            #  html.Div([
            #         html.Div([
            #              html.Div([
            #            # Makro Degiskenler ile Tuketim Korelasyonlari
            #            dcc.Graph(figure=descUretim.fig)
                        
            #                 ], style = {'background-color' : style.cardBackColor['back'],'box-shadow': '2px 5px 5px 1px rgba(30, 47, 123, .5)',"margin":"1rem","padding":"20px"})            
            #     ],className="col-xl-7"),
            #     html.Div([
            #             html.Div([
            #            # Makro degiskenler gelecek
            #                 dcc.Graph(figure=descUretim1.fig)
            #             ],style = {'background-color' : style.cardBackColor['back'], 'box-shadow': '2px 5px 5px 1px rgba(30, 47, 123, .5)',"margin":"1rem","padding":"20px"})            
            #     ],className="col-xl-5",)
            # ],className="row"),
            
    ], 
)






