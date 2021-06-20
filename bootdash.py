import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.graph_objects as go
import pandas as pd
import numpy as np
import plotly.express as px
import pandas as pd
from scipy import stats
import scipy as sp
from plotly.subplots import make_subplots
from dash.dependencies import Input, Output
import plotly.io as pio


pio.templates.default = "plotly_dark"


app = dash.Dash(external_stylesheets=[dbc.themes.DARKLY])



df = pd.read_excel("veri1.xlsx")
df['Tarih']=df['Tarih'].dt.year
df_tarih = df.groupby('Tarih')


###### pie #####
df2 = pd.read_excel("veri2.xlsx")

df_tur = df2.groupby(['Kategori','Tur'])
#print(df_tur.groups) 

yeap  = {"Teknik": [], "Cevre": [], "Ekonomi":[]}

print("===========")
print(yeap)
print("===========")

for kat,tur in df_tur:
    print(kat)
    if kat[0] == 'Teknik':
        yeap["Teknik"].append(kat[1])
    if kat[0] == 'Cevre':
        yeap["Cevre"].append(kat[1])
    if kat[0] == 'Ekonomi':
        yeap["Ekonomi"].append(kat[1])
        #print(kat[1])

print(yeap)


# values = []
# for sub_ind in (df.unique()):
#     values.append(df_tur.get_group(('CO2', sub_ind)))
# print(values)

#print(df_cat('Cevre'))
fig = go.Figure()

###### pie #####

# the style arguments for the sidebar. We use position:fixed and a fixed width
SIDEBAR_STYLE = {
    "position": "fixed",
    "top": 0,
    "left": 0,
    "bottom": 0,
    "width": "16rem",
    "padding": "2rem 1rem",
    "background-color": "#030303",
}

# the styles for the main content position it to the right of the sidebar and
# add some padding.
CONTENT_STYLE = {
    "margin-left": "15rem",
    "margin-right": "2rem",
    "padding": "2rem 1rem",
    "background-color": "#2A1D33",
   
}

colors = {
    'background': '#111111',
    'text': '#7FDBFF'
}



sidebar = html.Div(
    [
        html.H2("KDS", className="display-4"),
        html.Hr(),
        html.P(
            "Karar Destek Sistemleri"
        ),
        dbc.Nav(
            [
                dbc.NavLink("Home", href="/", active="exact"),
                dbc.NavLink("Descriptive", href="/page-1", active="exact"),
                dbc.NavLink("Integrative", href="/page-2", active="exact"),
                dbc.NavLink("Predictive", href="/page-3", active="exact"),
                dbc.NavLink("Prescriptive", href="/page-3", active="exact"),
           
            ],
            vertical=True,
            pills=True,
        ),
    ],
    style=SIDEBAR_STYLE,
)



yeni = html.Div(
    [
        html.H3("Descriptive"),
        html.Div([
                            html.Div([
                                html.Div([
                                    html.H6("Makro Değişkenler ile Tüketim Korelasyonları", style={'text-align': 'center'}),
                                        html.Div(style={'backgroundColor': colors['background']},
                                            children=html.Div([
                                            dcc.Dropdown( id="ticker3", options=[{"label": x, "value": x} for x in df.columns[3:]],value=df.columns[3],clearable=False,),
                                            dcc.Graph(id="time-series-chart3"),
                                            ]),
                                        ),
                                ],className="card-header")            
                            ],className="col-xl-4"),
                     

                    html.Div([
                        html.Div([
                            html.Div([
                                    html.H6("Makro Değişkenler", style={'text-align': 'center'}),
                                    dcc.Dropdown(
                                    id="graf2",
                                    options=[{"label": x, "value": x} 
                                            for x in df.columns[2:]],
                                    value=df.columns[2],
                                    clearable=False,
                                    ),
                                    dcc.Graph(id="time-series-chart-graf2"),
                            ])
                        ],className="card-header",)            
                    ],className="col-xl-8",)
                    

                ],className="row"),

 html.Hr(),
              html.Div([
  html.Div([
  html.Div([
          
      html.Div([

    html.H4("Kişibaşı Elektrik Tüketim Raporu", style={'text-align': 'center'}),

    dcc.Dropdown(id="slct_year",
                 options=[{"label": x, "value": x} 
                          for x in df_tarih.groups.keys()],
                 clearable=False,
                 multi=False,
                 value=1986,
                 style={'width': "40%"}
                 ),

    dcc.Graph(id='map')
])
      
        ],
        className="card-header",)            
        ],
        className="col-xl-7",),
         html.Div([
  html.Div([
       html.Div([
    html.H4("Kişibaşı Elektrik Tüketim Raporu", style={'text-align': 'center'}),
    html.P("Kategori:"),
    dcc.Dropdown(
        id='slct_cat', 
        value='Teknik', 
        options=[{'value': x, 'label': x} 
                 for x in ['Teknik', 'Cevre', 'Ekonomi']],
        clearable=False
    ),
    html.P("Tür"),
    dcc.Dropdown(id='slct_tur', value='Uretim'),
    html.Hr(),
    dcc.Graph(id="pie-chart",figure=fig),
])
  
      

        ],
        className="card-header",)            
        ],
        className="col-xl-5",)
        ],
        className="row"
        
        ),
        html.Hr(),
    ],
    
)

