from flask import render_template, url_for
from . import bp
from ..data import data


@bp.route('/')
@bp.route('/home/')
def home():
    context = {
        'title': 'Home',
        'data': data.data,
        'rank': data.data['rank'],
        'names': data.data.account_name,
        'owner': data.data.owner,
        'million_followers': data.data.million_followers,
        'occupation': data.data.occupation,
        'citizenship': data.data.citizenship,
    }
    return render_template(
        'index.html',
        **context 
    )