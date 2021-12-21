import dash_core_components as dcc
import dash_html_components as html
import style

txtContent = """
Elektriğin ihtiyaçtan fazla üretilmesi de az üretilmesi de makro düzeyde birçok soruna zemin hazırlamaktadır. 
Bu yüzden sürecin doğru planlanması ve yönetilmesi için kısa, orta ve uzun dönemli yük tüketim miktarlarıyla 
ilgili senaryolar oluşturarak tahmin modelleri geliştirilmektedir.
"""

pageAvailableData = html.Div(
    [
        html.H3("Available Data"),
              html.Div([
                html.Div([
                    html.Div([
                         html.P(txtContent, style = {'padding':"1rem"}),
                        
                         html.P("Bu Karar Destek Sisteminin içeriğinde;",style = {'padding-left':"1rem"}),
                         html.Ul([
                             html.Li("Nüfus verileri"),
                             html.Li("Gayri Safi Yurtiçi Hasıla (TL Bazlı)"),
                             html.Li("Gayri Safi Yurtiçi Hasıla (Dolar Bazlı) "),
                             html.Li("Sanayi Üretim Endeksi "),
                             html.Li("Kurulu güç, "),
                             html.Li("Yıllık üretim miktarı, "),
                             html.Li("Kapasite faktörü, "),
                             html.Li("Yatırım maliyetleri, "),
                             html.Li("İşletme ve bakım maliyetleri "),
                             html.Li("Yakıt maliyetleri,  "),
                             html.Li("Geri ödeme süresi, "),
                             html.Li("Arazi kullanımı, "),
                             html.Li("İstihdam oluşturma potansiyeli "),
                             html.Li(html.P(['CO', html.Sub('2'), ', CO,', ' NO', html.Sub('X'), ', SO', html.Sub('2'), ' Emisyonları'])),
                         ]),
                         html.P("verileri bulunmaktadır.",style = {'padding-left':"1rem",'padding-bottom':"1rem"}),
                        #  html.A("İleri" , href="/page-4",style={"font-size":18, "font-weight": "bold",'padding':"3rem"}),
                    ],style = {'background-color' : style.cardBackColor['back'],'box-shadow': '2px 5px 5px 1px rgba(30, 47, 123, .5)',"vertical-align":"middle"})            
                ],className="col-xl-12"),
              ],className="row"),
        html.Hr(),
         html.Div(html.Img(src=("assets/images/veriler.png"), style={"max-width":"100%", "height":"100%"})),
         
         
    ], 
)