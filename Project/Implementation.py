from asyncio.windows_events import NULL
from tkinter import messagebox, ttk
import tkinter as tk
from turtle import clear
from requests import delete
import tkintermapview
from tkinter import *
from tkinter import simpledialog
import pandas as pd

# <---------------------------------------------- Base de datos ------------------------------------------------>
db = pd.read_csv("https://raw.githubusercontent.com/EdgarGXI/OOPFinalProject/main/database.csv")
#print(db)

# <----------------------------------------- Configuración de ventana ------------------------------------------>
root= Tk() # Ventana
root.title("Mapa - Universidad del norte") # Titulo ventana
root.geometry("1150x700") # Tamaño ventana
root.resizable(width=False, height=False) # Evitar modificar tamaño de ventana 
esp3 = Label(root, text=" ") # Espacio 
esp3.pack()
title = Label(root, text = "CompaniUN  -  Mapa Universidad del Norte", font=("Calibri", 25)) # Titulo 
title.pack()

# <------------------------------------------ Mostrar mapa en pantalla ----------------------------------------->
my_label= LabelFrame(root)
my_label.pack(pady=10, padx=20) # Centrar mapa en la ventana
map_widget = tkintermapview.TkinterMapView(my_label, width=850, height=450,corner_radius=20) # Mostrar mapa en la ventana
map_widget.set_position(11.018985992247588, -74.85068279601066) # Coordenadas universidad
map_widget.set_zoom(18) # Zoom mapa
map_widget.pack()
# <-------------------------------------- Caja de opciones en pantalla ---------------------------------------->

opciones = ttk.Combobox(
    state="readonly", # Permite solo escoger opciones
    values=["Bloque A", "Bloque B", "Bloque C", "Bloque D", "Bloque E", "Bloque F", "Bloque G", "Bloque I", "Bloque J", 
    "Bienestar", "Bienestar bloque M", "Biblioteca", "Casa de Estudio", "duNord Graphique", "Km5","duNord Store", 
    "Cajero G", "Cajero F", "Cajero C", "Corresponsal","M.Transmetro", "Museo", "Centro Médico", "LeSalon", "LePetit",
    "duNord Plaza", "1966", "Café duNord", "duNord Terrase", "El Camion", "La Gofreria", "Lab 1", "Lab 2", "Lab 3", 
    "Lab 4", "Lab 5", "Bambu K", "Bambu J", "Puerta 4", "Puerta 7", "SDU B", "SDU G", "SDU K"] 
)

text = Label(root, text="¿A donde quiere ir? :", font=("Calibri", 12)) # Texto encima del menú
text.place(x=707, y=573) # Coordenadas texto
opciones.place(x=850, y=575) # Coordenadas menú
# <--------------------------------------------- Lugar que indique el usuario --------------------------------------------------->

lugar_user = ttk.Combobox(
    state="readonly", # Permite solo escoger opciones
    values=["Bloque A", "Bloque B", "Bloque C", "Bloque D", "Bloque E", "Bloque F", "Bloque G", "Bloque I", "Bloque J", 
    "Bienestar", "Bienestar bloque M", "Biblioteca", "Casa de Estudio", "duNord Graphique", "Km5","duNord Store", 
    "Cajero G", "Cajero F", "Cajero C", "Corresponsal","M.Transmetro", "Museo", "Centro Médico", "LeSalon", "LePetit",
    "duNord Plaza", "1966", "Café duNord", "duNord Terrase", "El Camion", "La Gofreria", "Lab 1", "Lab 2", "Lab 3", 
    "Lab 4", "Lab 5", "Bambu K", "Bambu J", "Puerta 4", "Puerta 7", "SDU B", "SDU G", "SDU K"] 
)

user = Label(root, text="¿Donde se encuentra? :", font=("Calibri", 12)) # Texto encima del menú
user.place(x=150, y=573) # Coordenadas texto
lugar_user.place(x=320, y=575) # Coordenadas menú




