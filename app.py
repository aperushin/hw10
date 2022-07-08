from flask import Flask
from utils import load_candidates
from constants import CANDIDATES_JSON

app = Flask(__name__)


@app.route('/')
def get_all():
    candidates = load_candidates(CANDIDATES_JSON)
    result = ['<pre>']
    [result.append(candidate.get_info()) for candidate in candidates]
    result.append('</pre>')
    return '\n'.join(result)


@app.route('/candidates/<int:pk>')
def get_by_pk(pk):
    candidates = load_candidates(CANDIDATES_JSON)
    for candidate in candidates:
        if candidate.pk == pk:
            return (
                f'<img src="{candidate.picture}">'
                f'<pre>{candidate.get_info()}</pre>'
            )
    return f'Кандидата с номером {pk} не существует'


@app.route('/skills/<skill>')
def get_by_skill(skill):
    candidates = load_candidates(CANDIDATES_JSON)
    result = ['<pre>']

    for candidate in candidates:
        if skill in candidate.skills:
            result.append(candidate.get_info())

    result.append('</pre>')
    return '\n'.join(result)


if __name__ == '__main__':
    app.run()
