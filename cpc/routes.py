from flask import render_template, url_for, flash, redirect, request
from flask_login import login_user, current_user, logout_user, login_required
from cpc import app, db #, bcrypt
from cpc.models import System, Star, Planet, User
from cpc.forms import SystemForm, StarForm, PlanetForm, LoginForm, RegistrationForm, UpdateAccountForm

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html')

@app.route("/about")
def about():
    return render_template('about.html', title='About')

# Following code block is for when we need to manually include data from
# csv files using sqlite. We don't need to bother about these.
#
# import pandas as pd
# import sqlalchemy
# df = pd.read_csv('data/systems.csv')
# url = 'sqlite:///site.db'
# engine = sqlalchemy.create_engine(url)
# with engine.connect().execution_options(autocommit=True) as conn:
#     df.to_sql('system', con=conn, if_exists='append', index= False)

# systems route - to show all the systems (as a table - catalogue)
# new_system route - to create a new system 
# system route - to show the parameters of a single system
# update_systems route - to update the parameters of a single system
# delete_systems route - to delete a specific system

# this same scheme has been applied for star and planet objects too 

@app.route("/systems/")
def systems():
    systems = System.query.all()
    form = SystemForm()
    return render_template('systems.html', title="System Catalogue", systems=systems, form=form)

@app.route("/systems/new", methods=['GET', 'POST'])
@login_required
def new_system():
    form = SystemForm()
    if form.validate_on_submit():
        system = System(**{k: v for k, v in form.data.items() if k not in ['csrf_token', 'submit']}, 
            author=current_user)
        db.session.add(system)
        db.session.commit()
        flash('The system entry has been successfully added for ', 'success')
        return redirect(url_for('system', system_id=system.id))
    return render_template('system_new.html', title="New System", form=form, legend='Add New System')

@app.route("/system/<int:system_id>", methods=['GET', 'POST'])
def system(system_id):
    system = System.query.get_or_404(system_id)
    form = SystemForm(obj=system)
    return render_template('system.html', title=system.system_name, system=system, form=form)

@app.route("/systems/<int:system_id>/update", methods=['GET', 'POST'])
@login_required
def update_system(system_id):
    system = System.query.get_or_404(system_id)
    form = SystemForm(obj=system)
    if form.validate_on_submit():
        form.populate_obj(system)
        db.session.commit()
        flash('The system entry has been updated', 'success')
        return redirect(url_for('system', system_id=system.id))
    elif request.method == 'GET':
        form.populate_obj(system)  
    return render_template('system_new.html', title="Update System", form=form, legend='Update System')

@app.route("/systems/<int:system_id>/delete", methods=['POST'])
@login_required
def delete_system(system_id):
    system = System.query.get_or_404(system_id)
    db.session.delete(system)
    db.session.commit()
    flash('The system entry has been deleted', 'success')
    return redirect(url_for('home'))




# Now the same thing for all star type objects 

@app.route("/stars")
def stars():
    stars=Star.query.all()
    return render_template('stars.html', title='Stars', stars=stars)

@app.route("/stars/new", methods=['GET', 'POST'])
@login_required
def new_star():
    form = StarForm()
    if form.validate_on_submit():
        star = Star(**{k: v for k, v in form.data.items() if k not in ['csrf_token', 'submit']}, 
            author=current_user)
        db.session.add(star)
        db.session.commit()
        flash('The star entry has been successfully added for ', 'success')
        return redirect(url_for('star', star_id=star.id))
    return render_template('star_new.html', title="Add new Star", form=form, legend='Add New Star')

@app.route("/star/<int:star_id>", methods=['GET', 'POST'])
def star(star_id):
    star = Star.query.get_or_404(star_id)
    form = StarForm(obj=star)
    return render_template('star.html', title=star.star_name, star=star, form=form)

@app.route("/stars/<int:star_id>/update", methods=['GET', 'POST'])
@login_required
def update_star(star_id):
    star = Star.query.get_or_404(star_id)
    form = StarForm(obj=star)
    if form.validate_on_submit():
        form.populate_obj(star)
        db.session.commit()
        flash('The star entry has been updated', 'success')
        return redirect(url_for('star', star_id=star.id))
    elif request.method == 'GET':
        form.populate_obj(star)  
    return render_template('star_new.html', title="Update Star", form=form, legend='Update star')

