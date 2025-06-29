import tkinter as tk

ventana=tk.Tk()
ventana.title("Frame")
ventana.geometry("700x700")
ventana.resizable(False, False)

marco=tk.Frame(ventana, width=300, height=200, bg="lightgray",borderwidth=2, relief="solid")
marco.pack_propagate(False)
marco.pack(pady=200)

ventana.mainloop()