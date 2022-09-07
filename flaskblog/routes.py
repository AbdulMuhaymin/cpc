from flask import render_template, url_for, flash, redirect, request, abort
from flaskblog import app, db, bcrypt
from flaskblog.forms import RegistrationForm, LoginForm, UpdateAccountForm, SystemForm, StarForm, PlanetForm
from flaskblog.models import User, System, Star, Planet
from flask_login import login_user, current_user, logout_user, login_required
import secrets
import os
from PIL import Image

@app.route('/home')
@app.route('/')
def home():
    return render_template('home.html')




@app.route('/about')
def about():
    return render_template('about.html', title="About us")

@app.route('/systems')
def systems():
    return render_template('systems.html', title="Systems Data")

@app.route('/stars')
def stars():
    return render_template('stars.html', title="Stars Data")
    
@app.route('/planets')
def planets():
    return render_template('planets.html', title="Planets Data")




# The following code is intended for creating new
# systems, updating existing systems data and visiting existing system. 
@app.route('/systems/new', methods=['GET', 'POST'])
@login_required
def new_system():
    form = SystemForm()
    if form.validate_on_submit():
        system = System(name=form.name.data, sp_type=form.sp_type.data, author=current_user)
        db.session.add(system)
        db.session.commit()
        flash('A new system has been successfully added!', 'success')
        return redirect(url_for('home'))
    return render_template('new_system.html', title="New System",
        form=form, legend='Add System Data')

@app.route('/systems/<int:system_id>', methods=['GET', 'POST'])
def system(system_id):
    system = System.query.get_or_404(system_id)
    return render_template('system.html', title=system.system_name, system=system)

@app.route('/systems/<int:system_id>/update', methods=['GET', 'POST'])
@login_required
def update_system(system_id):
    system = System.query.get_or_404(system_id)
    form = SystemForm()
    if form.validate_on_submit():
        system.name = form.name.data
        system.sp_type = form.sp_type.data
        db.session.commit()
        flash('The system data has been successfully updated.', 'success')
        return redirect(url_for('system', system_id=system.id))
    elif request.method == 'GET':
        form.name.data = system.name
        form.sp_type.data = system.sp_type
    return render_template('new_system.html', title="Update System",
        form=form, legend="Update System Data", system=system)

@app.route('/systems/<int:system_id>/delete', methods=['POST'])
@login_required
def delete_system(system_id):
    system = System.query.get_or_404(system_id)
    db.session.delete(system)
    db.session.commit()
    flash('The system has been deleted!', 'success')
    return redirect( url_for('home'))




# The following code is intended for creating new
# stars, updating existing stars data and visiting existing stars. 
@app.route('/stars/new', methods=['GET', 'POST'])
@login_required
def new_star():
    form = StarForm()
    if form.validate_on_submit():
        star = Star(name=form.name.data, sp_type=form.sp_type.data, author=current_user)
        db.session.add(star)
        db.session.commit()
        flash('A new star has been successfully added!', 'success')
        return redirect(url_for('stars'))
    return render_template('new_star.html', title="Add a Star",
        form=form, legend='Add Star Data')

@app.route('/stars/<int:star_id>', methods=['GET', 'POST'])
def star(star_id):
    star = Star.query.get_or_404(star_id)
    return render_template('star.html', title=star.star_name, star=star)

@app.route('/stars/<int:star_id>/update', methods=['GET', 'POST'])
@login_required
def update_star(star_id):
    star = Star.query.get_or_404(star_id)
    form = StarForm()
    if form.validate_on_submit():
        star.star_name = form.star_name.data
        star.sp_type = form.sp_type.data
        db.session.commit()
        flash('The star data has been successfully updated.', 'success')
        return redirect(url_for('star', star_id=star.id))
    elif request.method == 'GET':
        form.name.data = star.name
        form.sp_type.data = star.sp_type
    return render_template('star.html', title="Update Star",
        form=form, legend="Update Star Data", star=star)

@app.route('/stars/<int:star_id>/delete', methods=['POST'])
@login_required
def delete_star(star_id):
    star = Star.query.get_or_404(star_id)
    db.session.delete(star)
    db.session.commit()
    flash('The star has been deleted!', 'success')
    return redirect( url_for('home'))




# The following code is intended for creating new
# planets, updating existing planets data and visiting existing planets. 

@app.route('/planets/new', methods=['GET', 'POST'])
@login_required
def new_planet():
    form = PlanetForm()
    if form.validate_on_submit():
        flash('A new planet has been successfully added!', 'success')
        return redirect(url_for('planets'))
    return render_template('new_planet.html', title="Add a Planet", form=form)

@app.route('/planets/<int:planet_id>', methods=['GET', 'POST'])
def planet(planet_id):
    planet = Planet.query.get_or_404(planet_id)
    return render_template('planet.html', title=planet.planet_name, planet=planet)

@app.route('/planets/<int:planet_id>/update', methods=['GET', 'POST'])
@login_required
def update_planet(planet_id):
    planet = Planet.query.get_or_404(planet_id)
    form = PlanetForm()
    if form.validate_on_submit():
        planet.planet_name = form.planet_name.data
        db.session.commit()
        flash('The planet data has been successfully updated.', 'success')
        return redirect(url_for('planet', planet_id=planet.id))
    elif request.method == 'GET':
        form.name.data = planet.name
    return render_template('planet.html', title="Update planet",
        form=form, legend="Update planet Data", planet=planet)

@app.route('/planets/<int:planet_id>/delete', methods=['POST'])
@login_required
def delete_planet(planet_id):
    planet = Planet.query.get_or_404(planet_id)
    db.session.delete(planet)
    db.session.commit()
    flash('The planet has been deleted!', 'success')
    return redirect( url_for('home'))




# The following code is intended for very limited use
# i.e. to use the sign in, sign up, account update etc. feature.

# registration
@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash(f'Your account has been created! You are now able to log in!', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', title="Register", form=form)

# login 
@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check Email and Password', 'danger')
    return render_template('login.html', title="Login", form=form)

# logout
@app.route('/logout',)
def logout():
    logout_user()
    return redirect(url_for('home'))

# updating and resizing account picture
def save_picture(form_picture):
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(form_picture.filename)
    picture_fn = random_hex + f_ext
    picture_path = os.path.join(app.root_path, 'static/profile_pics', picture_fn)
    
    output_size = (125, 125)
    resized_pic = Image.open(form_picture)
    resized_pic.thumbnail(output_size)
    resized_pic.save(picture_path)
    return picture_fn

# updating account info
@app.route('/account', methods=['GET', 'POST'])
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
        flash('Your account info has been updated!', 'success')
        return redirect(url_for('account'))
    elif request.method == 'GET':
        form.username.data = current_user.username
        form.email.data = current_user.email
    image_file = url_for('static', filename='profile_pics/' + current_user.image_file)
    return render_template('account.html', title="Your Account",
        image_file=image_file, form=form)