from Conexion1 import *

class AAlmacen():
    
    def mostrarMateriales():
        try:
            cone = Conexion.ConexionBaseDeDatos()
            if cone is None:
                return []
            cursor = cone.cursor()
            cursor.execute("SELECT * FROM suministros.almacen;")
            miResultado = cursor.fetchall()
            cone.commit()
            cone.close()
            return miResultado
        except mysql.connector.Error as error:
            print("Error de muestra de datos {}".format(error))
            
    def busca_producto(nombre_producto):
        try:
            cone = Conexion.ConexionBaseDeDatos()
            if cone is None:
                    return []
            cursor = cone.cursor()
            sql = "SELECT * FROM productos WHERE Codigo_de_material = {}".format(nombre_producto)
            cursor.execute(sql)
            nombreX = cursor.fetchall()
            cone.commit()
            cone.close()
            return nombreX 
        except mysql.connector.Error as error:
            print("Error de muestra de datos {}".format(error))
            return []        
        

            
