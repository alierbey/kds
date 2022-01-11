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
       
       
        html.A("Web Based - EPPDSS", href="/", style={"font-size":18, "font-weight": "bold"}),
        html.Hr(),
        dbc.NavItem("DATA"),
        dbc.Nav(
            [
                dbc.NavLink("Available Data", href="/page-1", active="exact"),
                dbc.NavLink("Adding Data", href="/page-2", active="exact"),
                dbc.NavLink("Data Upload", href="/page-3", active="exact"),
            ],
            vertical=True,
            pills=True,
        ),
   
        html.Hr(),
        dbc.NavItem("ANALYTICS AND OPTIONS"),
        dbc.Nav(
            [
                dbc.NavLink("Consumption Forecast", href="/page-6", active="exact"),
                dbc.NavLink("Decision", href="/page-7", active="exact"),
            ],
            vertical=True,
            pills=True,
        ),
         html.Hr(),
        dbc.NavItem("SENSITIVITY ANALYSIS"),
        dbc.Nav(
            [
                dbc.NavLink("What - If", href="/page-4", active="exact"),
                dbc.NavLink("Goal Seeking", href="/page-5", active="exact"),
            ],
            vertical=True,
            pills=True,
        ),
          html.Hr(),
        dbc.NavItem("REPORTS"),
        dbc.Nav(
            [
                #dbc.NavLink("Home", href="/", active="exact"),
                dbc.NavLink("Descriptive", href="/page-8", active="exact"),
                dbc.NavLink("Predictive", href="/page-9", active="exact"),
                dbc.NavLink("Prescriptive", href="/page-10", active="exact"),
                dbc.NavLink("Scenario", href="/page-11", active="exact"),
           
            ],
            vertical=True,
            pills=True,
        ),
    ],
    style=SIDEBAR_STYLE,
)