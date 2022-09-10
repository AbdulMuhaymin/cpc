from flask import render_template, url_for, flash, redirect, request, Blueprint
from flask_login import current_user, login_required
from flaskblog import db
from flaskblog.models import Star
from flaskblog.stars.forms import StarForm

stars_bp = Blueprint('stars', __name__)

@stars_bp.route("/stars")
def stars():
    stars=Star.query.all()
    return render_template('stars.html', title='Stars', stars=stars)

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

@stars_bp.route("/star/<int:star_id>", methods=['GET', 'POST'])
def star(star_id):
    star = Star.query.get_or_404(star_id)
    return render_template('star.html', title=star.star_name, star=star)

@stars_bp.route("/stars/<int:star_id>/update", methods=['GET', 'POST'])
@login_required
def update_star(star_id):
    star = Star.query.get_or_404(star_id)
    form = StarForm(obj=star)
    if form.validate_on_submit():
        form.populate_obj(star)
        db.session.commit()
        flash('The star entry has been updated', 'success')
        return redirect(url_for('stars.star', star_id=star.id))
    elif request.method == 'GET':
        form.populate_obj(star)  
    return render_template('star_new.html', title="Update Star", form=form, legend='Update star')

@stars_bp.route("/stars/<int:star_id>/delete", methods=['POST'])
@login_required
def delete_star(star_id):
    star = Star.query.get_or_404(star_id)
    db.session.delete(star)
    db.session.commit()
    flash('The star entry has been deleted', 'success')
    return redirect(url_for('main.home'))