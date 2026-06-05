from database.conexion import conectar_bd


class CalificacionModel:

    @staticmethod
    def guardar(
        id_usuario,
        id_materia,
        unidad1,
        unidad2,
        unidad3
    ):

        conexion = conectar_bd()

        cursor = conexion.cursor()

        promedio = (
            unidad1 +
            unidad2 +
            unidad3
        ) / 3

        try:

            cursor.execute(
                """
                INSERT INTO calificaciones
                (
                    id_usuario,
                    id_materia,
                    unidad1,
                    unidad2,
                    unidad3,
                    promedio
                )
                VALUES
                (%s,%s,%s,%s,%s,%s)
                """,
                (
                    id_usuario,
                    id_materia,
                    unidad1,
                    unidad2,
                    unidad3,
                    promedio
                )
            )

            conexion.commit()

            return True, "Calificación guardada"

        except Exception as e:

            return False, str(e)

        finally:

            cursor.close()
            conexion.close()

    @staticmethod
    def obtener_por_usuario(id_usuario):

        conexion = conectar_bd()

        cursor = conexion.cursor(dictionary=True)

        cursor.execute(
            """
            SELECT
                c.*,
                m.nombre_materia
            FROM calificaciones c
            INNER JOIN materias m
            ON c.id_materia = m.id_materia
            WHERE c.id_usuario = %s
            """,
            (id_usuario,)
        )

        datos = cursor.fetchall()

        cursor.close()
        conexion.close()

        return datos

    @staticmethod
    def promedio_general(id_usuario):

        conexion = conectar_bd()

        cursor = conexion.cursor()

        cursor.execute(
            """
            SELECT AVG(promedio)
            FROM calificaciones
            WHERE id_usuario = %s
            """,
            (id_usuario,)
        )

        resultado = cursor.fetchone()

        cursor.close()
        conexion.close()

        if resultado[0] is None:
            return 0

        return round(float(resultado[0]), 2)