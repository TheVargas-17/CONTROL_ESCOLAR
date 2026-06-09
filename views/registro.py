import flet as ft

from database.conexion import conectar_bd
from models.usuario_model import UsuarioModel

def RegistroView(page):


    page.clean()

    page.bgcolor = ft.Colors.BLUE_900

    nombre = ft.TextField(
        label="Nombre Completo",
        width=350,
        prefix_icon=ft.Icons.PERSON,
        border_radius=15,
        color=ft.Colors.BLACK,
        label_style=ft.TextStyle(color=ft.Colors.BLACK),
        cursor_color=ft.Colors.BLUE,
    )

    curp = ft.TextField(
        label="CURP",
        width=350,
        border_radius=15,
        color=ft.Colors.BLACK,
        label_style=ft.TextStyle(color=ft.Colors.BLACK),
        cursor_color=ft.Colors.BLUE,    
    )

    matricula = ft.TextField(
        label="Matrícula",
        width=350,
        border_radius=15,
        color=ft.Colors.BLACK,
        label_style=ft.TextStyle(color=ft.Colors.BLACK),
        cursor_color=ft.Colors.BLUE, 
    )

    correo = ft.TextField(
        label="Correo",
        width=350,
        prefix_icon=ft.Icons.EMAIL,
        border_radius=15,
        color=ft.Colors.BLACK,
        label_style=ft.TextStyle(color=ft.Colors.BLACK),
        cursor_color=ft.Colors.BLUE, 
    )

    celular = ft.TextField(
        label="Celular",
        width=350,
        prefix_icon=ft.Icons.PHONE,
        border_radius=15,
        color=ft.Colors.BLACK,
        label_style=ft.TextStyle(color=ft.Colors.BLACK),
        cursor_color=ft.Colors.BLUE, 
    )

    usuario = ft.TextField(
        label="Usuario",
        width=350,
        border_radius=15,
        color=ft.Colors.BLACK,
        label_style=ft.TextStyle(color=ft.Colors.BLACK),
        cursor_color=ft.Colors.BLUE, 
    )

    contrasenia = ft.TextField(
        label="Contraseña",
        password=True,
        can_reveal_password=True,
        width=350,
        prefix_icon=ft.Icons.LOCK,
        border_radius=15,
        color=ft.Colors.BLACK,
        label_style=ft.TextStyle(color=ft.Colors.BLACK),
        cursor_color=ft.Colors.BLUE, 
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

            page.snack_bar = ft.SnackBar(
                content=ft.Text(
                    "Todos los campos son obligatorios"
                )
            )

            page.snack_bar.open = True
            page.update()

            return

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

        page.snack_bar = ft.SnackBar(
            content=ft.Text(mensaje)
        )

        page.snack_bar.open = True

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

    card = ft.Container(
        width=550,
        padding=40,
        border_radius=25,
        bgcolor=ft.Colors.WHITE,
        shadow=ft.BoxShadow(
            blur_radius=20,
            spread_radius=2
        ),
        content=ft.Column(
            [
                ft.Icon(
                    ft.Icons.PERSON_ADD,
                    size=90,
                    color=ft.Colors.GREEN
                ),

                ft.Text(
                    "REGISTRO DE ALUMNO",
                    size=30,
                    weight=ft.FontWeight.BOLD,
                    color=ft.Colors.BLUE_800
                ),

                ft.Divider(),

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
                    width=350,
                    height=50,
                    bgcolor=ft.Colors.GREEN,
                    color=ft.Colors.WHITE,
                    on_click=registrar
                ),

                ft.TextButton(
                    "Ya tengo cuenta",
                    on_click=lambda e:
                    page.mostrar_login()
                )
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER
        )
    )

    page.add(
        ft.Row(
            [
                card
            ],
            alignment=ft.MainAxisAlignment.CENTER
        )
    )

    page.update()

