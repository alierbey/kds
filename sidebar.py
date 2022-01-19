import dash_bootstrap_components as dbc
import dash_html_components as html
import dash_core_components as dcc
import style

# the style arguments for the sidebar. We use position:fixed and a fixed width
SIDEBAR_STYLE = {
    "position": "fixed",
    "top": 0,
    "left": 0,
    "bottom": 0,
    "width": "16rem",
    "padding": "2rem 1rem",
    "background-color": style.cardBackColor['back'],
    'box-shadow': '2px 5px 5px 1px rgba(30, 47, 123, .5)'
}





sidebar = html.Div(
    [
       
       
        html.A("Web Tabanlı KDS", href="/", style={"font-size":18, "font-weight": "bold"}),
        html.Hr(),
        dbc.NavItem("VERİ"),
        dbc.Nav(
            [
                dbc.NavLink("Mevcut veriler", href="/page-1", active="exact"),
                dbc.NavLink("Veri Düzenleme", href="/page-2", active="exact"),
                dbc.NavLink("Veri Yükleme", href="/page-3", active="exact"),
            ],
            vertical=True,
            pills=True,
        ),
   
        html.Hr(),
        dbc.NavItem("PARAMETRELER"),
        dbc.Nav(
            [
                dbc.NavLink("Tahmin Parametreleri", href="/page-6", active="exact"),
                dbc.NavLink("Karar Parametreleri", href="/page-7", active="exact"),
            ],
            vertical=True,
            pills=True,
        ),
         html.Hr(),
        dbc.NavItem("Duyarlılık Analizleri"),
        dbc.Nav(
            [
                dbc.NavLink("Eğer - Ne", href="/page-4", active="exact"),
                dbc.NavLink("Hedef Arama", href="/page-5", active="exact"),
            ],
            vertical=True,
            pills=True,
        ),
          html.Hr(),
        dbc.NavItem("RAPORLAR"),
        dbc.Nav(
            [
                #dbc.NavLink("Home", href="/", active="exact"),
                dbc.NavLink("Tanımlayıcı", href="/page-8", active="exact"),
                dbc.NavLink("Öngörücü", href="/page-9", active="exact"),
                dbc.NavLink("Kuralcı", href="/page-10", active="exact"),
                dbc.NavLink("Senaryolar", href="/page-11", active="exact"),
           
            ],
            vertical=True,
            pills=True,
        ),
    ],
    style=SIDEBAR_STYLE,
)