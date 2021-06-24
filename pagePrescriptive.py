###################### PRESCRIPTIVE graf-3 ######################
import dash_html_components as html
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import bullet as bl
import sunburst as sb
import table3 
import electric
import gauge2
import plotly.io as pio

import style

pageScriptive = html.Div(
    [
        html.H3("Prescriptive"),
        html.Hr(),
        html.Div([
            html.Div([
                html.Div([
            
                    html.Div([
                        html.H5("Elektrik Tüketiminde Yıllık Değişim Hızı", style = {"padding-top":20, "text-align":"center"}),
                        gauge2.gauge2
                    ],style = {'background-color' : style.cardBackColor['back'],
            'box-shadow': '2px 5px 5px 1px rgba(30, 47, 123, .5)'})
                ],)            
            ],className="col-xl-4",),
            html.Div([
                html.Div([
                    html.Div([
                        
                        html.H5("Elektrik Tüketim Tahmini", style = {"padding-top":20, "text-align":"center"}),
                            dcc.Graph(figure=electric.fig)
                    ])
                ],style = {'background-color' : style.cardBackColor['back'],
            'box-shadow': '2px 5px 5px 1px rgba(30, 47, 123, .5)'})            
            ],className="col-xl-8",)
        ],className="row"),
         html.Hr(),
         html.Div([
            html.Div([
                html.Div([
            
                    html.Div([
                        
                          html.H5("Elektrik Üretiminde Planlanan Değişim", style = {"padding-top":20, "text-align":"center"}),
                        dcc.Graph(figure=bl.fig)
                    ],style = {'background-color' : style.cardBackColor['back'],
            'box-shadow': '2px 5px 5px 1px rgba(30, 47, 123, .5)'})
                ],)            
            ],className="col-xl-6",),
            html.Div([
                html.Div([
                    html.Div([
                           table3.table3
                    ])
                ],style = {'background-color' : style.cardBackColor['back'],
            'box-shadow': '2px 5px 5px 1px rgba(30, 47, 123, .5)'})            
            ],className="col-xl-6",)
        ],className="row"),
          html.Hr(),
         html.Div([
            html.Div([
                html.Div([
            
                    html.Div([
                       
                         html.H5(" Kriter Ağırlıkları ", style = {"padding-top":20, "text-align":"center"}),
                        dcc.Graph(figure=sb.fig)
                    ],style = {'background-color' : style.cardBackColor['back'],
            'box-shadow': '2px 5px 5px 1px rgba(30, 47, 123, .5)'})
                ],)            
            ],className="col-xl-4",),
            html.Div([
                html.Div([
                    html.Div([
                           
                    ])
                ])            
            ],className="col-xl-8",)
        ],className="row"),
       
    ], 
)
