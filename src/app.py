import flet as ft

from src.navigation_rail import navigation_rail


class App:

    def __init__(self, page: ft.Page) -> None:
        self.page = page

        root = ft.Row(
            controls=[
                navigation_rail,
                ft.VerticalDivider(width=1),
                ft.Text("Hiii :)")
            ],
            expand=True
        )

        self.page.add(root)
