import dash_html_components as html
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import bullet as bl
import sunburst
import table3 
# import electric
import prs_gauge2
import plotly.io as pio

import style

import prs_card1
import prs_card2
import prs_card3
import prs_card4
import prs_gauge3
import prs_gauge4
import prs_pie2
import prs_bar4
import prs_bar2
import pred_tuketim2

import pageIntegrative4
import pageIntegrativeCard3
import pageIntegrative6
import pageIntegrative7
import pageIntegrative8
import pageIntegrative9
import style
import dataGlobals as dataGlobal



pageScriptive = html.Div(
    [
        html.H3("Prescriptive"),
        html.Hr(),
        html.Div([
            html.Div([
                html.Div([
            
                    html.Div([
                        html.H6("Elektrik Tüketiminde Yıllık Değişim (%)", style = {"padding":20, "text-align":"center"}),
                        prs_gauge2.gauge2
                    ],style = {'background-color' : style.cardBackColor['back'], "padding-bottom": 40,
            'box-shadow': '2px 5px 5px 1px rgba(30, 47, 123, .5)'})
                ],)            
            ],className="col-xl-4",),
            html.Div([
                html.Div([
                    html.Div([
                        
                        html.H6("Elektrik Talep Tahmini", style = {"padding-top":20, "text-align":"center"}),
                          pred_tuketim2.fig
                            #dcc.Graph(figure=electric.fig)
                    ])
                ],style = {'background-color' : style.cardBackColor['back'],
            'box-shadow': '2px 5px 5px 1px rgba(30, 47, 123, .5)'})            
            ],className="col-xl-8",)
        ],className="row"),
         html.Br(),
         html.Div([
            html.Div([
                html.Div([
            
                    html.Div([
                        
                        #yeap
                        html.H6(" Kriter Ağırlıkları ", style = {"padding-top":20, "text-align":"center"}),
                        
                        sunburst.fig
                        
                        # dcc.Graph(figure=sb.fig)
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
            'box-shadow': '2px 5px 5px 1px rgba(30, 47, 123, .5)', "padding-bottom":17})            
            ],className="col-xl-6",)
        ],className="row"),
        #   html.Hr(),
        #  html.Div([
        #     html.Div([
        #         html.Div([
            
        #             html.Div([
                       
        #                  html.H5(" Kriter Ağırlıkları ", style = {"padding-top":20, "text-align":"center"}),
        #                 dcc.Graph(figure=sb.fig)
        #             ],style = {'background-color' : style.cardBackColor['back'],
        #     'box-shadow': '2px 5px 5px 1px rgba(30, 47, 123, .5)'})
        #         ],)            
        #     ],className="col-xl-4",),
        #     html.Div([
        #         html.Div([
        #             html.Div([
                           
        #             ])
        #         ])            
        #     ],className="col-xl-8",)
        # ],className="row"),
    html.Br(),
         html.Div([
            html.Div([
                html.Div([
                    html.Div([
                    #    dcc.Graph(figure=pageIntegrativeCard1.fig)
                    prs_card1.fig
                   

                    ])
                ],style = {'background-color' : style.cardBackColor['back'],
            'box-shadow': '2px 5px 5px 1px rgba(30, 47, 123, .5)'})            
            ],className="col-xl-4",),
            html.Div([
                html.Div([
                    html.Div([
                      
                        # dcc.Graph(figure=pageIntegrativeCard2.fig)
                        #  dcc.Graph(figure= prs_card2.fig)
                         prs_card2.fig
                    ])
                ],style = {'background-color' : style.cardBackColor['back'],
            'box-shadow': '2px 5px 5px 1px rgba(30, 47, 123, .5)'})            
            ],className="col-xl-4",),
             html.Div([
                html.Div([
                    html.Div([
                            #  dcc.Graph(figure=pageIntegrativeCard3.fig)
                            #   dcc.Graph(figure= prs_card3.fig)
                              prs_card3.fig
                    ])
                ],style = {'background-color' : style.cardBackColor['back'],
            'box-shadow': '2px 5px 5px 1px rgba(30, 47, 123, .5)'})            
            ],className="col-xl-4",)
        ],className="row"),
        html.Br(),
                html.Div([
            html.Div([
                html.Div([
                    html.Div([
                           html.H6("Kurulu Güç Bazında Verimlilik ", style = {"padding-top":20, "text-align":"center"}),
                           dcc.Graph(figure=prs_gauge3.fig)
                        #    prs_gauge3.fig
                       
                    ]),
                ],style = {'background-color' : style.cardBackColor['back'],
            'box-shadow': '2px 5px 5px 1px rgba(30, 47, 123, .5)'}),          
            ],className="col-xl-6",),
            html.Div([
                html.Div([
                    html.Div([
                    #   dcc.Graph(figure=pageIntegrative4.fig)
                   
                     html.H6("Santral Türlerine Göre İstihdama Katkı", style = {"padding-top":20, "text-align":"center"}),
                    prs_bar2.fig 
                    ])
                ],style = {'background-color' : style.cardBackColor['back'],
            'box-shadow': '2px 5px 5px 1px rgba(30, 47, 123, .5)' ,"padding-bottom":0})            
            ],className="col-xl-6",)
        ],className="row"),
        html.Br(),
        html.Div([
            html.Div([
                html.Div([
                    html.Div([
                        #    dcc.Graph(figure=pageIntegrative6.fig)
                        prs_bar4.fig
                    ]),
                ],style = {'background-color' : style.cardBackColor['back'],
            'box-shadow': '2px 5px 5px 1px rgba(30, 47, 123, .5)'}),          
            ],className="col-xl-6",),
            html.Div([
                html.Div([
                    html.Div([
                    #   dcc.Graph(figure=pageIntegrative7.fig) 
                    # dcc.Graph(figure=prs_gauge4.fig)
                    # prs_gauge4.fig 
                    

                       html.H6("Elektrik Üretiminde Planlanan Değişim", style = {"padding":20, "text-align":"center"}),
                       
                        dcc.Graph(figure=bl.fig)

                    ])
                ],style = {'background-color' : style.cardBackColor['back'],
            'box-shadow': '2px 5px 5px 1px rgba(30, 47, 123, .5)'})            
            ],className="col-xl-6",)
        ],className="row"),
       
          html.Br(),
        html.Div([
            html.Div([
                html.Div([
                   prs_pie2.fig
                ],style = {'background-color' : style.cardBackColor['back'],
            'box-shadow': '2px 5px 5px 1px rgba(30, 47, 123, .5)'})            
            ],className="col-xl-12",),
            
        ],className="row"),
       
    ], 
)
