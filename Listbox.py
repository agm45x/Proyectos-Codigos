import tkinter as tk

ventana=tk.Tk()
ventana.title("ListBox")
ventana.geometry("500x500")

def MostrarSeleccion():
    
    seleccion= lista.get(lista.curselection())
    resultado.config(text=f"seleccionastes: {seleccion}")
    
    

lista= tk.Listbox(ventana, selectmode=tk.SINGLE)
lista.pack()

opciones=["Azul", "Rojo", "Negro", "Amarillo"]
for opcion in opciones:
    lista.insert(tk.END, opcion)
    
boton=tk.Button(ventana, text="Mostrar Seleccion", command=MostrarSeleccion)
boton.pack()

resultado=tk.Label(ventana, text="")
resultado.pack()





ventana.mainloop()

