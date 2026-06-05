import flet as ft
from models.calificacion_model import CalificacionModel
from models.usuario_model import UsuarioModel


def DashboardView(page):

    page.clean()

    usuario = page.usuario_actual

    promedio = (
        CalificacionModel
        .promedio_general(
            usuario["id_usuario"]
        )
    )

    especialidad = (
            UsuarioModel.obtener_especialidad(
                usuario["id_usuario"]
            )
        )

    page.add(
        ft.Column(
            [
                ft.Text(
                    "DASHBOARD",
                    size=30,
                    weight=ft.FontWeight.BOLD
                ),

                ft.Divider(),

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
                ),
                ft.Text(
                    f"Especialidad: {especialidad}"
                ),
    
                ft.Divider(),

                ft.Text(
                    f"Promedio General: {promedio}",
                    size=20,
                    weight=ft.FontWeight.BOLD,
                    color=(
                        ft.Colors.GREEN
                        if promedio >= 6
                        else ft.Colors.RED
                    )
                ),

                ft.Divider(),
                ft.Dropdown(
                    label="Semestre",
                    width=250,
                    options=[
                        ft.dropdown.Option("1"),
                        ft.dropdown.Option("2"),
                        ft.dropdown.Option("3"),
                        ft.dropdown.Option("4"),
                        ft.dropdown.Option("5"),
                        ft.dropdown.Option("6")
                    ]
                ),

                ft.ElevatedButton(
                    "Calificaciones",
                    on_click=lambda e:
                    __import__(
                        "views.calificaciones",
                        fromlist=["CalificacionesView"]
                    ).CalificacionesView(page)
                ),

                ft.ElevatedButton(
                    "Perfil",
                    on_click=lambda e:
                    __import__(
                        "views.perfil",
                        fromlist=["PerfilView"]
                    ).PerfilView(page)
                ),

                ft.ElevatedButton(
                    "Cerrar Sesión",
                    on_click=lambda e:
                    __import__(
                        "views.login",
                        fromlist=["LoginView"]
                    ).LoginView(page)
                )
            ]
        )
    )

    page.update()