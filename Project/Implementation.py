import folium
import pandas as pd

db = pd.read_csv("https://raw.githubusercontent.com/EdgarGXI/OOPFinalProject/main/database.csv")

def select_marker_color(row):
   if row['Categoria']=='Bloque':
        return'red'
   elif row['Categoria']=='Puerta':
        return'pink'
   elif row['Categoria']=='Servicios':
        return'blue'
   elif row['Categoria']=='Restaurantes':
        return'black'
   elif row['Categoria']=='Salas de Usuario':
        return'yellow'



db['color']=db.apply(select_marker_color,axis=1)
db.head(5)




m=folium.Map(
    location=[11.019465666697565,-74.85049692610932],
    zoom_start=20
)

for _, i in db.iterrows():
    folium.Marker(
        location=[i['Latitud'], i['Longitud']],popup=i['Nombre'],
        tooltip=i['Nombre'], icon=folium.Icon(color=i['color'])

    ).add_to(m)

m
