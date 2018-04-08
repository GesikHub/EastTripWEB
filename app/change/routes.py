from app.change import bp
from flask_login import current_user, login_required
from flask import redirect, url_for


@bp.route('/changeemail', methods=['GET', 'POST'])
@login_required
def new_place():
    if current_user.is_authenticated:
        redirect(url_for('auth.login'))
            
