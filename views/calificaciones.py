
import flet as ft

from models.calificacion_model import CalificacionModel
from models.materia_model import MateriaModel

def CalificacionesView(page):

    page.clean()

    page.bgcolor = ft.Colors.INDIGO_900

    usuario = page.usuario_actual

    id_seleccionado = {"valor": None}

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

    def seleccionar(registro):

        id_seleccionado["valor"] = registro["id_calificacion"]

        unidad1.value = str(registro["unidad1"])
        unidad2.value = str(registro["unidad2"])
        unidad3.value = str(registro["unidad3"])

        page.update()

    def cargar_datos():

        tabla.controls.clear()

        registros = CalificacionModel.obtener_por_usuario(
            usuario["id_usuario"]
        )

        for r in registros:

            aprobado = r["promedio"] >= 6

            tarjeta = ft.Container(
                padding=15,
                border_radius=15,
                bgcolor=(
                    ft.Colors.GREEN_100
                    if aprobado
                    else ft.Colors.RED_100
                ),
                on_click=lambda e, reg=r: seleccionar(reg),
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

            tabla.controls.append(tarjeta)

    def guardar(e):

        try:

            u1 = float(unidad1.value)
            u2 = float(unidad2.value)
            u3 = float(unidad3.value)

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

            cargar_datos()
            page.update()

        except:

            pass

    def editar(e):

        if not id_seleccionado["valor"]:

            page.snack_bar = ft.SnackBar(
                content=ft.Text(
                    "Selecciona una tarjeta primero"
                )
            )

            page.snack_bar.open = True
            page.update()

            return

        try:

            u1 = float(unidad1.value)
            u2 = float(unidad2.value)
            u3 = float(unidad3.value)

            exito, mensaje = CalificacionModel.actualizar(
                id_seleccionado["valor"],
                u1,
                u2,
                u3
            )

            page.snack_bar = ft.SnackBar(
                content=ft.Text(mensaje)
            )

            page.snack_bar.open = True

            cargar_datos()
            page.update()

        except:

            pass

    def eliminar(e):

        if not id_seleccionado["valor"]:

            page.snack_bar = ft.SnackBar(
                content=ft.Text(
                    "Selecciona una tarjeta primero"
                )
            )

            page.snack_bar.open = True
            page.update()

            return

        exito, mensaje = CalificacionModel.eliminar(
            id_seleccionado["valor"]
        )

        page.snack_bar = ft.SnackBar(
            content=ft.Text(mensaje)
        )

        page.snack_bar.open = True

        id_seleccionado["valor"] = None

        unidad1.value = ""
        unidad2.value = ""
        unidad3.value = ""

        cargar_datos()
        page.update()

    cargar_datos()

    card = ft.Container(
        width=750,
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

                materia,
                unidad1,
                unidad2,
                unidad3,

                ft.Row(
                    [
                        ft.ElevatedButton(
                            "Guardar",
                            bgcolor=ft.Colors.BLUE,
                            color=ft.Colors.WHITE,
                            on_click=guardar
                        ),

                        ft.ElevatedButton(
                            "Editar",
                            bgcolor=ft.Colors.ORANGE,
                            color=ft.Colors.WHITE,
                            on_click=editar
                        ),

                        ft.ElevatedButton(
                            "Eliminar",
                            bgcolor=ft.Colors.RED,
                            color=ft.Colors.WHITE,
                            on_click=eliminar
                        )
                    ],
                    alignment=ft.MainAxisAlignment.CENTER
                ),

                ft.Divider(),

                ft.Text(
                    "Selecciona una tarjeta para editar o eliminar",
                    color=ft.Colors.BLACK,
                    weight=ft.FontWeight.BOLD
                ),

                tabla,

                ft.ElevatedButton(
                    "Volver al Dashboard",
                    width=300,
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
            [card],
            alignment=ft.MainAxisAlignment.CENTER
        )
    )

    page.update()

