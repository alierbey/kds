import dash_html_components as html
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import style
import pred_table1
import pred_tuketim
import pred_sue
import pred_nufus
import pred_gsd
import pred_gstl


pagePredictive = html.Div(
    [
            html.H3("öngörücü"),
                html.Div([
                    html.Div([
                         html.Div([
                               pred_tuketim.fig
                                       ], style = {'background-color' : style.cardBackColor['back'],'box-shadow': '2px 5px 5px 1px rgba(30, 47, 123, .5)',"margin":"1rem","padding":"20px"})            
                ],className="col-xl-12"),
            ],className="row"),

             html.Div([
                    html.Div([
                         html.Div([
                               pred_sue.fig
                                       ], style = {'background-color' : style.cardBackColor['back'],'box-shadow': '2px 5px 5px 1px rgba(30, 47, 123, .5)',"margin":"1rem","padding":"20px"})            
                ],className="col-xl-12"),
            ],className="row"),
            html.Div([
                    html.Div([
                         html.Div([
                               pred_nufus.fig
                                       ], style = {'background-color' : style.cardBackColor['back'],'box-shadow': '2px 5px 5px 1px rgba(30, 47, 123, .5)',"margin":"1rem","padding":"20px"})            
                ],className="col-xl-12"),
            ],className="row"),

             html.Div([
                    html.Div([
                         html.Div([
                               pred_gsd.fig
                                       ], style = {'background-color' : style.cardBackColor['back'],'box-shadow': '2px 5px 5px 1px rgba(30, 47, 123, .5)',"margin":"1rem","padding":"20px"})            
                ],className="col-xl-12"),
            ],className="row"),
            html.Div([
                    html.Div([
                         html.Div([
                               pred_gstl.fig
                                       ], style = {'background-color' : style.cardBackColor['back'],'box-shadow': '2px 5px 5px 1px rgba(30, 47, 123, .5)',"margin":"1rem","padding":"20px"})            
                ],className="col-xl-12"),
            ],className="row"),
    


            html.Div([
            
                html.Div([
                        html.Div([
                       # Makro degiskenler gelecek
                            dcc.Graph(figure=pred_table1.fig)
                            
                        ],style = {'background-color' : style.cardBackColor['back'], 'box-shadow': '2px 5px 5px 1px rgba(30, 47, 123, .5)',"margin":"1rem","padding":"20px"})            
                ],className="col-xl-12",)
            ],className="row"),

         

            
    ], 
)






