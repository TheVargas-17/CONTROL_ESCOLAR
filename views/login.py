import flet as ft
import bcrypt

from database.conexion import conectar_bd

def LoginView(page):


    page.clean()

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

    def iniciar_sesion(e):

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

            print("Error de conexión")
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

            print("LOGIN CORRECTO")

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

    page.add(
        ft.Column(
            [
                ft.Text(
                    "INICIAR SESIÓN",
                    size=30,
                    weight=ft.FontWeight.BOLD
                ),

                usuario,

                contrasenia,

                ft.ElevatedButton(
                    "Ingresar",
                    on_click=iniciar_sesion
                ),

                ft.TextButton(
                "¿No tienes cuenta? Regístrate",
                on_click=lambda e: page.mostrar_registro()
            )
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER
        )
    )

    page.update()
