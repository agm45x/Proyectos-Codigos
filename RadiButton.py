import tkinter as tk

ventana=tk.Tk()
ventana.title("RadioButton")
ventana.geometry("500x500")


def mostrarSeleccion():
    
    resultado.config(text=f"Opcion seleccionada:{seleccionVar.get()}")

seleccionVar=tk.StringVar()

opcion1=tk.Radiobutton(ventana, text="Opcion 1", variable=seleccionVar, value="Opcion1")
opcion1.pack()

opcion2=tk.Radiobutton(ventana, text="Opcion 2", variable=seleccionVar, value="Opcion2")
opcion2.pack()

opcion3=tk.Radiobutton(ventana, text="Opcion 3", variable=seleccionVar, value="Opcion3")
opcion3.pack()

boton=tk.Button(ventana, text="Mostrar Seleccion", command=mostrarSeleccion)
boton.pack()

resultado=tk.Label(ventana, text="")
resultado.pack()



ventana.mainloop()