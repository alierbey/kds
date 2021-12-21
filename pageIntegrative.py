###################### PRESCRIPTIVE graf-3 ######################
import dash_html_components as html
import dash_bootstrap_components as dbc
import dash_core_components as dcc

import plotly.io as pio
import sc3



import style

pageIntegrative = html.Div(
    [
        html.H3("Integrative"),
        html.Hr(),
        html.Div([
            html.Div([
                html.Div([
                    html.Div([
                       dcc.Graph(figure=sc3.fig)

                    ])
                ],style = {'background-color' : style.cardBackColor['back'],
            'box-shadow': '2px 5px 5px 1px rgba(30, 47, 123, .5)'})            
            ],className="col-xl-12",),
            html.Div([
                html.Div([
                    html.Div([
                      
                        
                    ])
                ],style = {'background-color' : style.cardBackColor['back'],
            'box-shadow': '2px 5px 5px 1px rgba(30, 47, 123, .5)'})            
            ],className="col-xl-4",),
             html.Div([
                html.Div([
                    html.Div([
                             
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
                           html.H5("Verimlilik ", style = {"padding-top":20, "text-align":"center"}),
                           
                    ]),
                ],style = {'background-color' : style.cardBackColor['back'],
            'box-shadow': '2px 5px 5px 1px rgba(30, 47, 123, .5)'}),          
            ],className="col-xl-6",),
            html.Div([
                html.Div([
                    html.Div([
                      
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
                           
                    ]),
                ],style = {'background-color' : style.cardBackColor['back'],
            'box-shadow': '2px 5px 5px 1px rgba(30, 47, 123, .5)'}),          
            ],className="col-xl-6",),
            html.Div([
                html.Div([
                    html.Div([
                      
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
                    
                    ]),
                ],style = {'background-color' : style.cardBackColor['back'],
            'box-shadow': '2px 5px 5px 1px rgba(30, 47, 123, .5)'}),          
            ],className="col-xl-6",),
            html.Div([
                html.Div([
                    html.Div([
                      
                    ])
                ],style = {'background-color' : style.cardBackColor['back'],
            'box-shadow': '2px 5px 5px 1px rgba(30, 47, 123, .5)'})            
            ],className="col-xl-6",),
            
        ],className="row"),
        
       
    ], 
)
