from flask import render_template, url_for, flash, redirect, request, Blueprint
from flask_login import current_user, login_required
from flaskblog import db
from flaskblog.models import Planet
from flaskblog.planets.forms import PlanetForm

planets_bp = Blueprint('planets', __name__)

@planets_bp.route("/planets")
def planets():
    return render_template('planets.html', title='Planets')

@planets_bp.route("/planets/new")
@login_required
def new_planet():
    return render_template('planet_new.html', title='Add a planet')

