import mysql.connector

class Conexion:

    def ConexionBaseDeDatos():
        try:
            conexion = mysql.connector.connect(user='root',
                                                password='123456',
                                                host='127.0.0.1',
                                                database='suministros',
                                                port='3306')
            print("Conexion correcta")
            return conexion
        except mysql.connector.Error as error:
            print("Error al conectarte a la base de datos {}".format(error))
            return conexion
        
Conexion.ConexionBaseDeDatos()
