from dataclasses import dataclass


@dataclass
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

    def get_info(self) -> dict:
        candidate_info = dict(
            name=self.name,
            position=self.position,
            skills=', '.join(self.skills_list)
        )
        return candidate_info
