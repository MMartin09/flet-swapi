import flet as ft
import requests

from src import components
from src.settings import get_settings
from src.swapi.people import get_person_by_id

settings = get_settings()

class App:

    def __init__(self, page: ft.Page) -> None:
        self.page = page
        self.page.title = settings.APP_TITLE

        # InsecureRequestWarning
        requests.packages.urllib3.disable_warnings()

        persons = [
            get_person_by_id(settings.SWAPI_URL, 1),
            get_person_by_id(settings.SWAPI_URL, 2),
            get_person_by_id(settings.SWAPI_URL, 3),
        ]

        list_view = ft.ListView()
        for person in persons:
            list_view.controls.append(components.CardItemPerson(name=person.name))

        self.page.add(list_view)
