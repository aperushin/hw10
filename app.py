from flask import Flask
from utils import load_candidates
from constants import CANDIDATES_JSON, CANDIDATE_TEMPLATE

app = Flask(__name__)


@app.route('/')
def get_all():
    data = load_candidates(CANDIDATES_JSON)
    result = ['<pre>']

    for candidate in data:
        candidate_info = CANDIDATE_TEMPLATE.format(
            name=candidate['name'],
            position=candidate['position'],
            skills=candidate['skills']
        )
        result.append(candidate_info)

    result.append('</pre>')
    return '\n'.join(result)


@app.route('/candidates/<int:pk>')
def get_by_pk(pk):
    data = load_candidates(CANDIDATES_JSON)
    for candidate in data:
        if candidate['pk'] == pk:
            result = [
                f'<img src="{candidate["picture"]}">',
                '<pre>',
            ]
            candidate_info = CANDIDATE_TEMPLATE.format(
                name=candidate['name'],
                position=candidate['position'],
                skills=candidate['skills']
            )
            result.append(candidate_info)
            result.append('</pre>')
            return '\n'.join(result)
    return f'Кандидата с номером {pk} не существует'


@app.route('/skills/<skill>')
def get_by_skill(skill):
    data = load_candidates(CANDIDATES_JSON)
    result = ['<pre>']
    for candidate in data:
        if skill in candidate['skills'].lower().split(', '):
            candidate_info = CANDIDATE_TEMPLATE.format(
                name=candidate['name'],
                position=candidate['position'],
                skills=candidate['skills']
            )
            result.append(candidate_info)

    result.append('</pre>')
    return '\n'.join(result)


if __name__ == '__main__':
    app.run()
