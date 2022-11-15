from typing import List

from pydantic import BaseModel


class Person(BaseModel):
    url: str
    name: str
    height: int
    mass: int
    hair_color: str
    skin_color: str
    eye_color: str
    birth_year: str
    gender: str
    homeworld: str
    films: List[str]
    species: List
    vehicles: List[str]
    starships: List[str]
