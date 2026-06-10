import mysql.connector

def conectar_bd():
    try:
        conexion = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="control_escolar"
        )
        return conexion
    except mysql.connector.Error as error:
        print(f"Error al conectar con MySQL: {error}")
        return None