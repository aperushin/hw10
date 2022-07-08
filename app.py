from flask import Flask, abort
from utils import format_pre_tag, get_all, get_by_pk, get_by_skill
app = Flask(__name__)


@app.route('/')
def page_home():
    """Display all candidates"""
    result = '\n'.join(get_all())
    return format_pre_tag(result)


@app.route('/candidates/<int:uid>')
def page_candidate(uid):
    """Display candidate with given id"""
    candidate = get_by_pk(uid)
    if candidate:
        return (
            f'<img src="{candidate.picture}">\n' +
            format_pre_tag(candidate.get_info())
        )
    return abort(404)


@app.route('/skills/<skill>')
def page_skill(skill):
    """Display all candidates with given skill"""
    candidates = get_by_skill(skill)
    if candidates:
        result = '\n'.join(candidates)
        return format_pre_tag(result)
    return abort(404)


if __name__ == '__main__':
    app.run()
