import plotly.graph_objects as go
import pandas as pd
import numpy as np

df_card2 = pd.read_excel('veri2ham.xlsx',  sheet_name='Sheet1')
mevcut_card2 = df_card2.KuruluG*df_card2.YisOlusturma #istihdam
verimlilik_card2 = np.array([5.57, 2.19, 3.12, 4.04, 0.04, 7.83, 3.41]) #uretim/kurulugüç
uretim_card2= 401070.357-290446.924 #ihtiyaç olacak elektrik üretimi
kuruluguc_card2 = uretim_card2/verimlilik_card2 #ihtiyaç olacak kurulu güç
pre_card2 = (kuruluguc_card2*df_card2.YisOlusturma)/10 #gerekli olacak istihdam


fig = go.Figure(layout = go.Layout(
    title = "İstihdam", title_x=0.5,
))

fig.add_trace(go.Indicator(
    mode = "number+delta",
    value = int(pre_card2.sum()),
    title = {"text": "2019 : 47783  - 2030 : 131622"},
    
    delta = {'reference': 47783, 'relative': True},
    domain = {'x': [0, 1], 'y': [0, 1]}))

# fig.update_layout(paper_bgcolor = "mediumspringgreen")

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