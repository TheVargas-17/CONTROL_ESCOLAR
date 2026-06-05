from database.conexion import conectar_bd


class MateriaModel:

    @staticmethod
    def obtener_materias():

        conexion = conectar_bd()

        if not conexion:
            return []

        cursor = conexion.cursor(dictionary=True)

        cursor.execute("""
            SELECT *
            FROM materias
            ORDER BY semestre, nombre_materia
        """)

        datos = cursor.fetchall()

        cursor.close()
        conexion.close()

        return datos