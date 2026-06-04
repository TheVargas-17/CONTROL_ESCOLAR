import flet as ft

def DashboardView(page):

    page.clean()

    usuario = page.usuario_actual

    page.add(
        ft.Column(
            [
                ft.Text(
                    "DASHBOARD",
                    size=30,
                    weight=ft.FontWeight.BOLD
                ),

                ft.Text(
                    f"Bienvenido {usuario['nombre_completo']}"
                ),

                ft.Text(
                    f"Matrícula: {usuario['matricula']}"
                ),

                ft.Text(
                    f"Correo: {usuario['correo']}"
                ),

                ft.Text(
                    f"CURP: {usuario['curp']}"
                )
            ]
        )
    )

    page.update()
