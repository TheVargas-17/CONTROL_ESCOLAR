import flet as ft
import bcrypt

from database.conexion import conectar_bd


def LoginView(page):

    page.clean()

    page.bgcolor = ft.Colors.BLUE_900
    usuario = ft.TextField(
        label="Usuario",
        width=350,
        prefix_icon=ft.Icons.PERSON,
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

    def iniciar_sesion(e):

        try:

            if not usuario.value or not contrasenia.value:

                page.snack_bar = ft.SnackBar(
                    content=ft.Text(
                        "Debes llenar todos los campos"
                    )
                )

                page.snack_bar.open = True
                page.update()

                return

            conexion = conectar_bd()

            if not conexion:

                page.snack_bar = ft.SnackBar(
                    content=ft.Text(
                        "Error de conexión a la base de datos"
                    )
                )

                page.snack_bar.open = True
                page.update()

                return

            cursor = conexion.cursor(dictionary=True)

            cursor.execute(
                """
                SELECT *
                FROM usuarios
                WHERE usuario = %s
                """,
                (usuario.value,)
            )

            datos = cursor.fetchone()

            cursor.close()
            conexion.close()

            if not datos:

                page.snack_bar = ft.SnackBar(
                    content=ft.Text(
                        "Usuario no encontrado"
                    )
                )

                page.snack_bar.open = True
                page.update()

                return

            password_correcta = bcrypt.checkpw(
                contrasenia.value.encode("utf-8"),
                datos["contrasenia"].encode("utf-8")
            )

            if password_correcta:

                page.usuario_actual = datos

                from views.dashboard import DashboardView

                DashboardView(page)

            else:

                page.snack_bar = ft.SnackBar(
                    content=ft.Text(
                        "Contraseña incorrecta"
                    )
                )

                page.snack_bar.open = True
                page.update()

        except Exception as error:

            print(f"Error Login: {error}")

            page.snack_bar = ft.SnackBar(
                content=ft.Text(
                    "Ocurrió un error al iniciar sesión"
                )
            )

            page.snack_bar.open = True
            page.update()

    card = ft.Container(
        width=500,
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
                    ft.Icons.SCHOOL,
                    size=90,
                    color=ft.Colors.BLUE
                ),

                ft.Text(
                    "CONTROL ESCOLAR",
                    size=32,
                    weight=ft.FontWeight.BOLD,
                    color=ft.Colors.BLUE_800
                ),

                ft.Text(
                    "Iniciar Sesión",
                    size=18,
                    color=ft.Colors.GREY_700
                ),

                ft.Divider(),

                usuario,

                contrasenia,

                ft.ElevatedButton(
                    "Ingresar",
                    width=350,
                    height=50,
                    bgcolor=ft.Colors.BLUE,
                    color=ft.Colors.WHITE,
                    on_click=iniciar_sesion
                ),

                ft.TextButton(
                    "¿No tienes cuenta? Regístrate",
                    on_click=lambda e:
                    page.mostrar_registro()
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