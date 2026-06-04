import flet as ft

from views.login import LoginView
from views.registro import RegistroView

def main(page: ft.Page):

    page.title = "Control Escolar"
    page.window_width = 500
    page.window_height = 800
    page.scroll = ft.ScrollMode.AUTO

    def mostrar_login(e=None):
        LoginView(page)

    def mostrar_registro(e=None):
        RegistroView(page)

    page.mostrar_login = mostrar_login
    page.mostrar_registro = mostrar_registro

    mostrar_login()

ft.app(target=main)
