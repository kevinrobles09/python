from tkinter import *
from tkinter import messagebox
import sqlite3


root=Tk()
miFrame=Frame(root, width=800, height=600)
miFrame.pack()

#-------------menú crear base de datos---------------------------------------------
def conexionBBDD():
		
	try:
		miConexion=sqlite3.connect("Usuarios")
		miCursor=miConexion.cursor()

		miCursor.execute('''
			CREATE TABLE datos(
			ID INTEGER PRiMARY KEY,
			NOMBRE VARCHAR(50),
			PASSWORD VARCHAR(50),
			APELLIDO VARCHAR(50),
			DIRECCION VARCHAR(50),
			COMENTARIOS VARCHAR(100))
			''')

		messagebox.showinfo("BBDD", "BBDD creada con exito")

	except:
		messagebox.showwarning("Atencion", "La BBDD ya existe")

def salirAplicacion ():
	valor=messagebox.askquestion("Salir", "¿Deseas salir de la aplicación?")

	if valor=="yes":
		root.destroy()

#-------------menú borrar ------------------------------------------------

def limpiarCampos():
	miIdentificacion.set("")
	miNombre.set("")
	miPass.set("")
	miApellido.set("")
	miDireccion.set("")
	textoComentario.delete(1.0, END)

#-----------------menú CRUD-------------------------------------

def Create():
	try:
		miConexion=sqlite3.connect("Usuarios")
		miCursor=miConexion.cursor()

		#miCursor.execute("INSERT INTO datos VALUES (NULL , '"+ miNombre.get()+
		#	"','" + miPass.get()+
		#	"','" + miApellido.get()+
		#	"','" + miDireccion.get()+
		#	"','" + textoComentario.get("1.0", END) +"')")


		misValores=[
			miIdentificacion.get(),
			miNombre.get(),
			miPass.get(),
			miApellido.get(),
			miDireccion.get(),
			textoComentario.get("1.0", END)
		]
	
		miCursor.execute("INSERT INTO datos (ID,NOMBRE,PASSWORD,APELLIDO,DIRECCION,COMENTARIOS)VALUES (?,?,?,?,?,?)", misValores)

		miConexion.commit()
		messagebox.showinfo("BBDD", "Registro exitoso")
	except:
		messagebox.showwarning("ERROR", "El campo ID solo acepta números")

def Read():

	try: 
		miConexion=sqlite3.connect("Usuarios")
		miCursor=miConexion.cursor()

		miCursor.execute("SELECT * FROM datos WHERE ID=" + miIdentificacion.get())

		consulta=miCursor.fetchall()

		for Usuario in consulta:
			miIdentificacion.set(Usuario[0])
			miNombre.set(Usuario[1])
			miPass.set(Usuario[2])
			miApellido.set(Usuario[3])
			miDireccion.set(Usuario[4])
			textoComentario.insert(1.0, Usuario[5])

		miConexion.commit()

	except:
		messagebox.showinfo("Read", "No se encontró el Usuario")

def Update():

	try:
		miConexion=sqlite3.connect("Usuarios")
		miCursor=miConexion.cursor()

		"""miCursor.execute("UPDATE datos SET NOMBRE='"+ miNombre.get() +
			"', PASSWORD='" + miPass.get() +
			"', APELLIDO='" + miApellido.get() +
			"', DIRECCION='" + miDireccion.get() +
			"', COMENTARIOS='" + textoComentario.get("1.0", END) +
			"' WHERE ID=" + miIdentificacion.get())"""

		misValores=[
			miNombre.get(),
			miPass.get(),
			miApellido.get(),
			miDireccion.get(),
			textoComentario.get("1.0", END)
		]

		miCursor.execute("UPDATE datos SET NOMBRE=?, PASSWORD=?,APELLIDO=?,DIRECCION=?,COMENTARIOS=?" +
			"WHERE ID=" + miIdentificacion.get(), (misValores))

		miConexion.commit()
		messagebox.showinfo("BBDD", "Registro Actualizado")
	except:
		messagebox.showwarning("ERROR", "No se puede Actualizar")


def Delete():

	try:
		miConexion=sqlite3.connect("Usuarios")
		miCursor=miConexion.cursor()

		miCursor.execute("DELETE FROM datos WHERE ID=" + miIdentificacion.get())
		evaluar=miIdentificacion.get()

		miConexion.commit()
		messagebox.showinfo("BBDD", "Registro eliminado")
	except:
		messagebox.showwarning("ERROR", "No se puede eliminar")




