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
        html.H3("PreScriptive"),
        html.Hr(),
        html.Div([
            html.Div([
                html.Div([
            
                    html.Div([
                        gauge2.gauge2
                    ],style = {'background-color' : style.cardBackColor['back'],
            'box-shadow': '2px 5px 5px 1px rgba(30, 47, 123, .5)'})
                ],)            
            ],className="col-xl-4",),
            html.Div([
                html.Div([
                    html.Div([
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
                        dcc.Graph(figure=sb.fig)
                    ],style = {'background-color' : style.cardBackColor['back'],
            'box-shadow': '2px 5px 5px 1px rgba(30, 47, 123, .5)'})
                ],)            
            ],className="col-xl-4",),
            html.Div([
                html.Div([
                    html.Div([
                           
                    ])
                ],style = {'background-color' : style.cardBackColor['back'],
            'box-shadow': '2px 5px 5px 1px rgba(30, 47, 123, .5)'})            
            ],className="col-xl-8",)
        ],className="row"),
       
    ], 
)
