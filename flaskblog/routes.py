import os
import secrets
from PIL import Image
from flask import render_template, url_for, flash, redirect, request
from flaskblog import app, db, bcrypt
from flaskblog.forms import RegistrationForm, LoginForm, UpdateAccountForm, SystemForm
from flaskblog.models import User, System
from flask_login import login_user, current_user, logout_user, login_required


@app.route("/")
@app.route("/home")
def home():
    systems = System.query.all()
    return render_template('home.html', systems=systems)

@app.route("/about")
def about():
    return render_template('about.html', title='About')



@app.route("/register", methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash(f'Your account has been created! You are now able to log in', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)

@app.route("/login", methods=['GET', 'POST'])
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
            flash('Login Unsuccessful. Please check email and password', 'danger')
    return render_template('login.html', title='Login', form=form)

@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('home'))

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

@app.route("/system/<int:system_id>", methods=['GET', 'POST'])
def system(system_id):
    system = System.query.get_or_404(system_id)
    return render_template('system.html', title=system.system_name, system=system.__dict__)


@app.route("/systems/")
def systems():
    systems = System.query.all()
    return render_template('systems.html', title="System Catalogue", systems=systems)

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
    return render_template('new_system.html', title="Add a system entry", form=form, legend='Add New System')

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
        
    return render_template('new_system.html', title="Update a system entry", form=form, legend='Update System')

@app.route("/systems/<int:system_id>/delete", methods=['POST'])
@login_required
def delete_system(system_id):
    system = System.query.get_or_404(system_id)
    db.session.delete(system)
    db.session.commit()
    flash('The system entry has been deleted', 'success')
    return redirect(url_for('home'))
