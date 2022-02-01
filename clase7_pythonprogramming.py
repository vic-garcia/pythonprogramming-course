#APLICACIONES DE ESCRITORIO
import tkinter as tk
from tkinter import ttk
 #ttk tiene widgets mas livianas y visualmente mas modernos.
from tkinter import messagebox 

verify=0
def boton_pres():  
    global verify
    if verify==0: 
       boton1.config(text="presionado")  #cambia el text cuando apreto
       verify=1
    else:
        boton1.config(text="aceptar")
        verify=0
def cerrar_app():
    if messagebox.askokcancel(title="Pregunta", message="Esta seguro?"):
        ventana.destroy()


def nuevo():
    print("Nuevo Archivo...")

def acerca_de():
    print("Acerca de...")

ventana = tk.Tk()
ventana.title("Principal clase 7")

#BARRA DE MENÚ
barra_de_menu= tk.Menu()
menu_archivo = tk.Menu(barra_de_menu, tearoff=0)
menu_archivo.add_command(label="Nuevo", command=nuevo)
menu_ayuda= tk.Menu(barra_de_menu, tearoff=0)
menu_ayuda.add_command(label="Acerca de", command=acerca_de)
barra_de_menu.add_cascade(label="Archivo", menu= menu_archivo) #boton en cascada
barra_de_menu.add_cascade(label="Ayuda", menu=menu_ayuda) #boton en cascada


#aqui tengo que darle medidas a la ventan principal y asociar el menu, siempre va despues del menu
ventana.config(width=550, height=400, menu=barra_de_menu)  #aqui asocie con menu, la barra de menu

#WIDGETS
#boton
boton1= tk.Button(text="Aceptar", command=boton_pres)
boton1.place(x=250, y=300, width=80, height=30)

boton_salir= ttk.Button(text="Salir", command=cerrar_app)
boton_salir.place(x=350, y=300,width=80, height=30 )

boton2= ttk.Button(text="Aceptar")
boton2.place(x=100, y=300)

#Etiquetas
label = ttk.Label(text="Ingrese su nombre:")
label.place(x=50, y=40)

#poner foto
"""imagen= tk.PhotoImage(file="logo.jpg") #tienen que estar en la misma carpeta
label_img=ttk.Label(image=imagen)
label_img.place(x=5, y=70)"""

#Cajas de texto
def mostrar_texto():
    print(entrada.get())

def modificar_texto():
   # entrada.insert(0,"Clase n 7")
    entrada.delete(0, tk.END)
entrada = ttk.Entry()
entrada.place(x=50, y=200)

boton_txt= ttk.Button(text="Mostrar texto", command= mostrar_texto)
boton_txt.place(x=50, y=240)

boton_modif_txt= ttk.Button(text="Modificar txt", command= modificar_texto)
boton_modif_txt.place(x=50, y=270, width=80, height=30)

#Listbox Listas
lista= tk.Listbox()
lista.insert(0,"Python", "Java", "C++", "Delphi")
lista.insert(tk.END, "Javascript")
lista.place(x=220, y=10, height=100)

#combobox
lista_desplegable= ttk.Combobox(values=["PERL", "JAVA","pYTHON","C"])
lista_desplegable.place(x=220, y=120)

#Checkbox
check_box_estado= tk.BooleanVar()
check_box= ttk.Checkbutton(text="opcion", variable=check_box_estado)
check_box_estado.set(True)
check_box.place(x=220, y=220)

"""#Cuadros de dialogos
#Retornan True o False
messagebox.askokcancel(titlie="Pregunta", message="Desea salir?")
messagebox.askyesno(title="Pregunta", message="Desea eliminar el archivo?")
messagebox.askretrycancel(title="No se pudo cargar el arch", message="reintentar?")

#Siemore retorna "ok"
messagebox.showinfo(title="Información", message="Se habilitó el acceso")
messagebox.showwarning(title="atención", message="debe ingresar un valor en el campo")
messagebox.showerror(title="error", message="")"""

ventana.mainloop()  #Cierra la sección 

