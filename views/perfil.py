import flet as ft

from models.usuario_model import UsuarioModel


def PerfilView(page):

    page.clean()

    usuario = page.usuario_actual

    especialidad = UsuarioModel.obtener_especialidad(
        usuario["id_usuario"]
    )

    page.add(
        ft.Column(
            [
                ft.Text(
                    "PERFIL DEL ALUMNO",
                    size=30,
                    weight=ft.FontWeight.BOLD
                ),

                ft.Divider(),

                ft.Image(
                    src="assets/user.png",
                    width=150,
                    height=150
                ),

                ft.Text(
                    f"Nombre: {usuario['nombre_completo']}"
                ),

                ft.Text(
                    f"CURP: {usuario['curp']}"
                ),

                ft.Text(
                    f"Matrícula: {usuario['matricula']}"
                ),

                ft.Text(
                    f"Correo: {usuario['correo']}"
                ),

                ft.Text(
                    f"Celular: {usuario['celular']}"
                ),

                ft.Text(
                    f"Especialidad: {especialidad}"
                ),

                ft.Divider(),

                ft.ElevatedButton(
                    "Volver al Dashboard",
                    on_click=lambda e:
                    __import__(
                        "views.dashboard",
                        fromlist=["DashboardView"]
                    ).DashboardView(page)
                )
            ],
            horizontal_alignment=
            ft.CrossAxisAlignment.CENTER
        )
    )

    page.update()