content = html.Div(id="page-content", style=CONTENT_STYLE)

app.layout = html.Div([dcc.Location(id="url"), sidebar, content])


@app.callback(Output("page-content", "children"), [Input("url", "pathname")])
def render_page_content(pathname):
    if pathname == "/":
        return yeni
    elif pathname == "/page-1":
        return html.P("This is the content of page 1. Yay!")
    elif pathname == "/page-2":
        return html.P("Oh cool, this is page 2!")
    # If the user tries to reach a different page, return a 404 message
    return dbc.Jumbotron(
        [
            html.H1("404: Not found", className="text-danger"),
            html.Hr(),
            html.P(f"The pathname {pathname} was not recognised..."),
        ]
    )

@app.callback(
    Output("time-series-chart", "figure"), 
    [Input("ticker", "value")])
def display_time_series(ticker):
    print(ticker)
    #fig = px.line(df, x='Tarih', y=ticker, template="plotly_dark")
    X = np.array(df['Tuketim'])
    y = np.array(df[ticker])
    r = sp.stats.pearsonr(X, y) 

    fig = go.Figure(go.Indicator(
    mode = "number+gauge+delta",
    gauge = {'shape': "bullet"},
    delta = {'reference': 300},
    value = r[0]*100,
    domain = {'x': [0.1, 1], 'y': [0.2, 0.9]},
    title = {'text': "Avg order size"}))
    return fig


@app.callback(
    Output("time-series-chart2", "figure"), 
    [Input("ticker2", "value")])
def display_time_series(ticker):
    print(ticker)
    #fig = px.line(df, x='Tarih', y=ticker, template="plotly_dark")
    X = np.array(df['Tuketim'])
    y = np.array(df[ticker])
    r = sp.stats.pearsonr(X, y) 

    fig = go.Figure(go.Indicator(
    mode = "number+gauge+delta",
    gauge = {'shape': "bullet"},
    delta = {'reference': 300},
    value = r[0]*100,
    domain = {'x': [0.1, 1], 'y': [0.2, 0.9]},
    title = {'text': "Avg order size"}))
    return fig

@app.callback(
    Output("time-series-chart3", "figure"), 
    [Input("ticker3", "value")])
def display_time_series(ticker):
    print(ticker)
    #fig = px.line(df, x='Tarih', y=ticker, template="plotly_dark")
    X = np.array(df['Tuketim'])
    y = np.array(df[ticker])
    r = sp.stats.pearsonr(X, y) 
    
    fig = go.Figure(go.Indicator(
    mode = "gauge+number",
    value = r[0],
    domain = {'x': [0, 1], 'y': [0, 1]},
    title = {'text': 'Tüketim & ' + ticker},
    
    gauge = {
        'axis': {'range': [-1, 1], 'tickwidth': 1, 'tickcolor': "darkblue"},
        'bar': {'color': "darkblue"},
        'bgcolor': "white",
        'borderwidth': 2,
        'bordercolor': "gray",
        # 'steps': [
        #     {'range': [-1, 0], 'color': 'gray'},
        #     {'range': [0, r[0]], 'color': 'royalblue'}]
        }))
    return fig

@app.callback(
    Output('map', 'figure'),
    [Input('slct_year', 'value')]
)

# def update_graph(option_slctd):
#     print(option_slctd)
#     print(type(option_slctd))

def display_time_series(slct_year):
    fig = go.Figure(data=[go.Bar(
            x=df_tarih.get_group(slct_year).Periyot, y=df_tarih.get_group(slct_year).kbTuketim,
            textposition='auto'
        )])
    fig.update_traces(marker_color='rgb(158,202,225)', marker_line_color='rgb(8,48,107)',
                  marker_line_width=1.5, opacity=0.6,)
    fig.update_layout(title_text= 'Aylara göre kişibaşı elektrik tüketimi',template="plotly_dark" )
    return fig


@app.callback(
    Output("pie-chart", "figure"), 
    Input('slct_tur', 'value'),
    Input('slct_cat', 'value'),
)
def set_fig(slct_tur,slct_cat):
    print(slct_tur + " " + slct_cat )

    df_cat = df2.groupby('Kategori')
    df_tur = df_cat.get_group(slct_cat)
    df_son = df_tur.groupby('Tur')
    df_filter = df_son.get_group(slct_tur)

    fig = px.pie(df_filter, values='Deger', names='Santral', template="plotly_dark")
    fig.update_layout(title_text= 'Aylara göre kişibaşı elektrik tüketimi' )
    return fig

@app.callback(
    Output("slct_tur", "options"), 
    Input('slct_cat', 'value'),
)
def set_cat(x):
    print("secildi 1")
    return [{'label': i, 'value': i} for i in yeap[x]]

@app.callback(
    Output("time-series-chart-graf2", "figure"), 
    [Input("graf2", "value")])
def display_time_series(graf2):
    fig = px.line(df, x='Tarih', y=graf2, template="plotly_dark")
    return fig

if __name__ == "__main__":
    app.run_server(port=80)