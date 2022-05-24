from tkinter import messagebox, ttk
import tkinter as tk
import tkintermapview
from tkinter import *
from tkinter import simpledialog
import pandas as pd

# <------------------------------------ Base de datos -------------------------------------->

db = pd.read_csv("https://raw.githubusercontent.com/EdgarGXI/OOPFinalProject/main/database.csv")
#print(db)



# <------------------------------- Configuración de ventana -------------------------------->

root= Tk()
root.title("Mapa - Universidad del norte")
root.geometry("1300x720")
root.resizable(width=False, height=False)
esp3 = Label(root, text=" ")
esp3.pack()
title = Label(root, text = "CompaniUN  -  Mapa Universidad del Norte", font=("Calibri", 25))
title.pack()

my_label= LabelFrame(root)
my_label.pack(pady=10, padx=20)


# <-------------------------------- Mostrar mapa en pantalla ------------------------------>

map_widget = tkintermapview.TkinterMapView(my_label, width=850, height=420,corner_radius=20)
map_widget.set_position(11.018985992247588, -74.85068279601066)
map_widget.pack()
map_widget.set_zoom(18)



# <---------------------- Botones en pantalla ------------------------>

# Menu 1 = bloques
combo = ttk.Combobox(
    state="readonly",
    values=["Bloque A", "Bloque B", "Bloque C", "Bloque D"]
)

text_1 = Label(root, text="Bloques", font=("Calibri", 12))
text_1.place(x=85, y=123)
combo.place(x=40, y=150)
m = combo.get()
print(m)


# Menu 2 = oficinas
combo_2 = ttk.Combobox(
    state="readonly",
    values=["CREE", "Bienestar", "Bienestar bloque M"]
)

text_2 = Label(root, text="Oficinas", font=("Calibri", 12))
text_2.place(x=85, y=218)
combo_2.place(x=40, y=240)



# Menu 3 = servicios
combo_3 = ttk.Combobox(
    state="readonly",
    values=["Biblioteca", "Casa de Estudio", "duNord Graphique", "Km5","duNord Store ", "Cajero G", "Cajero F", "Cajero C", "Corresponsal", "M.Transmetro", "Museo", "Centro Médico", "LeSalon"]
)

text_3 = Label(root, text="Servicios")
text_3.place(x=85, y=308)
combo_3.place(x=40, y=330)



# Menu 4 = restaurantes
combo_4 = ttk.Combobox(
    state="readonly",
    values=["LePetit", "duNord Plaza", "1966", "Café duNord", "duNord Terrase", "El Camion", "La Gofreria"]
)

text_4 = Label(root, text="Restaurantes", font=("Calibri", 12))
text_4.place(x=70, y=390)
combo_4.place(x=40, y=420)


# Menu 5 = laboratorios
combo_5 = ttk.Combobox(
    state="readonly",
    values=["1", "2", "3", "4","5"]
)
text_5 = Label(root, text="Laboratorios", font=("Calibri", 12))
text_5.place(x=1155, y=120)
combo_5.place(x=1125, y=150)



# Menu 6 = bambu
combo_6 = ttk.Combobox(
    state="readonly",
    values=["1", "2"]
)
text_6 = Label(root, text="Bambús", font=("Calibri", 12))
text_6.place(x=1165, y=210)
combo_6.place(x=1125, y=240)



# Menu 7 = Puerta
combo_7 = ttk.Combobox(
    state="readonly",
    values=["4", "7"]
)
text_7 = Label(root, text="Restaurantes", font=("Calibri", 12))
text_7.place(x=1155, y=300)
combo_7.place(x=1125, y=330)



# Menu 8 = SDU
combo_8 = ttk.Combobox(
    state="readonly",
    values=["B", "G", "K"]
)
text_8 = Label(root, text="Restaurantes", font=("Calibri", 12))
text_8.place(x=1155, y=390)
combo_8.place(x=1125, y=420)



#esp1 = Label(root, text = " ")
#esp2 = Label(root, text = " ")
#ask = Label(root, text = "Indique hacia donde quiere ir: ", font=("Arial", 14))
#user2 = Entry(root, width=50)
#ask.pack()
#esp1.pack()
#user2.pack()


#def myClick():
  #  boton=Label(root, text="Escribiste: " + user2.get()) 
 #   boton.pack()

#myButton = Button(root, text="Buscar", command=myClick)
#myButton.pack()


root.mainloop()