#------------label y demas-----------------------------------------------------------
miIdentificacion=StringVar()
miIdentificacion.set("")
idLabel=Label(miFrame, text="ID:")
idLabel.grid(row=0, column=1, sticky="e", padx=10, pady=10)
cuadroID=Entry(miFrame, textvariable=miIdentificacion)
cuadroID.grid(row=0, column=2, padx=10, pady=10)

miNombre=StringVar()
#miIdentificacion.set("")
nombreLabel=Label(miFrame, text="Nombre:")
nombreLabel.grid(row=1, column=1, sticky="e", padx=10, pady=10)
cuadroNombre=Entry(miFrame, textvariable=miNombre)
cuadroNombre.grid(row=1, column=2, padx=10, pady=10)

miPass=StringVar()
#miIdentificacion.set("")
passLabel=Label(miFrame, text="Password:")
passLabel.grid(row=2, column=1, sticky="e", padx=10, pady=10)
cuadroPass=Entry(miFrame, textvariable=miPass)
cuadroPass.grid(row=2, column=2, padx=10, pady=10)
cuadroPass.config(show="?")

miApellido=StringVar()
#miIdentificacion.set("")
apellidoLabel=Label(miFrame, text="Apellido:")
apellidoLabel.grid(row=3, column=1, sticky="e", padx=10, pady=10)
cuadroApellido=Entry(miFrame, textvariable=miApellido)
cuadroApellido.grid(row=3, column=2, padx=10, pady=10)

miDireccion=StringVar()
#miIdentificacion.set("")
direccionLabel=Label(miFrame, text="Dirección:")
direccionLabel.grid(row=4, column=1, sticky="e", padx=10, pady=10)
cuadroDireccion=Entry(miFrame, textvariable=miDireccion)
cuadroDireccion.grid(row=4, column=2, padx=10, pady=10)
 

comentariosLabel=Label(miFrame, text="Comentarios:")
comentariosLabel.grid(row=5, column=1, sticky="e", padx=10, pady=10)
textoComentario=Text(miFrame, width=16, height=5)
textoComentario.grid(row=5, column=2, padx=10, pady=10)
scrollvertical=Scrollbar(miFrame, command=textoComentario.yview)
scrollvertical.grid(row=5, column=3, sticky="nsew")
textoComentario.config(yscrollcommand=scrollvertical.set)



#--------------barra de menus-------------------------------------
barraMenus=Menu(root)
root.config(menu=barraMenus, width=300, height=300)

BBDD=Menu(barraMenus, tearoff=0)
BBDD.add_command(label="Crear BBDD", command=conexionBBDD)
BBDD.add_command(label="Salir", command=salirAplicacion)

Borrar=Menu(barraMenus, tearoff=0)
Borrar.add_command(label="Borrar campos", command=limpiarCampos)


CRUD=Menu(barraMenus, tearoff=0)
CRUD.add_command(label="Crear", command=Create)
CRUD.add_command(label="Leer", command=Read)
CRUD.add_command(label="Actualizar", command=Update)
CRUD.add_command(label="Eliminar", command=Delete)

archivoAyuda=Menu(barraMenus)

barraMenus.add_cascade(label="BBDD", menu=BBDD)
barraMenus.add_cascade(label="Borrar", menu=Borrar)
barraMenus.add_cascade(label="CRUD", menu=CRUD)
barraMenus.add_cascade(label="Ayuda", menu=archivoAyuda)

#-------------botones----------------------------------------------
miFrame2=Frame(root)
miFrame2.pack()

botonCrear=Button(miFrame2,text="Create", command=Create)
botonCrear.grid(row=1, column=0, sticky="e", padx=10, pady=10)

botonRead=Button(miFrame2,text="Read", command=Read)
botonRead.grid(row=1, column=1, sticky="e", padx=10, pady=10)

botonUpdate=Button(miFrame2,text="Update",command=Update)
botonUpdate.grid(row=1, column=2, sticky="e", padx=10, pady=10)

botonDelete=Button(miFrame2,text="Delete", command=Delete)
botonDelete.grid(row=1, column=3, sticky="e", padx=10, pady=10)


#-----------------------------------------------------------------------
root.mainloop()