import requests

from src.models.person import Person


def get_person_by_id(host: str, id: int) -> Person:
    res = requests.get(
        f"{host}/people/{id}",
        verify=False
    )

    p = Person(**res.json())
    return p
