import flet as ft
import requests

from src.app import App
from src.models.person import Person


def main_old() -> None:
    ft.app(
        target=App,
        view=ft.FLET_APP
    )


def get_preson_by_id(host: str, id: int) -> Person:
    res = requests.get(
        f"{host}/people/{id}",
        verify=False
    )

    p = Person(**res.json())

    return p


def main() -> None:
    swapi_url: str = "https://swapi.dev/api/"

    res = requests.get(
        f"{swapi_url}/films/",
        verify=False
    )

    print(res.json())

    #res = requests.get(
    #    f"{swapi_url}/people/",
    #    params={"page": 4},
    #    verify=False
    #)
    #print(res.json())

    get_preson_by_id(swapi_url, 6)


if __name__ == "__main__":
    main()
