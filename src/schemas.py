from pydantic import BaseModel
from typing import List


class Relation(BaseModel):
    name: str
    relation: str


class CharacterInfo(BaseModel):
    name: str
    storyTitle: str
    summary: str
    relations: List[Relation]
    characterType: str