# <--------------------------------------------- Boton del input del usuario ----------------------------------------------->
def buscar():
    boton=Label(root) # Imprime input del usuario
    boton.pack()
    def limpiar():
        botonLimpiar = Label(root)
        botonLimpiar.pack()

        marker_user.delete()
        marker.delete()
        path_1.delete()

    
    # Caja de opciones del usuario
    if lugar_user.get() == "Bloque A":
        marker_user = map_widget.set_marker(11.018464, -74.851093, text="Estás Acá", text_color="black",
                                 marker_color_circle="red", marker_color_outside="gray40", font=("Helvetica Bold", 20))
        pos_1=(11.018464, -74.851093)

    if lugar_user.get() == "Bloque B":
        marker_user = map_widget.set_marker(11.018760, -74.851008, text="Estás Acá", text_color="black",
                                marker_color_circle="red", marker_color_outside="gray40", font=("Helvetica Bold", 20))
        pos_1=(11.018760, -74.851008)

    if lugar_user.get() == "Bloque C":
        marker_user = map_widget.set_marker(11.018991, -74.850942, text="Estás Acá", text_color="black",
                                 marker_color_circle="red", marker_color_outside="gray40", font=("Helvetica Bold", 20))
        pos_1=(11.018991, -74.850942)

    if lugar_user.get() == "Bloque D":
        marker_user = map_widget.set_marker(11.018190, -74.850134, text="Estás Acá", text_color="black",
                                marker_color_circle="red", marker_color_outside="gray40", font=("Helvetica Bold", 20))
        pos_1=(11.018190, -74.850134)

    if lugar_user.get() == "Bloque E":
        marker_user = map_widget.set_marker(11.018469, -74.850023, text="Estás Acá", text_color="black",
                                 marker_color_circle="red", marker_color_outside="gray40", font=("Helvetica Bold", 20))
        pos_1=(11.018469, -74.850023)

    if lugar_user.get() == "Bloque F":
        marker_user = map_widget.set_marker(11.018824, -74.850041, text="Estás Acá", text_color="black",
                                marker_color_circle="red", marker_color_outside="gray40", font=("Helvetica Bold", 20))
        pos_1=(11.018824, -74.850041)

    if lugar_user.get() == "Bloque G":
        marker_user = map_widget.set_marker(11.019709, -74.849727, text="Estás Acá", text_color="black",
                                 marker_color_circle="red", marker_color_outside="gray40", font=("Helvetica Bold", 20))
        pos_1=(11.019709, -74.849727)

    if lugar_user.get() == "Bloque I":
        marker_user = map_widget.set_marker(11.019644, -74.850759, text="Estás Acá", text_color="black",
                                marker_color_circle="red", marker_color_outside="gray40", font=("Helvetica Bold", 20))
        pos_1=(11.019644, -74.850759)

    if lugar_user.get() == "Bloque L":
        marker_user = map_widget.set_marker(11.019287, -74.851648, text="Estás Acá", text_color="black",
                                 marker_color_circle="red", marker_color_outside="gray40", font=("Helvetica Bold", 20))
        pos_1=(11.019287, -74.851648)

    if lugar_user.get() == "Bloque K":
        marker_user = map_widget.set_marker(11.020249, -74.851169, text="Estás Acá", text_color="black",
                                marker_color_circle="red", marker_color_outside="gray40", font=("Helvetica Bold", 20))
        pos_1=(11.020249, -74.851169)

    if lugar_user.get() == "Bloque J":
        marker_user = map_widget.set_marker(11.020857, -74.851975, text="Estás Acá", text_color="black",
                                 marker_color_circle="red", marker_color_outside="gray40", font=("Helvetica Bold", 20))
        pos_1=(11.020857, -74.851975)

    if lugar_user.get() == "Bloque M":
        marker_user = map_widget.set_marker(11.019971, -74.848069, text="Estás Acá", text_color="black",
                                marker_color_circle="red", marker_color_outside="gray40", font=("Helvetica Bold", 20))
        pos_1=(11.019971, -74.848069)

    if lugar_user.get() == "Puerto 4":
        marker_user = map_widget.set_marker(11.017380, -74.850544, text="Estás Acá", text_color="black",
                                 marker_color_circle="red", marker_color_outside="gray40", font=("Helvetica Bold", 20))
        pos_1=(11.017380, -74.850544)

    if lugar_user.get() == "Puerta 7":
        marker_user = map_widget.set_marker(11.019204, -74.849621, text="Estás Acá", text_color="black",
                                marker_color_circle="red", marker_color_outside="gray40", font=("Helvetica Bold", 20))
        pos_1=(11.019204, -74.849621)

    if lugar_user.get() == "Biblioteca":
        marker_user = map_widget.set_marker(11.017828, -74.850284, text="Estás Acá", text_color="black",
                                 marker_color_circle="red", marker_color_outside="gray40", font=("Helvetica Bold", 20))
        pos_1=(11.017828, -74.850284)

    if lugar_user.get() == "Casa de Estudio":
        marker_user = map_widget.set_marker(11.017580, -74.850313, text="Estás Acá", text_color="black",
                                marker_color_circle="red", marker_color_outside="gray40", font=("Helvetica Bold", 20))
        pos_1=(11.017580, -74.850313)

    if lugar_user.get() == "duNord Graphique":
        marker_user = map_widget.set_marker(11.018953, -74.850431, text="Estás Acá", text_color="black",
                                 marker_color_circle="red", marker_color_outside="gray40", font=("Helvetica Bold", 20))
        pos_1=(11.018953, -74.850431)

    if lugar_user.get() == "Km5":
        marker_user = map_widget.set_marker(11.018997, -74.850940, text="Estás Acá", text_color="black",
                                marker_color_circle="red", marker_color_outside="gray40", font=("Helvetica Bold", 20))
        pos_1=(11.018997, -74.850940)

    if lugar_user.get() == "duNord Store":
        marker_user = map_widget.set_marker(11.018935, -74.850781, text="Estás Acá", text_color="black",
                                 marker_color_circle="red", marker_color_outside="gray40", font=("Helvetica Bold", 20))
        pos_1=(11.018935, -74.850781)

    if lugar_user.get() == "Cajero G":
        marker_user = map_widget.set_marker(11.019744, -74.849635, text="Estás Acá", text_color="black",
                                marker_color_circle="red", marker_color_outside="gray40", font=("Helvetica Bold", 20))
        pos_1=(11.019744, -74.849635)

    if lugar_user.get() == "Cajero F":
        marker_user = map_widget.set_marker(1.018612, -74.850126, text="Estás Acá", text_color="black",
                                 marker_color_circle="red", marker_color_outside="gray40", font=("Helvetica Bold", 20))
        pos_1=(1.018612, -74.850126)

    if lugar_user.get() == "Cajero C":
        marker_user = map_widget.set_marker(11.019097, -74.850779, text="Estás Acá", text_color="black",
                                marker_color_circle="red", marker_color_outside="gray40", font=("Helvetica Bold", 20))
        pos_1=(11.019097, -74.850779)

    if lugar_user.get() == "Corresponsal":
        marker_user = map_widget.set_marker(11.019038, -74.850765, text="Estás Acá", text_color="black",
                                 marker_color_circle="red", marker_color_outside="gray40", font=("Helvetica Bold", 20))
        pos_1=(11.019038, -74.850765)

    if lugar_user.get() == "M.Transmetro":
        marker_user = map_widget.set_marker(11.018436, -74.851095, text="Estás Acá", text_color="black",
                                marker_color_circle="red", marker_color_outside="gray40", font=("Helvetica Bold", 20))
        pos_1=(11.018436, -74.851095)

    if lugar_user.get() == "SDU B":
        marker_user = map_widget.set_marker(11.018778, -74.851133, text="Estás Acá", text_color="black",
                                 marker_color_circle="red", marker_color_outside="gray40", font=("Helvetica Bold", 20))
        pos_1=(11.018778, -74.851133)

    if lugar_user.get() == "SDU G":
        marker_user = map_widget.set_marker(11.019763, -74.849906, text="Estás Acá", text_color="black",
                                marker_color_circle="red", marker_color_outside="gray40", font=("Helvetica Bold", 20))
        pos_1=(11.019763, -74.849906)

    if lugar_user.get() == "SDU K":
        marker_user = map_widget.set_marker(11.020121, -74.851154, text="Estás Acá", text_color="black",
                                 marker_color_circle="red", marker_color_outside="gray40", font=("Helvetica Bold", 20))
        pos_1=(11.020121, -74.851154)

    if lugar_user.get() == "Museo":
        marker_user = map_widget.set_marker(11.020059, -74.851332, text="Estás Acá", text_color="black",
                                marker_color_circle="red", marker_color_outside="gray40", font=("Helvetica Bold", 20))
        pos_1=(11.020059, -74.851332)

    if lugar_user.get() == "LePetit":
        marker_user = map_widget.set_marker(11.020272, -74.851114, text="Estás Acá", text_color="black",
                                marker_color_circle="red", marker_color_outside="gray40", font=("Helvetica Bold", 20))
        pos_1=(11.020272, -74.851114)

    if lugar_user.get() == "duNord Plaza":
        marker_user = map_widget.set_marker(11.018913, -74.849960, text="Estás Acá", text_color="black",
                                 marker_color_circle="red", marker_color_outside="gray40", font=("Helvetica Bold", 20))
        pos_1=(11.018913, -74.849960)

    if lugar_user.get() == "1966":
        marker_user = map_widget.set_marker(11.018820, -74.849874, text="Estás Acá", text_color="black",
                                marker_color_circle="red", marker_color_outside="gray40", font=("Helvetica Bold", 20))
        pos_1=(11.018820, -74.849874)

    if lugar_user.get() == "Café duNord":
        marker_user = map_widget.set_marker(11.019539, -74.850265, text="Estás Acá", text_color="black",
                                 marker_color_circle="red", marker_color_outside="gray40", font=("Helvetica Bold", 20))
        pos_1=(11.019539, -74.850265)

    if lugar_user.get() == "duNord Terrase":
        marker_user = map_widget.set_marker(11.020264, -74.850584, text="Estás Acá", text_color="black",
                                marker_color_circle="red", marker_color_outside="gray40", font=("Helvetica Bold", 20))
        pos_1=(11.020264, -74.850584)

    if lugar_user.get() == "El Camion":
        marker_user = map_widget.set_marker(11.019156, -74.849935, text="Estás Acá", text_color="black",
                                 marker_color_circle="red", marker_color_outside="gray40", font=("Helvetica Bold", 20))
        pos_1=(11.019156, -74.849935)

    if lugar_user.get() == "La Gofreria":
        marker_user = map_widget.set_marker(11.018907, -74.850202, text="Estás Acá", text_color="black",
                                marker_color_circle="red", marker_color_outside="gray40", font=("Helvetica Bold", 20))
        pos_1=(11.018907, -74.850202)

    if lugar_user.get() == "Bambu K":
        marker_user = map_widget.set_marker(11.019649, -74.851375, text="Estás Acá", text_color="black",
                                 marker_color_circle="red", marker_color_outside="gray40", font=("Helvetica Bold", 20))
        pos_1=(11.019649, -74.851375)

    if lugar_user.get() == "Bambu J":
        marker_user = map_widget.set_marker(11.020636, -74.852212, text="Estás Acá", text_color="black",
                                marker_color_circle="red", marker_color_outside="gray40", font=("Helvetica Bold", 20))
        pos_1=(11.020636, -74.852212)

    if lugar_user.get() == "Centro Médico":
        marker_user = map_widget.set_marker(11.018884, -74.851916, text="Estás Acá", text_color="black",
                                 marker_color_circle="red", marker_color_outside="gray40", font=("Helvetica Bold", 20))
        pos_1=(11.018884, -74.851916)

    if lugar_user.get() == "LeSalon":
        marker_user = map_widget.set_marker(11.019483, -74.850183, text="Estás Acá", text_color="black",
                                marker_color_circle="red", marker_color_outside="gray40", font=("Helvetica Bold", 20))
        pos_1=(11.019483, -74.850183)

    if lugar_user.get() == "Lab 1":
        marker_user = map_widget.set_marker(11.018446, -74.850587, text="Estás Acá", text_color="black",
                                marker_color_circle="red", marker_color_outside="gray40", font=("Helvetica Bold", 20))
        pos_1=(11.018446, -74.850587)

    if lugar_user.get() == "Lab 2":
        marker_user = map_widget.set_marker(11.018750, -74.850508, text="Estás Acá", text_color="black",
                                 marker_color_circle="red", marker_color_outside="gray40", font=("Helvetica Bold", 20))
        pos_1=(11.018750, -74.850508)

    if lugar_user.get() == "Lab 3":
        marker_user = map_widget.set_marker(11.018989, -74.850434, text="Estás Acá", text_color="black",
                                marker_color_circle="red", marker_color_outside="gray40", font=("Helvetica Bold", 20))
        pos_1=(11.018989, -74.850434)

    if lugar_user.get() == "Lab 4":
        marker_user = map_widget.set_marker(11.018793, -74.851810, text="Estás Acá", text_color="black",
                                 marker_color_circle="red", marker_color_outside="gray40", font=("Helvetica Bold", 20))
        pos_1=(11.018793, -74.851810)

    if lugar_user.get() == "Lab 5":
        marker_user = map_widget.set_marker(11.018135, -74.852001, text="Estás Acá", text_color="black",
                                marker_color_circle="red", marker_color_outside="gray40", font=("Helvetica Bold", 20))
        pos_1=(11.018135, -74.852001)

    if lugar_user.get() == "CREE":
        marker_user = map_widget.set_marker(11.019625, -74.849638, text="Estás Acá", text_color="black",
                                 marker_color_circle="red", marker_color_outside="gray40", font=("Helvetica Bold", 20))
        pos_1=(11.019625, -74.849638)

    if lugar_user.get() == "Bienestar":
        marker_user = map_widget.set_marker(11.020029, -74.850332, text="Estás Acá", text_color="black",
                                marker_color_circle="red", marker_color_outside="gray40", font=("Helvetica Bold", 20))
        pos_1=(11.020029, -74.850332)

    if lugar_user.get() == "Bienestar bloque M":
        marker_user = map_widget.set_marker(11.019723, -74.848260, text="Estás Acá", text_color="black",
                                marker_color_circle="red", marker_color_outside="gray40", font=("Helvetica Bold", 20))
        pos_1=(11.019723, -74.848260)




    # Caja de opciones del usuario #2
    if opciones.get() == "Bloque A":
        marker = map_widget.set_marker(11.018464, -74.851093, text="Bloque A", text_color="black",
                                 marker_color_circle="blue", marker_color_outside="gray40", font=("Helvetica Bold", 20))
        pos_2=(11.018464, -74.851093)

    if opciones.get() == "Bloque B":
        marker = map_widget.set_marker(11.018760, -74.851008, text="Bloque B", text_color="black",
                                marker_color_circle="blue", marker_color_outside="gray40", font=("Helvetica Bold", 20))
        pos_2=(11.018760, -74.851008)

    if opciones.get() == "Bloque C":
        marker = map_widget.set_marker(11.018991, -74.850942, text="Bloque C", text_color="black",
                                 marker_color_circle="blue", marker_color_outside="gray40", font=("Helvetica Bold", 20))
        pos_2=(11.018991, -74.850942)

    if opciones.get() == "Bloque D":
        marker = map_widget.set_marker(11.018190, -74.850134, text="Bloque D", text_color="black",
                                marker_color_circle="blue", marker_color_outside="gray40", font=("Helvetica Bold", 20))
        pos_2=(11.018190, -74.850134)

    if opciones.get() == "Bloque E":
        marker = map_widget.set_marker(11.018469, -74.850023, text="Bloque E", text_color="black",
                                 marker_color_circle="blue", marker_color_outside="gray40", font=("Helvetica Bold", 20))
        pos_2=(11.018469, -74.850023)

    if opciones.get() == "Bloque F":
        marker = map_widget.set_marker(11.018824, -74.850041, text="Bloque F", text_color="black",
                                marker_color_circle="blue", marker_color_outside="gray40", font=("Helvetica Bold", 20))
        pos_2=(11.018824, -74.850041)

    if opciones.get() == "Bloque G":
        marker = map_widget.set_marker(11.019709, -74.849727, text="Bloque G", text_color="black",
                                 marker_color_circle="blue", marker_color_outside="gray40", font=("Helvetica Bold", 20))
        pos_2=(11.019709, -74.849727)

    if opciones.get() == "Bloque I":
        marker = map_widget.set_marker(11.019644, -74.850759, text="Bloque I", text_color="black",
                                marker_color_circle="blue", marker_color_outside="gray40", font=("Helvetica Bold", 20))
        pos_2=(11.019644, -74.850759)

    if opciones.get() == "Bloque L":
        marker = map_widget.set_marker(11.019287, -74.851648, text="Bloque L", text_color="black",
                                 marker_color_circle="blue", marker_color_outside="gray40", font=("Helvetica Bold", 20))
        pos_2=(11.019287, -74.851648)

    if opciones.get() == "Bloque K":
        marker = map_widget.set_marker(11.020249, -74.851169, text="Bloque K", text_color="black",
                                marker_color_circle="blue", marker_color_outside="gray40", font=("Helvetica Bold", 20))
        pos_2=(11.020249, -74.851169)

    if opciones.get() == "Bloque J":
        marker = map_widget.set_marker(11.020857, -74.851975, text="Bloque J", text_color="black",
                                 marker_color_circle="blue", marker_color_outside="gray40", font=("Helvetica Bold", 20))
        pos_2=(11.020857, -74.851975)

    if opciones.get() == "Bloque M":
        marker = map_widget.set_marker(11.019971, -74.848069, text="Bloque M", text_color="black",
                                marker_color_circle="blue", marker_color_outside="gray40", font=("Helvetica Bold", 20))
        pos_2=(11.019971, -74.848069)

    if opciones.get() == "Puerta 4":
        marker = map_widget.set_marker(11.017380, -74.850544, text="Puerta 4", text_color="black",
                                 marker_color_circle="blue", marker_color_outside="gray40", font=("Helvetica Bold", 20))
        pos_2=(11.017380, -74.850544)

    if opciones.get() == "Puerta 7":
        marker = map_widget.set_marker(11.019204, -74.849621, text="Puerta 7", text_color="black",
                                marker_color_circle="blue", marker_color_outside="gray40", font=("Helvetica Bold", 20))
        pos_2=(11.019204, -74.849621)

    if opciones.get() == "Biblioteca":
        marker = map_widget.set_marker(11.017828, -74.850284, text="Biblioteca", text_color="black",
                                 marker_color_circle="blue", marker_color_outside="gray40", font=("Helvetica Bold", 20))
        pos_2=(11.017828, -74.850284)

    if opciones.get() == "Casa de Estudio":
        marker = map_widget.set_marker(11.017580, -74.850313, text="Casa de Estudio", text_color="black",
                                marker_color_circle="blue", marker_color_outside="gray40", font=("Helvetica Bold", 20))
        pos_2=(11.017580, -74.850313)

    if opciones.get() == "duNord Graphique":
        marker = map_widget.set_marker(11.018953, -74.850431, text="duNord Graphique", text_color="black",
                                 marker_color_circle="blue", marker_color_outside="gray40", font=("Helvetica Bold", 20))
        pos_2=(11.018953, -74.850431)

    if opciones.get() == "Km5":
        marker = map_widget.set_marker(11.018997, -74.850940, text="Km5", text_color="black",
                                marker_color_circle="blue", marker_color_outside="gray40", font=("Helvetica Bold", 20))
        pos_2=(11.018997, -74.850940)

    if opciones.get() == "duNord Store":
        marker = map_widget.set_marker(11.018935, -74.850781, text="duNord Store", text_color="black",
                                 marker_color_circle="blue", marker_color_outside="gray40", font=("Helvetica Bold", 20))
        pos_2=(11.018935, -74.850781)

    if opciones.get() == "Cajero G":
        marker = map_widget.set_marker(11.019744, -74.849635, text="Cajero G", text_color="black",
                                marker_color_circle="blue", marker_color_outside="gray40", font=("Helvetica Bold", 20))
        pos_2=(11.019744, -74.849635)

    if opciones.get() == "Cajero F":
        marker = map_widget.set_marker(1.018612, -74.850126, text="Cajero F", text_color="black",
                                 marker_color_circle="blue", marker_color_outside="gray40", font=("Helvetica Bold", 20))
        pos_2=(1.018612, -74.850126)

    if opciones.get() == "Cajero C":
        marker = map_widget.set_marker(11.019097, -74.850779, text="Cajero C", text_color="black",
                                marker_color_circle="blue", marker_color_outside="gray40", font=("Helvetica Bold", 20))
        pos_2=(11.019097, -74.850779)

    if opciones.get() == "Corresponsal":
        marker = map_widget.set_marker(11.019038, -74.850765, text="Corresponsal", text_color="black",
                                 marker_color_circle="blue", marker_color_outside="gray40", font=("Helvetica Bold", 20))
        pos_2=(11.019038, -74.850765)

    if opciones.get() == "M.Transmetro":
        marker = map_widget.set_marker(11.018436, -74.851095, text="M.Transmetro", text_color="black",
                                marker_color_circle="blue", marker_color_outside="gray40", font=("Helvetica Bold", 20))
        pos_2=(11.018436, -74.851095)

    if opciones.get() == "SDU B":
        marker = map_widget.set_marker(11.018778, -74.851133, text="SDU B", text_color="black",
                                 marker_color_circle="blue", marker_color_outside="gray40", font=("Helvetica Bold", 20))
        pos_2=(11.018778, -74.851133)

    if opciones.get() == "SDU G":
        marker = map_widget.set_marker(11.019763, -74.849906, text="SDU G", text_color="black",
                                marker_color_circle="blue", marker_color_outside="gray40", font=("Helvetica Bold", 20))
        pos_2=(11.019763, -74.849906)

    if opciones.get() == "SDU K":
        marker = map_widget.set_marker(11.020121, -74.851154, text="SDU K", text_color="black",
                                 marker_color_circle="blue", marker_color_outside="gray40", font=("Helvetica Bold", 20))
        pos_2=(11.020121, -74.851154)

    if opciones.get() == "Museo":
        marker = map_widget.set_marker(11.020059, -74.851332, text="Museo", text_color="black",
                                marker_color_circle="blue", marker_color_outside="gray40", font=("Helvetica Bold", 20))
        pos_2=(11.020059, -74.851332)

    if opciones.get() == "LePetit":
        marker = map_widget.set_marker(11.020272, -74.851114, text="LePetit", text_color="black",
                                marker_color_circle="blue", marker_color_outside="gray40", font=("Helvetica Bold", 20))
        pos_2=(11.020272, -74.851114)

    if opciones.get() == "duNord Plaza":
        marker = map_widget.set_marker(11.018913, -74.849960, text="duNord Plaza", text_color="black",
                                 marker_color_circle="blue", marker_color_outside="gray40", font=("Helvetica Bold", 20))
        pos_2=(11.018913, -74.849960)

    if opciones.get() == "1966":
        marker = map_widget.set_marker(11.018820, -74.849874, text="1966", text_color="black",
                                marker_color_circle="blue", marker_color_outside="gray40", font=("Helvetica Bold", 20))
        pos_2=(11.018820, -74.849874)

    if opciones.get() == "Café duNord":
        marker = map_widget.set_marker(11.019539, -74.850265, text="Café duNord", text_color="black",
                                 marker_color_circle="blue", marker_color_outside="gray40", font=("Helvetica Bold", 20))
        pos_2=(11.019539, -74.850265)

    if opciones.get() == "duNord Terrase":
        marker = map_widget.set_marker(11.020264, -74.850584, text="duNord Terrase", text_color="black",
                                marker_color_circle="blue", marker_color_outside="gray40", font=("Helvetica Bold", 20))
        pos_2=(11.020264, -74.850584)

    if opciones.get() == "El Camion":
        marker = map_widget.set_marker(11.019156, -74.849935, text="El Camion", text_color="black",
                                 marker_color_circle="blue", marker_color_outside="gray40", font=("Helvetica Bold", 20))
        pos_2=(11.019156, -74.849935)

    if opciones.get() == "La Gofreria":
        marker = map_widget.set_marker(11.018907, -74.850202, text="La Gofreria", text_color="black",
                                marker_color_circle="blue", marker_color_outside="gray40", font=("Helvetica Bold", 20))
        pos_2=(11.018907, -74.850202)

    if opciones.get() == "Bambu K":
        marker = map_widget.set_marker(11.019649, -74.851375, text="Bambu K", text_color="black",
                                 marker_color_circle="blue", marker_color_outside="gray40", font=("Helvetica Bold", 20))
        pos_2=(11.019649, -74.851375)

    if opciones.get() == "Bambu J":
        marker = map_widget.set_marker(11.020636, -74.852212, text="Bambu J", text_color="black",
                                marker_color_circle="blue", marker_color_outside="gray40", font=("Helvetica Bold", 20))
        pos_2=(11.020636, -74.852212)

    if opciones.get() == "Centro Médico":
        marker = map_widget.set_marker(11.018884, -74.851916, text="Centro Médico", text_color="black",
                                 marker_color_circle="blue", marker_color_outside="gray40", font=("Helvetica Bold", 20))
        pos_2=(11.018884, -74.851916)

    if opciones.get() == "LeSalon":
        marker = map_widget.set_marker(11.019483, -74.850183, text="LeSalon", text_color="black",
                                marker_color_circle="blue", marker_color_outside="gray40", font=("Helvetica Bold", 20))
        pos_2=(11.019483, -74.850183)

    if opciones.get() == "Lab 1":
        marker = map_widget.set_marker(11.018446, -74.850587, text="Laboratirio 1", text_color="black",
                                marker_color_circle="blue", marker_color_outside="gray40", font=("Helvetica Bold", 20))
        pos_2=(11.018446, -74.850587)

    if opciones.get() == "Lab 2":
        marker = map_widget.set_marker(11.018750, -74.850508, text="Laboratirio 2", text_color="black",
                                 marker_color_circle="blue", marker_color_outside="gray40", font=("Helvetica Bold", 20))
        pos_2=(11.018750, -74.850508)

    if opciones.get() == "Lab 3":
        marker = map_widget.set_marker(11.018989, -74.850434, text="Laboratirio 3", text_color="black",
                                marker_color_circle="blue", marker_color_outside="gray40", font=("Helvetica Bold", 20))
        pos_2=(11.018989, -74.850434)

    if opciones.get() == "Lab 4":
        marker = map_widget.set_marker(11.018793, -74.851810, text="Laboratirio 4", text_color="black",
                                 marker_color_circle="blue", marker_color_outside="gray40", font=("Helvetica Bold", 20))
        pos_2=(11.018793, -74.851810)

    if opciones.get() == "Lab 5":
        marker = map_widget.set_marker(11.018135, -74.852001, text="Laboratirio 5", text_color="black",
                                marker_color_circle="blue", marker_color_outside="gray40", font=("Helvetica Bold", 20))
        pos_2=(11.018135, -74.852001)

    if opciones.get() == "CREE":
        marker = map_widget.set_marker(11.019625, -74.849638, text="CREE", text_color="black",
                                 marker_color_circle="blue", marker_color_outside="gray40", font=("Helvetica Bold", 20))
        pos_2=(11.019625, -74.849638)

    if opciones.get() == "Bienestar":
        marker = map_widget.set_marker(11.020029, -74.850332, text="Bienestar", text_color="black",
                                marker_color_circle="blue", marker_color_outside="gray40", font=("Helvetica Bold", 20))
        pos_2=(11.020029, -74.850332)

    if opciones.get() == "Bienestar bloque M":
        marker = map_widget.set_marker(11.019723, -74.848260, text="Bienestar bloque M", text_color="black",
                                marker_color_circle="blue", marker_color_outside="gray40", font=("Helvetica Bold", 20))
        pos_2=(11.019723, -74.848260)

        
    
    

        
    mybutton2 = Button(root, text=" Limpiar ", command=limpiar)
    mybutton2.place(x=610, y=572)

    path_1= map_widget.set_path([pos_1,pos_2])
    path_1.draw()

myButton = Button(root, text=" Buscar ", command=buscar) # Boton que almacena la input del usuario
myButton.place(x=510, y=572)

root.mainloop()
