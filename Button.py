import tkinter as tk

def cambiartexto():
    mensajecambiente.config(text="Texto Cambiadooo")
def textooriginal():
    mensajecambiente.config(text="Texto Original")




ventana=tk.Tk()
ventana.title("Button")
ventana.geometry("600x600")

label=tk.Label(ventana, text="Botones:")
label.pack()

label.config(text="Funcionalidades:")

mensajecambiente=tk.Label(ventana, text="Texto Original")
mensajecambiente.pack()


boton=tk.Button(ventana, text="Cambiar texto", command=cambiartexto)
boton.pack()


boton2=tk.Button(ventana, text="Restablecer texto", command=textooriginal)
boton2.pack()
ventana.mainloop()
