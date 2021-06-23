import plotly.graph_objects as go

fig = go.Figure(layout = go.Layout(
    title = "Tüketimde Beklenen Değişim", title_x=0.5,
))

fig.add_trace(go.Indicator(
    mode = "number+delta",
    value = 401070.357,
    title = {"text": "290446 GWh - 401070 GWh"},
    delta = {'reference': 290446.924, 'relative': True},
    domain = {'x': [0, 1], 'y': [0, 1]}))

# fig.update_layout(paper_bgcolor = "midnightblue")

fig.update_layout({
    "height": 300,
    "font_color":"white",
    "plot_bgcolor": "rgba(0, 0, 0, 0)",
    "paper_bgcolor": "rgba(0, 0, 0, 0)",
})


# import dash
# import dash_core_components as dcc
# import dash_html_components as html

# app = dash.Dash()
# app.layout = html.Div([
#     dcc.Graph(figure=fig)
# ])

# app.run_server(debug=True, use_reloader=False)  # Turn off reloader if inside Jupyter