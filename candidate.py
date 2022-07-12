from dataclasses import dataclass


@dataclass(slots=True)
class Candidate:

    pk: int
    name: str
    picture: str
    position: str
    gender: str
    age: int
    skills: str

    def __post_init__(self):
        self.skills_list = self.skills.lower().split(', ')
