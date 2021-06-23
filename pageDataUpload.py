import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import style

pageDataUpload = html.Div(
    [
        html.H3("Data Upload"),
              html.Div([
                html.Div([
                    html.Div([
                         html.P("Veri ekleme işleminden farklı olarak mevcut verilerin kullanılmayacağı tamamen yeni verilerin kullanıcı tarafından ekleneceği anlatılacak. Önceki menüye benzer şekilde iki seçenek sunulacak fakat bir de kullanıcıya veri Upload alanı verilecek. "),
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
              ],className="row"),
        html.Hr(),
    ], 
)