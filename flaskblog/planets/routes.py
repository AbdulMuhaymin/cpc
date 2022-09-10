from flask import render_template, url_for, flash, redirect, request, Blueprint
from flask_login import current_user, login_required
from flaskblog import db
from flaskblog.models import Planet
from flaskblog.planets.forms import PlanetForm

planets_bp = Blueprint('planets', __name__)

@planets_bp.route("/planets")
def planets():
    planets = Planet.query.all()
    return render_template('planets.html', title="Planet Catalogue", planets=planets)

@planets_bp.route("/planets/new", methods=['GET', 'POST'])
@login_required
def new_planet():
    form = PlanetForm()
    if form.validate_on_submit():
        planet = Planet(**{k: v for k, v in form.data.items() if k not in ['csrf_token', 'submit']}, 
            author=current_user)
        db.session.add(planet)
        db.session.commit()
        flash('The planet entry has been successfully added for ', 'success')
        return redirect(url_for('planets.planet', planet_id=planet.id))
    return render_template('planet_new.html', title="Add new Planet", form=form, legend='Add New Planet')
