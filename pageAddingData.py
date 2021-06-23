import dash_core_components as dcc
import dash_html_components as html
import style 
txtContent = """
Karar Destek Sisteminde çok sayıda veri kullanılmakta olup, bu veriler üzerinde çok sayıda veri önişleme yöntemi uygulanmaktadır. Ayrıca uygulanan analitik yöntemlerin çoğu verinin formatına bağlı olarak çalışmaktadır. Bu sebeple yeni veri yüklenebilmesi için aşağıdaki şartların sağlanması gerekmektedir.
"""
pageAddingData = html.Div(
    [
        html.H3("Adding Data"),
              html.Div([
                html.Div([
                    html.Div([
                         html.P(txtContent, style = {'padding':"1rem"}),
                         
                         html.Ul([
                             html.Li("Öncelikle hangi veri türüne ekleme/silme işlemi uygulanacağı seçimi yapılmalıdır. "),
                             html.Li("Tüketim verileri ay bazlı zaman serisi verileri olduğu için veritabanında yer alan verilerin bir kısmını silebilir veya değiştirebilirsiniz."),
                             html.Li("Santral seçim kriterleri ile ilgili santral türü bazlı veriler yer aldığı için ilgili kriterle ilgili verileri değiştirebilir, bu verileri silebilir veya ekleyebilirsiniz."),
                             html.Li("•	Eksik veri tanımlanması durumunda Veri Madenciliği yöntemleriyle eksik veriler tamamlanacaktır. Bu sebeple sonuçların gerçeğe daha yakın olması için eksik veri bırakmamanız önemlidir."),
                             
                         ]),
                         

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
              ],className="row",style={"height":"100vh"}),
        html.Hr(),
    ], 
)
