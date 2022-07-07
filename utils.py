import json
from typing import List


def load_candidates(filename: str) -> List[dict]:
    with open(filename, encoding='utf8') as f:
        data = json.load(f)
    return data
