import flet as ft

from models.usuario_model import UsuarioModel

def PerfilView(page):

    
    page.clean()

    page.bgcolor = ft.Colors.INDIGO_900

    usuario = page.usuario_actual

    especialidad = UsuarioModel.obtener_especialidad(
        usuario["id_usuario"]
    )

    card = ft.Container(
        width=650,
        padding=40,
        border_radius=25,
        bgcolor=ft.Colors.WHITE,
        shadow=ft.BoxShadow(
            blur_radius=20,
            spread_radius=2
        ),
        content=ft.Column(
            [
                ft.Image(
                    src="assets/user.png",
                    width=150,
                    height=150
                ),

                ft.Text(
                    "PERFIL DEL ALUMNO",
                    size=30,
                    weight=ft.FontWeight.BOLD,
                    color=ft.Colors.BLUE_800
                ),

                ft.Divider(),

                ft.Container(
                    padding=20,
                    border_radius=15,
                    bgcolor=ft.Colors.BLUE_100,
                    content=ft.Column(
                        [
                            ft.Text(
                                f"Nombre: {usuario['nombre_completo']}",
                                size=18,
                                color=ft.Colors.BLACK
                            ),

                            ft.Text(
                                f"CURP: {usuario['curp']}",
                                size=18,
                                color=ft.Colors.BLACK
                            ),

                            ft.Text(
                                f"Matrícula: {usuario['matricula']}",
                                size=18,
                                color=ft.Colors.BLACK
                            ),

                            ft.Text(
                                f"Correo: {usuario['correo']}",
                                size=18,
                                color=ft.Colors.BLACK
                            ),

                            ft.Text(
                                f"Celular: {usuario['celular']}",
                                size=18,
                                color=ft.Colors.BLACK
                            ),

                            ft.Text(
                                f"Especialidad: {especialidad}",
                                size=18,
                                weight=ft.FontWeight.BOLD,
                                color=ft.Colors.BLACK
                            )
                        ]
                    )
                ),

                ft.Divider(),

                ft.ElevatedButton(
                    "Volver al Dashboard",
                    width=300,
                    height=50,
                    bgcolor=ft.Colors.BLUE,
                    color=ft.Colors.WHITE,
                    icon=ft.Icons.ARROW_BACK,
                    on_click=lambda e:
                    __import__(
                        "views.dashboard",
                        fromlist=["DashboardView"]
                    ).DashboardView(page)
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

