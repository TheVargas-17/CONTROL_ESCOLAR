import flet as ft

from models.calificacion_model import CalificacionModel
from models.usuario_model import UsuarioModel

def DashboardView(page):

    page.clean()
    page.bgcolor = ft.Colors.BLUE_900

    usuario = page.usuario_actual

    promedio = CalificacionModel.promedio_general(
        usuario["id_usuario"]
    )

    especialidad = UsuarioModel.obtener_especialidad(
        usuario["id_usuario"]
    )

    card = ft.Container(
        width=700,
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
                    size=100,
                    color=ft.Colors.BLUE
                ),

                ft.Text(
                    "CONTROL ESCOLAR",
                    size=32,
                    weight=ft.FontWeight.BOLD,
                    color=ft.Colors.BLACK
                ),

                ft.Divider(),

                ft.Container(
                    padding=20,
                    border_radius=15,
                    bgcolor=ft.Colors.BLUE_100,
                    content=ft.Column(
                        [
                            ft.Text(
                                f"Bienvenido {usuario['nombre_completo']}",
                                size=22,
                                weight=ft.FontWeight.BOLD,
                                color=ft.Colors.BLACK
                            ),

                            ft.Text(
                                f"Matrícula: {usuario['matricula']}",
                                color=ft.Colors.BLACK
                            ),

                            ft.Text(
                                f"Correo: {usuario['correo']}",
                                color=ft.Colors.BLACK
                            ),

                            ft.Text(
                                f"CURP: {usuario['curp']}",
                                color=ft.Colors.BLACK
                            ),

                            ft.Text(
                                f"Especialidad: {especialidad}",
                                color=ft.Colors.BLACK
                            )
                        ]
                    )
                ),

                ft.Divider(),

                ft.Container(
                    padding=20,
                    border_radius=15,
                    bgcolor=ft.Colors.GREY_200,
                    content=ft.Column(
                        [
                            ft.Text(
                                "PROMEDIO GENERAL",
                                size=18,
                                weight=ft.FontWeight.BOLD,
                                color=ft.Colors.BLACK
                            ),

                            ft.Text(
                                str(promedio),
                                size=40,
                                weight=ft.FontWeight.BOLD,
                                color=(
                                    ft.Colors.GREEN
                                    if promedio >= 6
                                    else ft.Colors.RED
                                )
                            )
                        ],
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER
                    )
                ),

                ft.Divider(),

                ft.Text(
                    "Menú Principal",
                    size=20,
                    weight=ft.FontWeight.BOLD,
                    color=ft.Colors.BLACK
                ),

                ft.ElevatedButton(
                    "Calificaciones",
                    icon=ft.Icons.SCHOOL,
                    width=300,
                    height=50,
                    bgcolor=ft.Colors.BLUE,
                    color=ft.Colors.WHITE,
                    on_click=lambda e:
                    __import__(
                        "views.calificaciones",
                        fromlist=["CalificacionesView"]
                    ).CalificacionesView(page)
                ),

                ft.ElevatedButton(
                    "Perfil",
                    icon=ft.Icons.PERSON,
                    width=300,
                    height=50,
                    bgcolor=ft.Colors.GREEN,
                    color=ft.Colors.WHITE,
                    on_click=lambda e:
                    __import__(
                        "views.perfil",
                        fromlist=["PerfilView"]
                    ).PerfilView(page)
                ),

                ft.ElevatedButton(
                    "Cerrar Sesión",
                    icon=ft.Icons.LOGOUT,
                    width=300,
                    height=50,
                    bgcolor=ft.Colors.RED,
                    color=ft.Colors.WHITE,
                    on_click=lambda e:
                    __import__(
                        "views.login",
                        fromlist=["LoginView"]
                    ).LoginView(page)
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