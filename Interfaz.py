import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from time import strftime


from Conexion1 import * 

from Almacen import *

class FormularioAlmacen:
    
    global base
    base = None
    
    global textBoxCodMaterial
    textBoxCodMaterial = None
    
    global textBoxMatDescripcion 
    textBoxMatDescripcion = None
    
    global textBoxMatTotal
    textBoxMatTotal = None
    
    global textBoxMatAgregar
    textBoxMatAgregar = None
    
    global textBoxAsignarMat
    textBoxAsignarMat = None
    
    global textBoxFecha
    textBoxFecha = None
    
    global textBoxMatProy
    textBoxMatProy = None
    
    global textBoxAsignarProy
    textBoxAsignarProy = None
    
    global groupBox
    groupBox = None
    
    global textBoxCodMate
    textBoxCodMate = None
    
    global textBoxSipro
    textBoxSipro = None
    
    global nombre_producto
    nombre_producto = None
    
    global nombre_buscado
    nombre_buscado = None
    
    global tree
    tree = None
    
def Formulario():
        
    global base
    global textBoxCodMaterial
    global textBoxMatDescripcion
    global textBoxMatTotal
    global textBoxMatAgregar
    global textBoxAsignarMat
    global textBoxFecha
    global textBoxMatProy
    global textBoxAsignarProy
    global groupBox
    global textBoxCodMate
    global textBoxSipro
    global tree
        
        
        
        
    try:
        base = Tk()
        base.geometry("1200x1000")
        base.title("Buscar Material - Almacen")
            
        #BUSCADOR 1
            
        groupBox = LabelFrame(base,text="Ingreso de Materiales", padx=5,pady=5)
        groupBox.pack(side=LEFT,anchor='nw',padx=10,pady=10,fill='both',expand=True)
        groupBox.config(width=60,height=80)
            
        LabelCodMaterial = Label(groupBox,text="Codigo de Material",width=13,font=("Arial",12),padx=10,pady=5).grid(row=0,column=0)
        textBoxCodMaterial = Entry(groupBox).grid(row=0,column=1,padx=10,pady=5)
            
        LabelMatDescripcion = Label(groupBox,text="Descripcion del Material",width=20,font=("Arial",12),padx=10,pady=5).grid(row=1,column=0)
        textBoxMatDescripcion = Entry(groupBox).grid(row=1,column=1,padx=10,pady=5)
            
        LabelMatTotal = Label(groupBox,text="Total en Almacen",width=13,font=("Arial",12),padx=10,pady=5).grid(row=3,column=0)
        textBoxMatTotal = Entry(groupBox).grid(row=3,column=1,padx=10,pady=5)
            
        Button(groupBox, text="BUSCAR",command= buscar_nombre ,width=10).grid(row=4,columnspan=2)
            
        #Buscador 2
            
        LabelMatAgregar = Label(groupBox,text="Cantidad a ingresar",width=13,font=("Arial",12),padx=10,pady=5).grid(row=5,column=0)
        textBoxMatAgregar = Entry(groupBox).grid(row=5,column=1,padx=10,pady=5)
            
        LabelAsignarMat = Label(groupBox,text="Asignar Material",width=13,font=("Arial",12),padx=10,pady=5).grid(row=6,column=0)
        AsignarMateriales = tk.StringVar()
        Asigna = ttk.Combobox(groupBox, values=["Ingeniero 1","Ingeniero 2", "Ingeniero 3", "Almacen"],textvariable=AsignarMateriales,width=28)
        Asigna.grid(row=6,column=1,padx=5,pady=5)
        AsignarMateriales.set("Asigne mat. a una persona")
            
        LabelAsignarProy = Label(groupBox,text="Asignar Material a Proyecto",width=20,font=("Arial",12),padx=10,pady=5).grid(row=7,column=0)
        textBoxAsignarProy = Entry(groupBox).grid(row=7,column=1,padx=10,pady=5)
            
        LabelMatProy = Label(groupBox,text="Proveedor",width=13,font=("Arial",12),padx=10,pady=5).grid(row=8,column=0)
        proveedor = tk.StringVar()
        AsignaPro = ttk.Combobox(groupBox, values=["Triple A", "CRDA"],textvariable=proveedor,width=28)
        AsignaPro.grid(row=8,column=1,padx=5,pady=5)
        proveedor.set("¿Quien suministra el material?")
            
        LabelFecha = Label(groupBox,text="Fecha de Ingreso",width=13,font=("Arial",12),padx=10,pady=5).grid(row=9,column=0)
        textBoxFecha = Entry(groupBox).grid(row=9,column=1,padx=10,pady=5)
            
        Button(groupBox, text="AGREGAR", width=10).grid(row=10,columnspan=2)
            
        #BUSCADOR 3
        LabelCodMate = Label(groupBox,text="Codigo de Material",width=13,font=("Arial",12),padx=10,pady=15).grid(row=11,column=0)
        textBoxCodMate = Entry(groupBox).grid(row=11,column=1,padx=10,pady=5)
            
        LabelSipro = Label(groupBox,text="SIPRO",width=13,font=("Arial",12)).grid(row=12,column=0,padx=10,pady=5)
        textBoxSipro = Entry(groupBox).grid(row=12,column=1,padx=10,pady=5)
            
        LabelInge = Label(groupBox,text="Consulta Proyectos",width=20,font=("Arial",12)).grid(row=13,column=0,padx=10,pady=5)
        Inge = tk.StringVar()
        AsignaInge = ttk.Combobox(groupBox, values=["Ingeniero 1","Ingeniero 2","Ingeniero 3"],textvariable=Inge,width=28)
        AsignaInge.grid(row=13,column=1,padx=5,pady=5)
        Inge.set("Seleccione un ingeniero")
           
        Button(groupBox, text="CONSULTAR", width=10).grid(row=14,columnspan=2)
         
        #Tabla
           
        groupBox2 = LabelFrame(base, text="Materiales Cargados en Proyectos")
        groupBox2.pack(side=RIGHT,anchor='ne',padx=10,pady=10,fill='both',expand=True)
        groupBox2.config(width=120,height=140)
             
        tree = ttk.Treeview(groupBox2, columns=("CODIGO MATERIAL","MATERIAL - DESCRIPCION","GRUPO","INGENIERO 1",
                                                    "INGENIERO 2","INGENIERO 3","ALMACEN","TOTAL","UNIDADES DE MEDIDA"),show='headings',height=20)
            
        tree.column("# 1",anchor=CENTER, width=100)
        tree.column("# 2", width=270)
        tree.column("# 3",anchor=CENTER, width=50)
        tree.column("# 4",anchor=CENTER, width=50)
        tree.column("# 5",anchor=CENTER, width=50)
        tree.column("# 6",anchor=CENTER, width=50)
        tree.column("# 7",anchor=CENTER, width=70)
        tree.column("# 8",anchor=CENTER, width=50)
        tree.column("# 9",anchor=CENTER, width=100)
            
        tree.heading("# 1",text="COD MATERIAL")
        tree.heading("# 2",text="MATERIAL - DESCRIPCION")
        tree.heading("# 3",text="GRUPO")
        tree.heading("# 4",text="ING 1")
        tree.heading("# 5",text="ING 2")
        tree.heading("# 6",text="ING 3")
        tree.heading("# 7",text="ALMACEN")
        tree.heading("# 8",text="TOTAL")
        tree.heading("# 9",text="UN-MEDIDA")
            
        for row in AAlmacen.mostrarMateriales():
            tree.insert("","end",values=row)
            
        tree.pack()
            
        base.mainloop()
            
    except ValueError as error:
        print("Error al monstrar la interfaz, error: {}".format(error))
    
def actualizarTreeView():
    global tree
    
    try:
        tree.delete(*tree.get_children())
        datos = AAlmacen.mostrarMateriales()
        for row in AAlmacen.mostrarMateriales():
            tree.insert("","end", values=row)
    
    except ValueError as error:
        print("Error al actualizar tabla {}".format(error))
    
def buscar_nombre():
        
    global nombre_producto,nombre_buscado,tree,nombreX
    
    try:    
        nombre_producto = str(textBoxCodMaterial)
        nombre_producto = str("'" + nombre_producto + "'")
        nombre_buscado = AAlmacen.busca_producto(nombre_producto)
        i = -1
        tree.delete(*tree.get_children())
        actualizarTreeView()
        
        for dato in nombre_buscado:
            i= i+1                       
            tree.insert('',i, text = str(dato[0]), values=dato[1:])
    except mysql.connector.Error as error:
        print("No se encuentra nada {}".format(error))
    
    
Formulario()         
    
