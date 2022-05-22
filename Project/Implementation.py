import tkintermapview
from tkinter import *
##from tkinter import tkintermapview
from tkinter import simpledialog

root= Tk()
##root.configure(bg="gray")
root.title("Mapa - Universidad del norte")
root.geometry("900x700")
esp3 = Label(root, text=" ")
esp3.pack()
title = Label(root, text = "CompaniUN", font=("Calibri", 20))
title.pack()
##user = simpledialog.askstring(title = "CompaniUN", prompt = "Indique un lugar:")

my_label= LabelFrame(root)
my_label.pack(pady=20)

map_widget = tkintermapview.TkinterMapView(my_label, width=800, height=500,corner_radius=2)
map_widget.set_position(11.018985992247588, -74.85068279601066)
map_widget.pack()
map_widget.set_zoom(20)


esp1 = Label(root, text = " ")
esp2 = Label(root, text = " ")
ask = Label(root, text = "Indique hacia donde quiere ir: ", font=("Arial", 14))
user2 = Entry(root, width=50)
ask.pack()
esp1.pack()
user2.pack()


def myClick():
    boton=Label(root, text="Escribiste: " + user2.get()) 
    boton.pack()

myButton = Button(root, text="Buscar", command=myClick)
myButton.pack()


root.mainloop()

