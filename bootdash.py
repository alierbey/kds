import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options
df = pd.DataFrame({
    "Fruit": ["Apples", "Oranges", "Bananas", "Apples", "Oranges", "Bananas"],
    "Amount": [4, 1, 2, 2, 4, 5],
    "City": ["SF", "SF", "SF", "Montreal", "Montreal", "Montreal"]
})

fig = px.bar(df, x="Fruit", y="Amount", color="City", barmode="group")

app.layout = html.Div(children=[
    html.H1(children='Hello Dash'),

    html.Div(children='''
        Dash: A web application framework for Python.
    '''),

    dcc.Graph(
        id='example-graph',
        figure=fig
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)



# import dash
# import dash_bootstrap_components as dbc
# import dash_core_components as dcc
# import dash_html_components as html
# from dash.dependencies import Input, Output
# import plotly.graph_objects as go
# import pandas as pd
# import numpy as np
# import plotly.express as px
# from scipy import stats
# import scipy as sp
# from plotly.subplots import make_subplots
# import numpy as np
# import plotly.io as pio
# import plotly.express as px

# pio.templates.default = "plotly_dark"

# app = dash.Dash(external_stylesheets=[dbc.themes.DARKLY])

# # df = pd.read_excel("veri1.xlsx")
# # df['Tarih']=df['Tarih'].dt.year
# # df_tarih = df.groupby('Tarih')



# fig = go.Figure()

# ###### pie #####

# # the style arguments for the sidebar. We use position:fixed and a fixed width
# SIDEBAR_STYLE = {
#     "position": "fixed",
#     "top": 0,
#     "left": 0,
#     "bottom": 0,
#     "width": "16rem",
#     "padding": "2rem 1rem",
#     "background-color": "#030303",
# }

# # the styles for the main content position it to the right of the sidebar and
# # add some padding.
# CONTENT_STYLE = {
#     "margin-left": "15rem",
#     "margin-right": "2rem",
#     "padding": "2rem 1rem",
#     "background-color": "#2A1D33",
   
# }

# colors = {
#     'background': '#111111',
#     'text': '#7FDBFF'
# }



# sidebar = html.Div(
#     [
#         html.H2("KDS", className="display-4"),
#         html.Hr(),
#         html.P(
#             "Karar Destek Sistemleri"
#         ),
#         dbc.Nav(
#             [
#                 dbc.NavLink("Home", href="/", active="exact"),
#                 dbc.NavLink("Descriptive", href="/page-1", active="exact"),
#                 dbc.NavLink("Integrative", href="/page-2", active="exact"),
#                 dbc.NavLink("Predictive", href="/page-3", active="exact"),
#                 dbc.NavLink("Prescriptive", href="/page-3", active="exact"),
           
#             ],
#             vertical=True,
#             pills=True,
#         ),
#     ],
#     style=SIDEBAR_STYLE,
# )



# yeni = html.Div(
#     [
#         html.H3("Descriptive"),
#         html.Div([
#                             html.Div([
#                                 html.Div([
                                    
#                                 ],className="card-header")            
#                             ],className="col-xl-4"),
                     

#                     html.Div([
#                         html.Div([
#                             html.Div([
                                   
#                             ])
#                         ],className="card-header",)            
#                     ],className="col-xl-8",)
                    

#                 ],className="row"),

#  html.Hr(),
#               html.Div([
#   html.Div([
#   html.Div([
          
#       html.Div([

    
# ])
      
#         ],
#         className="card-header",)            
#         ],
#         className="col-xl-7",),
#          html.Div([
#   html.Div([
#        html.Div([
   
   
#     html.Hr(),
   
# ])
#         ],
#         className="card-header",)            
#         ],
#         className="col-xl-5",)
#         ],
#         className="row"
        
#         ),
#         html.Hr(),
#     ],
    
# )

# content = html.Div(id="page-content", style=CONTENT_STYLE)

# app.layout = html.Div([dcc.Location(id="url"), sidebar, content])


# @app.callback(Output("page-content", "children"), [Input("url", "pathname")])
# def render_page_content(pathname):
#     if pathname == "/":
#         return yeni
#     elif pathname == "/page-1":
#         return html.P("This is the content of page 1. Yay!")
#     elif pathname == "/page-2":
#         return html.P("Oh cool, this is page 2!")
#     # If the user tries to reach a different page, return a 404 message
#     return dbc.Jumbotron(
#         [
#             html.H1("404: Not found", className="text-danger"),
#             html.Hr(),
#             html.P(f"The pathname {pathname} was not recognised..."),
#         ]
#     )

# # @app.callback(
# #     Output("time-series-chart", "figure"), 
# #     [Input("ticker", "value")])
# # def display_time_series(ticker):
# #     print(ticker)
# #     #fig = px.line(df, x='Tarih', y=ticker, template="plotly_dark")
# #     X = np.array(df['Tuketim'])
# #     y = np.array(df[ticker])
# #     r = sp.stats.pearsonr(X, y) 

# #     fig = go.Figure(go.Indicator(
# #     mode = "number+gauge+delta",
# #     gauge = {'shape': "bullet"},
# #     delta = {'reference': 300},
# #     value = r[0]*100,
# #     domain = {'x': [0.1, 1], 'y': [0.2, 0.9]},
# #     title = {'text': "Avg order size"}))
# #     return fig


# # @app.callback(
# #     Output("time-series-chart2", "figure"), 
# #     [Input("ticker2", "value")])
# # def display_time_series(ticker):
# #     print(ticker)
# #     #fig = px.line(df, x='Tarih', y=ticker, template="plotly_dark")
# #     X = np.array(df['Tuketim'])
# #     y = np.array(df[ticker])
# #     r = sp.stats.pearsonr(X, y) 

# #     fig = go.Figure(go.Indicator(
# #     mode = "number+gauge+delta",
# #     gauge = {'shape': "bullet"},
# #     delta = {'reference': 300},
# #     value = r[0]*100,
# #     domain = {'x': [0.1, 1], 'y': [0.2, 0.9]},
# #     title = {'text': "Avg order size"}))
# #     return fig

# # @app.callback(
# #     Output("time-series-chart3", "figure"), 
# #     [Input("ticker3", "value")])
# # def display_time_series(ticker):
# #     print(ticker)
# #     #fig = px.line(df, x='Tarih', y=ticker, template="plotly_dark")
# #     X = np.array(df['Tuketim'])
# #     y = np.array(df[ticker])
# #     r = sp.stats.pearsonr(X, y) 
    
# #     fig = go.Figure(go.Indicator(
# #     mode = "gauge+number",
# #     value = r[0],
# #     domain = {'x': [0, 1], 'y': [0, 1]},
# #     title = {'text': 'Tüketim & ' + ticker},
    
# #     gauge = {
# #         'axis': {'range': [-1, 1], 'tickwidth': 1, 'tickcolor': "darkblue"},
# #         'bar': {'color': "darkblue"},
# #         'bgcolor': "white",
# #         'borderwidth': 2,
# #         'bordercolor': "gray",
# #         # 'steps': [
# #         #     {'range': [-1, 0], 'color': 'gray'},
# #         #     {'range': [0, r[0]], 'color': 'royalblue'}]
# #         }))
# #     return fig

# # @app.callback(
# #     Output('map', 'figure'),
# #     [Input('slct_year', 'value')]
# # )



# # def display_time_series(slct_year):
# #     fig = go.Figure(data=[go.Bar(
# #             x=df_tarih.get_group(slct_year).Periyot, y=df_tarih.get_group(slct_year).kbTuketim,
# #             textposition='auto'
# #         )])
# #     fig.update_traces(marker_color='rgb(158,202,225)', marker_line_color='rgb(8,48,107)',
# #                   marker_line_width=1.5, opacity=0.6,)
# #     fig.update_layout(title_text= 'Aylara göre kişibaşı elektrik tüketimi',template="plotly_dark" )
# #     return fig




# # @app.callback(
# #     Output("slct_tur", "options"), 
# #     Input('slct_cat', 'value'),
# # )
# # def set_cat(x):
# #     print("secildi 1")
# #     return [{'label': i, 'value': i} for i in yeap[x]]

# # @app.callback(
# #     Output("time-series-chart-graf2", "figure"), 
# #     [Input("graf2", "value")])
# # def display_time_series(graf2):
# #     fig = px.line(df, x='Tarih', y=graf2, template="plotly_dark")
# #     return fig

# if __name__ == "__main__":
#     app.run_server(port=8888)