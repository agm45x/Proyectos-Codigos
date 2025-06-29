import tkinter as tk

ventana=tk.Tk()

ventana.title("Personalizar Widget")
ventana.geometry("550x600")

etiqueta=tk.Label(ventana, text="Bienvenidos a Tkinter!",
                  bg="lightgreen", 
                  fg="darkblue",
                  width=50,
                  height=4,
                  font= ("Helvetica", 24, "italic"))
etiqueta.pack(pady=25)

def accionboton():
    etiqueta.config(text="Boton presionado", bg="blue")

boton=tk.Button(ventana, text="Haz clic aqui",
                font=("Arial",20, "bold"),
                bg="orange",
                fg="white",
                activebackground="red",
                activeforeground="yellow",
                width=15,
                command=accionboton
                
                )

boton.pack()

ventana.mainloop()