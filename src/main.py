import flet as ft

from src.app import App


def main() -> None:
    ft.app(
        target=App,
        view=ft.FLET_APP
    )


if __name__ == "__main__":
    main()
