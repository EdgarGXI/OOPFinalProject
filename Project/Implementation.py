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

combo_4.place(x=40, y=340)



# Menu 5 = laboratorios
combo_5 = ttk.Combobox(
    state="readonly",
    values=["Bloque A", "Bloque B", "Bloque C", "Bloque D"]
)

#combo_5.place(x=40, y=420)



# Menu 6 = bambu
combo_6 = ttk.Combobox(
    state="readonly",
    values=["Bloque A", "Bloque B", "Bloque C", "Bloque D"]
)

#combo_6.place(x=40, y=500)



# Menu 7 = bambu
combo_7 = ttk.Combobox(
    state="readonly",
    values=["Bloque A", "Bloque B", "Bloque C", "Bloque D"]
)

#combo_7.place(x=40, y=500)



# Menu 8 = bambu
combo_8 = ttk.Combobox(
    state="readonly",
    values=["Bloque A", "Bloque B", "Bloque C", "Bloque D"]
)

#combo_8.place(x=40, y=500)



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
