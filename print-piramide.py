import time
from tkinter import *
from tkinter import ttk

#Variables para contar el tiempo
start_time = None
start_time_piramide = None

def update_clock(): #Función que actualiza el reloj global
    global start_time
    if start_time is None:
        start_time = time.time()
    elapsed_time = time.time() - start_time
    reloj_label.config(text=f"Reloj: {int(elapsed_time)} segundos")
    root.after(1000, update_clock)  # Actualiza el reloj cada 1000 milisegundos


def imprimir_simbolo(): #Función que imprime la pirámide
    global start_time_piramide
    simbolo = simbolo_entry.get()
    numero = int(numero_entry.get())
    resultado_text.delete(1.0, END)
    
    #Impresión de la pirámide
    for i in range(1, numero + 1):
        resultado_text.insert(END, ' '*(numero - i) + simbolo*(2 * i - 1) + ' '*(numero - i) + '\n')
    start_time_piramide = time.time() #Inicia el tiempo de la pirámide en pantalla
    
    #Limpiar campos
    simbolo_entry.delete(0, END)
    numero_entry.delete(0, END)
    tiempo_label.config(text="")

def limpiar_piramide(): #Función que limpia la pirámide y muestra el tiempo en pantalla
    global start_time_piramide
    resultado_text.delete(1.0, END)
    if start_time_piramide is not None:
        elapsed_time = time.time() - start_time_piramide
        tiempo_label.config(text=f"La pirámide estuvo en pantalla durante {int(elapsed_time)} segundos.")
        start_time_piramide = None #reinicia el tiempo de la piramide, para una nueva impresión

#Creación de la app
root = Tk()

#Estilos 
style = ttk.Style()
style.configure("Dark.TFrame", background='#3e4e50')
style.configure("Plat.TButton", background='#e1e6e1')

#Frames
content = ttk.Frame(root, borderwidth=10, relief='ridge' ,width=200, height=200, style="Dark.TFrame")
dibujo = ttk.Frame(content,  width=100, height=100)
mainframe = ttk.Frame(content, borderwidth=5, relief="ridge", 
    width=100, height=100, padding="3 3 12 12")

#Campos y etiquetas
reloj_label = ttk.Label(mainframe, text="Reloj:") #Etiqueta del reloj global
tiempo_label = ttk.Label(mainframe, text="") #Etiqueta del tiempo de la pirámide en pantalla

#Etiqueta y campo del símbolo
simbolo_label = ttk.Label(mainframe, text="Símbolo:", style="Plat.TLabel") 
simbolo_entry = ttk.Entry(mainframe) 

#Etiqueta y campo del número
numero_label = ttk.Label(mainframe, text="Número:")
numero_entry = ttk.Entry(mainframe)

#Campo para mostar la pirámide
resultado_text = Text(dibujo, width=50, height=20)
resultado_text.pack()

#Botones
imprimir_btn = ttk.Button(mainframe, text="Imprimir", command=imprimir_simbolo, style="Plat.TButton")
limpiar_btn = ttk.Button(mainframe, text="Limpiar", command=limpiar_piramide, style="Plat.TButton")

#Grid layout
content.grid(column=0, row=0)
dibujo.grid(column=0, row=0, columnspan=3, rowspan=3, padx=10)
mainframe.grid(column=4, row=0, columnspan=6, rowspan=6, padx=10)

reloj_label.grid(column=6, row=1, pady=20)

simbolo_label.grid(column=4, row=2, pady=5, padx=10)
simbolo_entry.grid(column=4, row=3, pady=10, padx=10)

numero_label.grid(column=6, row=2, pady=5)
numero_entry.grid(column=6, row=3, pady=10)

imprimir_btn.grid(column=4, row=5)
limpiar_btn.grid(column=6, row=5, pady=10)

tiempo_label.grid(column=4, row=6, columnspan=3)

#Inicialización de la app
root.after(1000, update_clock)  # Inicia el reloj 1 segundo después de abrir el programa
root.mainloop()

