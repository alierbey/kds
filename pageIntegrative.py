###################### PRESCRIPTIVE graf-3 ######################
import dash_html_components as html
import dash_bootstrap_components as dbc
import dash_core_components as dcc

import plotly.io as pio


import pageIntegrativeCard1
import pageIntegrative2
import pageIntegrativeCard2
import pageIntegrative4
import pageIntegrativeCard3
import pageIntegrative6
import pageIntegrative7
import pageIntegrative8
import pageIntegrative9
import style

pageIntegrative = html.Div(
    [
        html.H3("Integrative"),
        html.Hr(),
        html.Div([
            html.Div([
                html.Div([
                    html.Div([
                       dcc.Graph(figure=pageIntegrativeCard1.fig)

                    ])
                ],style = {'background-color' : style.cardBackColor['back'],
            'box-shadow': '2px 5px 5px 1px rgba(30, 47, 123, .5)'})            
            ],className="col-xl-4",),
            html.Div([
                html.Div([
                    html.Div([
                        
                        dcc.Graph(figure=pageIntegrativeCard2.fig)
                    ])
                ],style = {'background-color' : style.cardBackColor['back'],
            'box-shadow': '2px 5px 5px 1px rgba(30, 47, 123, .5)'})            
            ],className="col-xl-4",),
             html.Div([
                html.Div([
                    html.Div([
                             dcc.Graph(figure=pageIntegrativeCard3.fig)
                    ])
                ],style = {'background-color' : style.cardBackColor['back'],
            'box-shadow': '2px 5px 5px 1px rgba(30, 47, 123, .5)'})            
            ],className="col-xl-4",)
        ],className="row"),
        html.Hr(),
                html.Div([
            html.Div([
                html.Div([
                    html.Div([
                           dcc.Graph(figure=pageIntegrative2.fig)
                    ]),
                ],style = {'background-color' : style.cardBackColor['back'],
            'box-shadow': '2px 5px 5px 1px rgba(30, 47, 123, .5)'}),          
            ],className="col-xl-6",),
            html.Div([
                html.Div([
                    html.Div([
                      dcc.Graph(figure=pageIntegrative4.fig) 
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
                           dcc.Graph(figure=pageIntegrative6.fig)
                    ]),
                ],style = {'background-color' : style.cardBackColor['back'],
            'box-shadow': '2px 5px 5px 1px rgba(30, 47, 123, .5)'}),          
            ],className="col-xl-6",),
            html.Div([
                html.Div([
                    html.Div([
                      dcc.Graph(figure=pageIntegrative7.fig) 
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
                    dcc.Graph(figure=pageIntegrative8.fig)
                    ]),
                ],style = {'background-color' : style.cardBackColor['back'],
            'box-shadow': '2px 5px 5px 1px rgba(30, 47, 123, .5)'}),          
            ],className="col-xl-6",),
            html.Div([
                html.Div([
                    html.Div([
                      dcc.Graph(figure=pageIntegrative9.fig) 
                    ])
                ],style = {'background-color' : style.cardBackColor['back'],
            'box-shadow': '2px 5px 5px 1px rgba(30, 47, 123, .5)'})            
            ],className="col-xl-6",),
            
        ],className="row"),
        
       
    ], 
)
