import flet as ft

from src.models.person import Person


class CardItemPerson(ft.UserControl):

    def __init__(self, person: Person) -> None:
        super().__init__()
        self.person = person

        def close_dlg(e):
            self.dlg_modal.open = False
            self.page.update()

        self.dlg_modal = ft.AlertDialog(
            modal=True,
            title=ft.Text("Please confirm"),
            content=ft.Text("Do you really want to delete all those files?"),
            actions=[
                ft.TextButton("Yes", on_click=close_dlg),
                ft.TextButton("No", on_click=close_dlg),
            ],
            actions_alignment="end",
            on_dismiss=lambda e: print("Modal dialog dismissed!"),
        )

    def open_dlg_modal(self, e):
        self.page.dialog = self.dlg_modal
        self.dlg_modal.open = True
        self.page.update()

    def build(self) -> ft.Card:
        card = ft.Card(
            content=ft.Container(
                content=ft.Column(
                    controls=[
                        ft.ListTile(
                            leading=ft.Icon(ft.icons.PERSON),
                            title=ft.Text(value=self.person.name),
                            subtitle=ft.Text(value=self.person.url),
                            on_click=self.open_dlg_modal
                        )
                    ]
                )
            )
        )

        return card
