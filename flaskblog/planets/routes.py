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

@planets_bp.route("/planet/<int:planet_id>", methods=['GET', 'POST'])
def planet(planet_id):
    planet = Planet.query.get_or_404(planet_id)
    return render_template('planet.html', title=planet.planet_name, planet=planet)

@planets_bp.route("/planets/<int:planet_id>/update", methods=['GET', 'POST'])
@login_required
def update_planet(planet_id):
    planet = Planet.query.get_or_404(planet_id)
    form = PlanetForm(obj=planet)
    if form.validate_on_submit():
        form.populate_obj(planet)
        db.session.commit()
        flash('The planet entry has been updated', 'success')
        return redirect(url_for('planets.planet', planet_id=planet.id))
    elif request.method == 'GET':
        form.populate_obj(planet)  
    return render_template('planet_new.html', title="Update a planet entry", form=form, legend='Update Planet')

@planets_bp.route("/planets/<int:planet_id>/delete", methods=['POST'])
@login_required
def delete_planet(planet_id):
    planet = planet.query.get_or_404(planet_id)
    db.session.delete(planet)
    db.session.commit()
    flash('The planet entry has been deleted', 'success')
    return redirect(url_for('main.home'))