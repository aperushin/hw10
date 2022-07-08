import json
from candidate import Candidate


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
