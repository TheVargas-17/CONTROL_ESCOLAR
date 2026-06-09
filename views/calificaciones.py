import flet as ft

from models.calificacion_model import CalificacionModel
from models.materia_model import MateriaModel

def CalificacionesView(page):


    page.clean()

    page.bgcolor = ft.Colors.INDIGO_900

    usuario = page.usuario_actual

    materia = ft.Dropdown(
        label="Materia",
        width=350,
        color=ft.Colors.BLACK
    )

    for m in MateriaModel.obtener_materias():

        materia.options.append(
            ft.dropdown.Option(
                key=str(m["id_materia"]),
                text=f'{m["nombre_materia"]} - Sem {m["semestre"]}'
            )
        )

    unidad1 = ft.TextField(
        label="Unidad 1",
        width=350,
        border_radius=15,
        color=ft.Colors.BLACK
    )

    unidad2 = ft.TextField(
        label="Unidad 2",
        width=350,
        border_radius=15,
        color=ft.Colors.BLACK
    )

    unidad3 = ft.TextField(
        label="Unidad 3",
        width=350,
        border_radius=15,
        color=ft.Colors.BLACK
    )

    tabla = ft.Column()

    def cargar_datos():

        tabla.controls.clear()

        registros = CalificacionModel.obtener_por_usuario(
            usuario["id_usuario"]
        )

        for r in registros:

            aprobado = r["promedio"] >= 6

            tabla.controls.append(
                ft.Container(
                    padding=15,
                    border_radius=15,
                    bgcolor=(
                        ft.Colors.GREEN_100
                        if aprobado
                        else ft.Colors.RED_100
                    ),
                    content=ft.Column(
                        [
                            ft.Text(
                                r["nombre_materia"],
                                size=18,
                                weight=ft.FontWeight.BOLD,
                                color=ft.Colors.BLACK
                            ),

                            ft.Text(
                                f"Unidad 1: {r['unidad1']}",
                                color=ft.Colors.BLACK
                            ),

                            ft.Text(
                                f"Unidad 2: {r['unidad2']}",
                                color=ft.Colors.BLACK
                            ),

                            ft.Text(
                                f"Unidad 3: {r['unidad3']}",
                                color=ft.Colors.BLACK
                            ),

                            ft.Text(
                                f"Promedio: {r['promedio']}",
                                weight=ft.FontWeight.BOLD,
                                color=ft.Colors.BLACK
                            ),

                            ft.Text(
                                "APROBADO"
                                if aprobado
                                else "REPROBADO",
                                color=(
                                    ft.Colors.GREEN
                                    if aprobado
                                    else ft.Colors.RED
                                ),
                                weight=ft.FontWeight.BOLD
                            )
                        ]
                    )
                )
            )

    def guardar(e):

        if not materia.value:

            page.snack_bar = ft.SnackBar(
                content=ft.Text(
                    "Debes seleccionar una materia"
                )
            )

            page.snack_bar.open = True
            page.update()

            return

        try:

            u1 = float(unidad1.value)
            u2 = float(unidad2.value)
            u3 = float(unidad3.value)

            if (
                u1 < 0 or u1 > 10 or
                u2 < 0 or u2 > 10 or
                u3 < 0 or u3 > 10
            ):

                page.snack_bar = ft.SnackBar(
                    content=ft.Text(
                        "Las calificaciones deben estar entre 0 y 10"
                    )
                )

                page.snack_bar.open = True
                page.update()

                return

            exito, mensaje = CalificacionModel.guardar(
                usuario["id_usuario"],
                int(materia.value),
                u1,
                u2,
                u3
            )

            page.snack_bar = ft.SnackBar(
                content=ft.Text(mensaje)
            )

            page.snack_bar.open = True

            if exito:

                materia.value = None
                unidad1.value = ""
                unidad2.value = ""
                unidad3.value = ""

                cargar_datos()

            page.update()

        except Exception:

            page.snack_bar = ft.SnackBar(
                content=ft.Text(
                    "Las unidades deben ser números válidos"
                )
            )

            page.snack_bar.open = True
            page.update()

    cargar_datos()

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
                    size=90,
                    color=ft.Colors.BLUE
                ),

                ft.Text(
                    "CALIFICACIONES",
                    size=30,
                    weight=ft.FontWeight.BOLD,
                    color=ft.Colors.BLUE_800
                ),

                ft.Text(
                    f"Alumno: {usuario['nombre_completo']}",
                    color=ft.Colors.BLACK
                ),

                ft.Divider(),

                materia,
                unidad1,
                unidad2,
                unidad3,

                ft.ElevatedButton(
                    "Guardar Calificación",
                    width=350,
                    height=50,
                    bgcolor=ft.Colors.BLUE,
                    color=ft.Colors.WHITE,
                    on_click=guardar
                ),

                ft.Divider(),

                ft.Text(
                    "Historial de Calificaciones",
                    size=22,
                    weight=ft.FontWeight.BOLD,
                    color=ft.Colors.BLACK
                ),

                tabla,

                ft.ElevatedButton(
                    "Volver al Dashboard",
                    width=300,
                    height=50,
                    bgcolor=ft.Colors.GREY_700,
                    color=ft.Colors.WHITE,
                    icon=ft.Icons.ARROW_BACK,
                    on_click=lambda e:
                    __import__(
                        "views.dashboard",
                        fromlist=["DashboardView"]
                    ).DashboardView(page)
                )
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            scroll=ft.ScrollMode.AUTO
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
   
