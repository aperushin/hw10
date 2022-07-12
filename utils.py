import json
from candidate import Candidate
from constants import CANDIDATES_JSON


def load_json(filename: str) -> list[dict]:
    with open(filename, encoding='utf8') as f:
        data = json.load(f)
    return data


def load_candidates(filename: str) -> list[Candidate]:
    data = load_json(filename)
    result = list()
    for candidate in data:
        result.append(Candidate(**candidate))
    return result


def get_all() -> list[Candidate]:
    candidates = load_candidates(CANDIDATES_JSON)
    return candidates


def get_by_pk(pk) -> Candidate | None:
    candidates: list[Candidate] = load_candidates(CANDIDATES_JSON)
    for candidate in candidates:
        if candidate.pk == pk:
            return candidate
    return None


def get_by_skill(skill) -> list[Candidate]:
    candidates = load_candidates(CANDIDATES_JSON)
    result = [c for c in candidates if skill.lower() in c.skills_list]
    return result
