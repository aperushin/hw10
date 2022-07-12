from dataclasses import dataclass
from constants import CANDIDATE_TEMPLATE


@dataclass
class Candidate:

    pk: int
    name: str
    picture: str
    position: str
    gender: str
    age: int
    skills: str | list[str]

    def __post_init__(self):
        """Make self.skills a list of lower-case strings"""
        if isinstance(self.skills, str):
            self.skills = self.skills.lower().split(', ')
        elif isinstance(self.skills, list):
            self.skills = [x.lower() for x in self.skills]

    def get_info(self) -> str:
        candidate_info = CANDIDATE_TEMPLATE.format(
            name=self.name,
            position=self.position,
            skills=', '.join(self.skills)
        )
        return candidate_info
