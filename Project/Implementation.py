from tkinter import messagebox, ttk
import tkinter as tk
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
root.geometry("1300x720") # Tamaño ventana
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

# Menu 1 -> Bloques
combo = ttk.Combobox( 
    state="readonly", # Permite solo escoger opciones
    values=["Bloque A", "Bloque B", "Bloque C", "Bloque D"] # Opciones menú 1
)

text_1 = Label(root, text="Bloques", font=("Calibri", 12)) # Texto encima del menú
text_1.place(x=85, y=123) # Coordenadas texto
combo.place(x=40, y=150) # Coordenadas menú



# Menu 2 -> Oficinas
combo_2 = ttk.Combobox(
    state="readonly", # Permite solo escoger opciones
    values=["CREE", "Bienestar", "Bienestar bloque M"] # Opciones menú 2
)

text_2 = Label(root, text="Oficinas", font=("Calibri", 12)) # Texto encima del menú
text_2.place(x=85, y=212) # Coordenadas texto
combo_2.place(x=40, y=240) # Coordenadas menú



# Menu 3 = servicios
combo_3 = ttk.Combobox(
    state="readonly", # Permite solo escoger opciones
    values=["Biblioteca", "Casa de Estudio", "duNord Graphique", "Km5","duNord Store ", "Cajero G", "Cajero F", "Cajero C", "Corresponsal", "M.Transmetro", "Museo", "Centro Médico", "LeSalon"] # Opciones menú 3
)

text_3 = Label(root, text="Servicios", font=("Calibri", 12)) # Texto encima del menú
text_3.place(x=85, y=300) # Coordenadas texto
combo_3.place(x=40, y=330) # Coordenadas menú



# Menu 4 = restaurantes
combo_4 = ttk.Combobox(
    state="readonly", # Permite solo escoger opciones
    values=["LePetit", "duNord Plaza", "1966", "Café duNord", "duNord Terrase", "El Camion", "La Gofreria"] # Opciones menú 4
)

text_4 = Label(root, text="Restaurantes", font=("Calibri", 12)) # Texto encima del menú
text_4.place(x=70, y=390) # Coordenadas texto
combo_4.place(x=40, y=420) # Coordenadas menú



# Menu 5 = laboratorios
combo_5 = ttk.Combobox(
    state="readonly", # Permite solo escoger opciones
    values=["1", "2", "3", "4","5"] # Opciones menú 5
)

text_5 = Label(root, text="Laboratorios", font=("Calibri", 12)) # Texto encima del menú
text_5.place(x=1155, y=120) # Coordenadas texto
combo_5.place(x=1125, y=150) # Coordenadas menú



# Menu 6 = bambu
combo_6 = ttk.Combobox(
    state="readonly", # Permite solo escoger opciones
    values=["1", "2"] # Opciones menú 6
)

text_6 = Label(root, text="Bambús", font=("Calibri", 12)) # Texto encima del menú
text_6.place(x=1165, y=210) # Coordenadas texto
combo_6.place(x=1125, y=240) # Coordenadas menú



# Menu 7 = Puerta
combo_7 = ttk.Combobox(
    state="readonly", # Permite solo escoger opciones
    values=["4", "7"] # Opciones menú 7
)

text_7 = Label(root, text="Puertas", font=("Calibri", 12)) # Texto encima del menú
text_7.place(x=1170, y=300) # Coordenadas texto
combo_7.place(x=1125, y=330) # Coordenadas menú



# Menu 8 = SDU
combo_8 = ttk.Combobox(
    state="readonly", # Permite solo escoger opciones
    values=["B", "G", "K"] # Opciones menú 8
)

text_8 = Label(root, text="Salas de estudio", font=("Calibri", 12)) # Texto encima del menú
text_8.place(x=1140, y=390) # Coordenadas texto
combo_8.place(x=1125, y=420) # Coordenadas menú



# <-------------------- Almacenar input de donde esta el usuario -------------------->

esp2 = Label(root, text = " ") # Espacio
ask = Label(root, text = "Indique en donde se encuentra: ", font=("Arial", 14))
esp3 = Label(root, text = " ")
user2 = Entry(root, width=50) # Input box del usuario
esp1 = Label(root, text = " ")
ask.pack()
esp1.pack()
esp2.pack()
user2.pack()
esp3.pack()




if user2.get() == "Museo":
    marker_3 = map_widget.set_marker(11.020059, -74.851332, text="Tower", text_color="green",
                                 marker_color_circle="black", marker_color_outside="gray40", font=("Helvetica Bold", 24))


# <--------------------------------------------- Boton del input del usuario ----------------------------------------------->
def myClick():
    boton=Label(root, text="Escribiste: " + user2.get()) # Imprime input del usuario
    boton.pack()

    if user2.get() == "Museo":
        marker_3 = map_widget.set_marker(11.020059, -74.851332, text="Usted está aqui", text_color="black",
                                 marker_color_circle="black", marker_color_outside="gray40", font=("Helvetica Bold", 20))
    if user2.get() == "Puerta 7":
        marker_3 = map_widget.set_marker(11.019204, -74.849621, text="Usted está aqui", text_color="black",
                                marker_color_circle="red", marker_color_outside="gray40", font=("Helvetica Bold", 20))
    if user2.get() == "Bloque B":
        marker_3 = map_widget.set_marker(11.018760, -74.851008, text="Usted está aqui", text_color="black",
                                 marker_color_circle="black", marker_color_outside="gray40", font=("Helvetica Bold", 20))
    if user2.get() == "Puerta 7":
        marker_3 = map_widget.set_marker(11.019204, -74.849621, text="Usted está aqui", text_color="black",
                                marker_color_circle="red", marker_color_outside="gray40", font=("Helvetica Bold", 20))
    if combo_3.get() == "Casa de Estudio":
        marker_3 = map_widget.set_marker(11.017580, -74.850313, text="Casa de estudio", text_color="black",
                                marker_color_circle="blue", marker_color_outside="gray40", font=("Helvetica Bold", 20))
    if combo_2.get() == "CREE":
        marker_3 = map_widget.set_marker(11.019625, -74.849638, text="CREE", text_color="black",
                                marker_color_circle="blue", marker_color_outside="gray40", font=("Helvetica Bold", 20))
    if combo_4.get() == "Café duNord":
        marker_3 = map_widget.set_marker(11.019539, -74.850265, text="Café duNord", text_color="black",
                                marker_color_circle="blue", marker_color_outside="gray40", font=("Helvetica Bold", 20))
    if combo_8.get() == "B":
        marker_3 = map_widget.set_marker(11.018778, -74.850265, text="SDU 8", text_color="black",
                                marker_color_circle="blue", marker_color_outside="gray40", font=("Helvetica Bold", 20))


myButton = Button(root, text="Buscar", command=myClick) # Boton que almacena la input del usuario
myButton.pack()


root.mainloop()
