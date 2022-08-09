from flask import render_template, url_for
from flask_login import login_required
from app.settings import bp


@bp.route('/settings', methods=['GET', 'POST'])
@login_required
def settings():
    return render_template('settings/settings.html', title='Settings')
