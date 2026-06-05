from database.conexion import conectar_bd
import bcrypt


class UsuarioModel:

    @staticmethod
    def registrar(
        nombre_completo,
        curp,
        matricula,
        correo,
        celular,
        usuario,
        contrasenia,
        id_especialidad
    ):

        conexion = conectar_bd()

        if not conexion:
            return False, "Error de conexión"

        cursor = conexion.cursor()

        try:

            cursor.execute(
                """
                SELECT id_usuario
                FROM usuarios
                WHERE usuario = %s
                   OR matricula = %s
                   OR curp = %s
                   OR correo = %s
                """,
                (
                    usuario,
                    matricula,
                    curp,
                    correo
                )
            )

            existe = cursor.fetchone()

            if existe:
                return False, "Usuario ya registrado"

            password_hash = bcrypt.hashpw(
                contrasenia.encode("utf-8"),
                bcrypt.gensalt()
            )

            cursor.execute(
                """
                INSERT INTO usuarios
                (
                    nombre_completo,
                    curp,
                    matricula,
                    correo,
                    celular,
                    usuario,
                    contrasenia,
                    id_especialidad
                )
                VALUES
                (%s,%s,%s,%s,%s,%s,%s,%s)
                """,
                (
                    nombre_completo,
                    curp,
                    matricula,
                    correo,
                    celular,
                    usuario,
                    password_hash.decode("utf-8"),
                    id_especialidad
                )
            )

            conexion.commit()

            return True, "Usuario registrado"

        except Exception as e:

            return False, str(e)

        finally:

            cursor.close()
            conexion.close()

    @staticmethod
    def obtener_especialidad(id_usuario):

        conexion = conectar_bd()

        if not conexion:
            return "Sin especialidad"

        cursor = conexion.cursor()

        try:

            cursor.execute(
                """
                SELECT e.nombre_especialidad
                FROM usuarios u
                INNER JOIN especialidades e
                    ON u.id_especialidad = e.id_especialidad
                WHERE u.id_usuario = %s
                """,
                (id_usuario,)
            )

            dato = cursor.fetchone()

            if dato:
                return dato[0]

            return "Sin especialidad"

        except Exception:

            return "Sin especialidad"

        finally:

            cursor.close()
            conexion.close()