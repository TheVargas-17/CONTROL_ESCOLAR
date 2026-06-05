import flet as ft

from models.calificacion_model import CalificacionModel
from models.materia_model import MateriaModel

def CalificacionesView(page):


    page.clean()

    usuario = page.usuario_actual

    materia = ft.Dropdown(
        label="Materia",
        width=350
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
        width=350
    )

    unidad2 = ft.TextField(
        label="Unidad 2",
        width=350
    )

    unidad3 = ft.TextField(
        label="Unidad 3",
        width=350
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
                    content=ft.Column(
                        [
                            ft.Text(
                                f"Materia: {r['materia']}",
                                weight=ft.FontWeight.BOLD
                            ),

                            ft.Text(
                                f"Unidad 1: {r['unidad1']}"
                            ),

                            ft.Text(
                                f"Unidad 2: {r['unidad2']}"
                            ),

                            ft.Text(
                                f"Unidad 3: {r['unidad3']}"
                            ),

                            ft.Text(
                                f"Promedio: {r['promedio']}"
                            ),

                            ft.Text(
                                "APROBADO"
                                if aprobado
                                else "REPROBADO",
                                color=(
                                    ft.Colors.GREEN
                                    if aprobado
                                    else ft.Colors.RED
                                )
                            )
                        ]
                    ),
                    bgcolor=(
                        ft.Colors.GREEN_100
                        if aprobado
                        else ft.Colors.RED_100
                    ),
                    padding=15,
                    border_radius=10
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

            exito, texto = CalificacionModel.guardar(
                usuario["id_usuario"],
                int(materia.value),
                u1,
                u2,
                u3
            )

            page.snack_bar = ft.SnackBar(
                content=ft.Text(texto)
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

    page.add(
        ft.Column(
            [
                ft.Text(
                    "CALIFICACIONES",
                    size=30,
                    weight=ft.FontWeight.BOLD
                ),

                ft.Text(
                    f"Alumno: {usuario['nombre_completo']}"
                ),

                materia,
                unidad1,
                unidad2,
                unidad3,

                ft.ElevatedButton(
                    "Guardar Calificación",
                    on_click=guardar
                ),

                ft.Divider(),

                ft.Text(
                    "Historial",
                    size=22,
                    weight=ft.FontWeight.BOLD
                ),

                tabla,

                ft.ElevatedButton(
                    "Volver al Dashboard",
                    on_click=lambda e:
                    __import__(
                        "views.dashboard",
                        fromlist=["DashboardView"]
                    ).DashboardView(page)
                )
            ],
            scroll=ft.ScrollMode.AUTO
        )
    )

    page.update()
