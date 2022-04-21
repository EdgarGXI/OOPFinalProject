from Classes import *
import folium

##Creates map
map = folium.Map(location=[11.019033, -74.850760], zoom_start=14, control_scale=True)

map

##Asks for user input
r=Input
r.getInput()

##Locates the file
a=File
a.getFile("text.txt")

