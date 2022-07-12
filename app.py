from flask import Flask, abort, render_template
from utils import get_all, get_by_pk, get_by_skill

app = Flask(__name__)


@app.route('/')
def page_home():
    """Display all candidates"""
    candidates = get_all()
    return render_template('all.html', candidates=candidates)


@app.route('/candidates/<int:uid>')
def page_candidate(uid):
    """Display candidate with given id"""
    candidate = get_by_pk(uid)
    if candidate:
        return render_template('search_result.html', candidate=candidate)
    return abort(404)


@app.route('/skills/<skill>')
def page_skill(skill):
    """Display all candidates with given skill"""
    candidates = get_by_skill(skill)
    if candidates:
        return render_template('all.html', candidates=candidates)
    return abort(404)


if __name__ == '__main__':
    app.run(port=5050, debug=True)
