from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from flask_login import current_user
from wtforms import StringField, SubmitField, PasswordField, BooleanField, TextAreaField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from flaskblog.models import User


class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')
    
    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('That username is taken. Please choose a different one.')
    
    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('That email is already in use. Please choose another one.')

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Sign In')

class UpdateAccountForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    picture = FileField('Update Profile Picture', validators=[FileAllowed(['jpg','png'])])
    submit = SubmitField('Update')
    
    def validate_username(self, username):
        if username.data != current_user.username:
            user = User.query.filter_by(username=username.data).first()
            if user:
                raise ValidationError('That username is taken. Please choose a different one.')
    
    def validate_email(self, email):
        if email.data != current_user.email:
            user = User.query.filter_by(email=email.data).first()
            if user:
                raise ValidationError('That email is already in use. Please choose another one.')

class SystemForm(FlaskForm):
    system_name = StringField('Title', validators=[DataRequired()])
    gaia_id
    sp_type =  StringField('Spectral Type')

    sp_type = db.Column()
    sp_type_ref = db.Column()

    ra = StringField('')
    ra_error_upper = db.Column()
    ra_error_lower = db.Column()
    dec = db.Column()
    dec_error_upper = db.Column()
    dec_error_lower = db.Column()
    ra_dec_ref = StringField('')

    parallax = db.Column()
    parallax_error = db.Column()
    distance = db.Column()
    distance_error_upper = db.Column()
    distance_error_lower = db.Column()
    distance_ref = StringField('')

    distance_gspphot = db.Column()
    distance_gspphot_upperper = db.Column()
    distance_gspphot_lower = db.Column()

    pmra = db.Column()
    pmra_error_upper = db.Column()
    pmra_error_lower = db.Column()
    pmdec = db.Column()
    pmdec_error_upper = db.Column()
    pmdec_error_lower = db.Column()
    pm = db.Column()
    pm_ref = StringField('')

    radial_velocity = db.Column()
    radial_velocity_upper = db.Column()
    radial_velocity_lower = db.Column()
    radial_velocity_ref = StringField('')

    a = db.Column()
    a_error_upper = db.Column()
    a_error_lower = db.Column()
    a_ref = StringField('')

    incl = db.Column()
    incl_error_upper = db.Column()
    incl_error_lower = db.Column()
    incl_ref = StringField('')

    e = db.Column()
    e_error_upper = db.Column()
    e_error_lower = db.Column()
    e_ref = StringField('')
    
    w = db.Column()
    w_error_upper = db.Column()
    w_error_lower = db.Column()
    w_ref = StringField('')

    age = db.Column()
    age_error_upper = db.Column()
    age_error_lower = db.Column()
    age_ref = StringField('')

    alt_names = TextAreaField()
    notes = TextAreaField()


    submit = SubmitField('Submit')

class StarForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    sp_type =  StringField('Spectral Type')
    submit = SubmitField('Submit')

class PlanetForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    sp_type =  StringField('Spectral Type')
    submit = SubmitField('Submit')
    