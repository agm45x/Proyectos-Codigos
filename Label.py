import tkinter as tk

ventana=tk.Tk()
ventana.title("Label")
ventana.geometry("700x700")

label= tk.Label(ventana, text="Hola, bienvenidos a Tkinter!")
label.pack()

label2=tk.Label(ventana, text="Este es un segundo label")
label2.pack()

ventana.mainloop()