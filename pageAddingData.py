import dash_core_components as dcc
import dash_html_components as html
import style 
txtContent = """
Gelecek
"""
pageAddingData = html.Div(
    [
        html.H3("Adding Data"),
              html.Div([
                html.Div([
                    html.Div([
                         html.P(txtContent, style = {'padding':"1rem"}),
                         
                         html.Hr(),
                         html.P("Mevcut verilerle analize devam etmek istiyorum şeklinde.",style={"text-align": "center"}),


                        html.Div([
                             html.Div([
                                    html.Div([
                                        html.Div([
                                            html.P("Tüketim verilerine ekleme yapmak istiyorum",style={"text-align": "center"}),
                                            html.Button("Ekle", className = "btn btn-warning"),
                                        ], className="card-body"),
                                    ], className="card text-white bg-primary mb-3",style={"text-align": "center", "margin":"1rem"}),
                              ],className="col-m-6",),
                              html.Div([
                                    html.Div([
                                        html.Div([
                                            html.P("Enerji karması verilerine ekleme yapmak istiyorum."),
                                            html.Button("Ekle", className = "btn btn-warning"),
                                        ], className="card-body"),
                                    ], className="card text-white bg-primary mb-3", style={"text-align": "center", "margin":"1rem"}),
                              ],className="col-m-6",),
                        ],className="row justify-content-md-center"),
                    ],style = {'background-color' : style.cardBackColor['back'],'box-shadow': '2px 5px 5px 1px rgba(30, 47, 123, .5)',"vertical-align":"middle"})            
                ],className="col-xl-12"),
              ],className="row"),
        html.Hr(),
    ], 
)
