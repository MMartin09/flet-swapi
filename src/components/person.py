import flet as ft


class CardItemPerson(ft.UserControl):

    def __init__(self, name: str) -> None:
        super().__init__()
        self.name = name

    def build(self) -> ft.Card:
        card = ft.Card(
            content=ft.Container(
                content=ft.Column(
                    controls=[
                        ft.ListTile(
                            title=ft.Text(value=self.name)
                        )
                    ]
                )
            )
        )

        return card
