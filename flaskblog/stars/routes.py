from flask import render_template, url_for, flash, redirect, request, Blueprint
from flask_login import current_user, login_required
from flaskblog import db
from flaskblog.models import Star
from flaskblog.stars.forms import StarForm

stars_bp = Blueprint('stars', __name__)

@stars_bp.route("/stars")
def stars():
    return render_template('stars.html', title='Stars')

@stars_bp.route("/stars/new", methods=['GET', 'POST'])
@login_required
def new_star():
    form = StarForm()
    if form.validate_on_submit():
        star = Star(**{k: v for k, v in form.data.items() if k not in ['csrf_token', 'submit']}, 
            author=current_user)
        db.session.add(star)
        db.session.commit()
        flash('The star entry has been successfully added for ', 'success')
        return redirect(url_for('stars.star', star_id=star.id))
    return render_template('star_new.html', title="Add new Star", form=form, legend='Add New Star')
