import flet as ft

from database.conexion import conectar_bd
from models.usuario_model import UsuarioModel


def RegistroView(page):

    page.clean()

    nombre = ft.TextField(
        label="Nombre Completo",
        width=350
    )

    curp = ft.TextField(
        label="CURP",
        width=350
    )

    matricula = ft.TextField(
        label="Matrícula",
        width=350
    )

    correo = ft.TextField(
        label="Correo",
        width=350
    )

    celular = ft.TextField(
        label="Celular",
        width=350
    )

    usuario = ft.TextField(
        label="Usuario",
        width=350
    )

    contrasenia = ft.TextField(
        label="Contraseña",
        password=True,
        can_reveal_password=True,
        width=350
    )

    especialidad = ft.Dropdown(
        label="Especialidad",
        width=350
    )

    conexion = conectar_bd()

    if conexion:

        cursor = conexion.cursor()

        cursor.execute(
            """
            SELECT
                id_especialidad,
                nombre_especialidad
            FROM especialidades
            """
        )

        datos = cursor.fetchall()

        for item in datos:

            especialidad.options.append(
                ft.dropdown.Option(
                    key=str(item[0]),
                    text=item[1]
                )
            )

        cursor.close()
        conexion.close()

    def registrar(e):

        print("BOTON PRESIONADO")

        if (
            not nombre.value
            or not curp.value
            or not matricula.value
            or not correo.value
            or not celular.value
            or not usuario.value
            or not contrasenia.value
            or not especialidad.value
        ):

            print("Todos los campos son obligatorios")
            return

        try:

            exito, mensaje = UsuarioModel.registrar(
                nombre.value,
                curp.value,
                matricula.value,
                correo.value,
                celular.value,
                usuario.value,
                contrasenia.value,
                int(especialidad.value)
            )

            print("RESULTADO:", exito)
            print("MENSAJE:", mensaje)

            if exito:

                nombre.value = ""
                curp.value = ""
                matricula.value = ""
                correo.value = ""
                celular.value = ""
                usuario.value = ""
                contrasenia.value = ""
                especialidad.value = None

            page.update()

        except Exception as error:

            print("ERROR:", error)

        

    page.update()

    page.add(
        ft.Column(
            [
                ft.Text(
                    "REGISTRO DE ALUMNO",
                    size=30,
                    weight=ft.FontWeight.BOLD
                ),

                nombre,
                curp,
                matricula,
                correo,
                celular,
                usuario,
                contrasenia,
                especialidad,

                ft.ElevatedButton(
                    "Registrarse",
                    on_click=registrar
                ),

                ft.TextButton(
                    "Ya tengo cuenta",
                    on_click=lambda e: page.mostrar_login()
                )
            ],
            horizontal_alignment=
            ft.CrossAxisAlignment.CENTER
        )
    )

    page.update()