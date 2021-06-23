import dash_core_components as dcc
import dash_html_components as html
import style

txtContent = """
Gelecek
"""

pageAvailableData = html.Div(
    [
        html.H3("Available Data"),
              html.Div([
                html.Div([
                    html.Div([
                         html.P(txtContent, style = {'padding':"1rem"}),
                         html.Hr(),
                         html.P("Burada hangi veri kümesine eklemek yapıldığı sorularak iki seçenek sunulacak.",style = {'padding':"1rem"}),
                         html.A("İleri" , href="/page-4",style = {'padding':"1rem"}),
                    ],style = {'background-color' : style.cardBackColor['back'],'box-shadow': '2px 5px 5px 1px rgba(30, 47, 123, .5)',"vertical-align":"middle"})            
                ],className="col-xl-12"),
              ],className="row",),
        html.Hr(),
    ], 
)