import plotly.express as px
import pandas as pd
import plotly.io as pio
pio.templates.default = "plotly_dark"

kriter = ["Üretim", "Kapasite Faktörü", "Kurulu Güç", "CO2", "CH4", 
           "NOx", "SO2", "Arazi Kullanımı", "Yatırım Maliyeti", 
           "İsletme Maliyeti", "Yakıt Maliyeti", "Geri Odeme Süresi.", "İstihdam"]
kategori = ["Teknik", "Teknik", "Teknik", "Çevre", "Çevre","Çevre","Çevre","Çevre",
           "Ekonomik","Ekonomik","Ekonomik","Ekonomik","Ekonomik"]
agirlik = [0.193066, 0.175514, 0.152621, 0.127184, 0.101747, 0.0782672, 0.0579757,
           0.0414112, 0.0285595, 0.0190397, 0.0122836, 0.00767728, 0.0046529]
df = pd.DataFrame(
    dict(kriter=kriter, kategori=kategori, agirlik=agirlik)
)

fig = px.sunburst(df, path=['kategori', 'kriter'], values='agirlik')


fig.update_layout({
"plot_bgcolor": "rgba(0, 0, 0, 0)",
"paper_bgcolor": "rgba(0, 0, 0, 0)",
})