@app.route("/stars/<int:star_id>/delete", methods=['POST'])
@login_required
def delete_star(star_id):
    star = Star.query.get_or_404(star_id)
    db.session.delete(star)
    db.session.commit()
    flash('The star entry has been deleted', 'success')
    return redirect(url_for('home'))



# And now for all planet type objects 

@app.route("/planets")
def planets():
    planets = Planet.query.all()
    return render_template('planets.html', title="Planet Catalogue", planets=planets)

@app.route("/planets/new", methods=['GET', 'POST'])
@login_required
def new_planet():
    form = PlanetForm()
    if form.validate_on_submit():
        planet = Planet(**{k: v for k, v in form.data.items() if k not in ['csrf_token', 'submit']}, 
            author=current_user)
        db.session.add(planet)
        db.session.commit()
        flash('The planet entry has been successfully added for ', 'success')
        return redirect(url_for('planet', planet_id=planet.id))
    return render_template('planet_new.html', title="Add new Planet", form=form, legend='Add New Planet')

@app.route("/planet/<int:planet_id>", methods=['GET', 'POST'])
def planet(planet_id):
    planet = Planet.query.get_or_404(planet_id)
    form = PlanetForm(obj=planet)
    return render_template('planet.html', title=planet.planet_name, planet=planet, form=form)

@app.route("/planets/<int:planet_id>/update", methods=['GET', 'POST'])
@login_required
def update_planet(planet_id):
    planet = Planet.query.get_or_404(planet_id)
    form = PlanetForm(obj=planet)
    if form.validate_on_submit():
        form.populate_obj(planet)
        db.session.commit()
        flash('The planet entry has been updated', 'success')
        return redirect(url_for('planet', planet_id=planet.id))
    elif request.method == 'GET':
        form.populate_obj(planet)  
    return render_template('planet_new.html', title="Update a planet entry", form=form, legend='Update Planet')

@app.route("/planets/<int:planet_id>/delete", methods=['GET', 'POST'])
@login_required
def delete_planet(planet_id):
    planet = Planet.query.get_or_404(planet_id)
    db.session.delete(planet)
    db.session.commit()
    flash('The planet entry has been deleted', 'success')
    return redirect(url_for('home'))

# Lastly, some routes to handle user login, registration and updating username, email etc.
# remember that to prevent further registration, we commented the registration route

# DO NOT UNCOMMENT THIS FOLLOWING REGISTRATION ROUTE CODE BLOCK
# OTHERWISE EVERYONE IN THE INTERNET CAN OPEN AN ACCOUNT AND ADD, DELETE, UPDATE INFORMATION

# @app.route("/register", methods=['GET', 'POST'])
# def register():
#     if current_user.is_authenticated:
#         return redirect(url_for('home'))
#     form = RegistrationForm()
#     if form.validate_on_submit():
#         # hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
#         hashed_password =form.password.data
#         user = User(username=form.username.data, email=form.email.data, password=hashed_password)
#         db.session.add(user)
#         db.session.commit()
#         flash(f'Your account has been created! You are now able to log in', 'success')
#         return redirect(url_for('login'))
#     return render_template('register.html', title='Register', form=form)

@app.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and (user.password==form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check email and password', 'danger')
    return render_template('login.html', title='Login', form=form)

@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('home'))

# A extra feature to save the profile photo of an user. Don't edit these. We don't need to care about these. 
import os
import secrets
from PIL import Image

def save_picture(form_picture):
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(form_picture.filename)
    picture_fn = random_hex + f_ext
    picture_path = os.path.join(app.root_path, 'static/profile_pics', picture_fn)
    output_size = (125, 125)
    i = Image.open(form_picture)
    i.thumbnail(output_size)
    i.save(picture_path)
    return picture_fn
    
@app.route("/account", methods=['GET', 'POST'])
@login_required
def account():
    form = UpdateAccountForm()
    if form.validate_on_submit():
        if form.picture.data:
            picture_file = save_picture(form.picture.data)
            current_user.image_file = picture_file
        current_user.username = form.username.data
        current_user.email = form.email.data
        db.session.commit()
        flash('Your account has been updated!', 'success')
        return redirect(url_for('account'))
    elif request.method == 'GET':
        form.username.data = current_user.username
        form.email.data = current_user.email
    image_file = url_for('static', filename='profile_pics/' + current_user.image_file)
    return render_template('account.html', title='Account',
                           image_file=image_file, form=form)


