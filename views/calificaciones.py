import flet as ft

from models.calificacion_model import CalificacionModel

def CalificacionesView(page):

    page.clean()

    usuario = page.usuario_actual

    materia = ft.TextField(
        label="Materia",
        width=350
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

        registros = (
            CalificacionModel
            .obtener_por_usuario(
                usuario["id_usuario"]
            )
        )

        for r in registros:

            estado = (
                "APROBADO"
                if r["promedio"] >= 6
                else "REPROBADO"
            )

            tabla.controls.append(
                ft.Container(
                    content=ft.Column(
                        [
                            ft.Text(
                                f"Materia: {r['materia']}"
                            ),
                            ft.Text(
                                f"Promedio: {r['promedio']}"
                            ),
                            ft.Text(
                                estado
                            )
                        ]
                    ),
                    bgcolor=(
                        ft.Colors.GREEN_200
                        if r["promedio"] >= 6
                        else ft.Colors.RED_200
                    ),
                    padding=10
                )
            )

    def guardar(e):

        try:

            u1 = float(unidad1.value)
            u2 = float(unidad2.value)
            u3 = float(unidad3.value)

            if (
                u1 < 0 or u1 > 10 or
                u2 < 0 or u2 > 10 or
                u3 < 0 or u3 > 10
            ):

                print(
                    "Las calificaciones deben estar entre 0 y 10"
                )

                return

            exito, mensaje = (
                CalificacionModel.guardar(
                    usuario["id_usuario"],
                    materia.value,
                    u1,
                    u2,
                    u3
                )
            )

            print(mensaje)

            cargar_datos()

            page.update()

        except:

            print(
                "Datos inválidos"
            )

    cargar_datos()

    page.add(
        ft.Column(
            [
                ft.Text(
                    "CALIFICACIONES",
                    size=30,
                    weight=ft.FontWeight.BOLD
                ),

                materia,
                unidad1,
                unidad2,
                unidad3,

                ft.ElevatedButton(
                    "Guardar",
                    on_click=guardar
                ),

                ft.Divider(),

                tabla,

                ft.ElevatedButton(
                    "Volver",
                    on_click=lambda e:
                    __import__(
                        "views.dashboard",
                        fromlist=[
                            "DashboardView"
                        ]
                    ).DashboardView(page)
                )
            ],
            scroll=ft.ScrollMode.AUTO
        )
    )

    page.update()
