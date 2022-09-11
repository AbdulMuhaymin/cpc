from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, TextAreaField, FloatField, IntegerField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError, Optional

class SystemForm(FlaskForm):
    system_name = StringField('Name of the System', validators=[DataRequired()])
    gaia_id = StringField('Gaia Designation', validators=[Optional(strip_whitespace=True)])

    sp_type = StringField('Spectral Type', validators=[Optional(strip_whitespace=True)])
    sp_type_ref = TextAreaField('Spectral Type Ref.', default='', validators=[Optional(strip_whitespace=True)])

    ra = FloatField('RA (deg)', validators=[Optional(strip_whitespace=True)])
    ra_error_upper = FloatField('RA_error_upper', validators=[Optional(strip_whitespace=True)])
    ra_error_lower = FloatField('RA_error_lower', validators=[Optional(strip_whitespace=True)])
    dec = FloatField('DEC (deg)', validators=[Optional(strip_whitespace=True)])
    dec_error_upper = FloatField('DEC_error_upper', validators=[Optional(strip_whitespace=True)])
    dec_error_lower = FloatField('DEC_error_lower', validators=[Optional(strip_whitespace=True)])
    ra_dec_ref = TextAreaField('RA DEC Ref.', default='', validators=[Optional(strip_whitespace=True)])

    parallax = FloatField('Parallax (mas)', validators=[Optional(strip_whitespace=True)])
    parallax_error = FloatField('Parallax_error', validators=[Optional(strip_whitespace=True)])
    distance = FloatField('Distance (pc)', validators=[Optional(strip_whitespace=True)])
    distance_error_upper = FloatField('Distance_error_upper', validators=[Optional(strip_whitespace=True)])
    distance_error_lower = FloatField('Distance_error_lower', validators=[Optional(strip_whitespace=True)])
    distance_ref = TextAreaField('Distance Ref.', default='', validators=[Optional(strip_whitespace=True)])

    distance_gspphot = FloatField('Distance_gspphot (pc)', validators=[Optional(strip_whitespace=True)])
    distance_gspphot_upper = FloatField('Distance_gspphot_error_upper', validators=[Optional(strip_whitespace=True)])
    distance_gspphot_lower = FloatField('Distance_gspphot_error_lower', validators=[Optional(strip_whitespace=True)])

    pmra = FloatField('PMRA (mas/yr', validators=[Optional(strip_whitespace=True)])
    pmra_error_upper = FloatField('PMRA_error_upper', validators=[Optional(strip_whitespace=True)])
    pmra_error_lower = FloatField('PMRA_error_lower', validators=[Optional(strip_whitespace=True)])
    pmdec = FloatField('PMDEC (mas/yr)', validators=[Optional(strip_whitespace=True)])
    pmdec_error_upper = FloatField('PMDEC_error_upper', validators=[Optional(strip_whitespace=True)])
    pmdec_error_lower = FloatField('PMDEC_error_lower', validators=[Optional(strip_whitespace=True)])
    pm = FloatField('PM (mas/yr)', validators=[Optional(strip_whitespace=True)])
    pm_ref = TextAreaField('PM_ref', default='', validators=[Optional(strip_whitespace=True)])

    radial_velocity = FloatField('Radial Velocity (km/s)', validators=[Optional(strip_whitespace=True)])
    radial_velocity_error_upper = FloatField('RV_error_upper', validators=[Optional(strip_whitespace=True)])
    radial_velocity_error_lower = FloatField('RV_error_lower', validators=[Optional(strip_whitespace=True)])
    radial_velocity_ref = TextAreaField('RV_ref', default='', validators=[Optional(strip_whitespace=True)])

    a = FloatField('Orbit Semi-major Axis (au)', validators=[Optional(strip_whitespace=True)])
    a_error_upper = FloatField('a_error_upper', validators=[Optional(strip_whitespace=True)])
    a_error_lower = FloatField('a_error_lower', validators=[Optional(strip_whitespace=True)])
    a_ref = TextAreaField('a_ref', default='', validators=[Optional(strip_whitespace=True)])

    incl = FloatField('Inclination (deg)', validators=[Optional(strip_whitespace=True)])
    incl_error_upper = FloatField('Inclination_error_upper', validators=[Optional(strip_whitespace=True)])
    incl_error_lower = FloatField('Inclination_error_lower', validators=[Optional(strip_whitespace=True)])
    incl_ref = TextAreaField('Inclination Ref.', default='', validators=[Optional(strip_whitespace=True)])

    e = FloatField('Eccentricity', validators=[Optional(strip_whitespace=True)])
    e_error_upper = FloatField('Eccentricity_error_upper', validators=[Optional(strip_whitespace=True)])
    e_error_lower = FloatField('Eccentricity_error_lower', validators=[Optional(strip_whitespace=True)])
    e_ref = TextAreaField('Eccentricity Ref.', default='', validators=[Optional(strip_whitespace=True)])
    
    w = FloatField('Argument of Periastron (deg)', validators=[Optional(strip_whitespace=True)])
    w_error_upper = FloatField('w_error_upper', validators=[Optional(strip_whitespace=True)])
    w_error_lower = FloatField('w_error_lower', validators=[Optional(strip_whitespace=True)])
    w_ref = TextAreaField('w_ref', default='', validators=[Optional(strip_whitespace=True)])

    age = FloatField('Age (Gyr)', validators=[Optional(strip_whitespace=True)])
    age_error_upper = FloatField('Age_error_upper', validators=[Optional(strip_whitespace=True)])
    age_error_lower = FloatField('Age_error_lower', validators=[Optional(strip_whitespace=True)])
    age_ref = TextAreaField('Age_ref', default='', validators=[Optional(strip_whitespace=True)])

    alt_names = TextAreaField('Alternative names')
    notes = TextAreaField('Notes')

    submit = SubmitField('Submit')

class StarForm(FlaskForm):
    star_name = StringField('Name of the Star', validators=[DataRequired()])
    system_name = StringField('Name of the System', validators=[Optional(strip_whitespace=True)])
    sp_type = StringField('Spectral Type', validators=[Optional(strip_whitespace=True)])

    mass = FloatField('Mass (Mₛᵤₙ)', validators=[Optional(strip_whitespace=True)])
    mass_error_upper = FloatField('Mass_error_upper', validators=[Optional(strip_whitespace=True)])
    mass_error_lower = FloatField('Mass_error_lower', validators=[Optional(strip_whitespace=True)])
    mass_ref = TextAreaField('Mass_ref', validators=[Optional(strip_whitespace=True)])

    radius = FloatField('Radius (Rₛᵤₙ)', validators=[Optional(strip_whitespace=True)])
    radius_error_upper = FloatField('Radius_error_upper', validators=[Optional(strip_whitespace=True)])
    radius_error_lower = FloatField('Radius_error_lower', validators=[Optional(strip_whitespace=True)])
    radius_ref = TextAreaField('Radius_ref', validators=[Optional(strip_whitespace=True)])

    log_g = FloatField('Surface Gravity - log g (cm/s²)', validators=[Optional(strip_whitespace=True)])
    log_g_error_upper = FloatField('log_g_error_upper', validators=[Optional(strip_whitespace=True)])
    log_g_error_lower = FloatField('log_g_error_lower', validators=[Optional(strip_whitespace=True)])
    log_g_ref = TextAreaField('log_g_ref', validators=[Optional(strip_whitespace=True)])

    T_eff = FloatField('T_effective (K)', validators=[Optional(strip_whitespace=True)])
    T_eff_error_upper = FloatField('T_effective_error_upper', validators=[Optional(strip_whitespace=True)])
    T_eff_error_lower = FloatField('T_effective_error_lower', validators=[Optional(strip_whitespace=True)])
    T_eff_ref = TextAreaField('T_effective_ref', validators=[Optional(strip_whitespace=True)])

    Fe_H = FloatField('[Fe/H] (dex)', validators=[Optional(strip_whitespace=True)])
    Fe_H_error_upper = FloatField('[Fe/H]_error_upper', validators=[Optional(strip_whitespace=True)])
    Fe_H_error_lower = FloatField('[Fe/H]_error_lower', validators=[Optional(strip_whitespace=True)])
    Fe_H_ref = TextAreaField('[Fe/H]_ref', validators=[Optional(strip_whitespace=True)])

    M_H = FloatField('[M/H] (dex)', validators=[Optional(strip_whitespace=True)])
    M_H_error_upper = FloatField('[M/H]_error_upper', validators=[Optional(strip_whitespace=True)])
    M_H_error_lower = FloatField('[M/H]_error_lower', validators=[Optional(strip_whitespace=True)])
    M_H_ref = TextAreaField('[M/H]_ref', validators=[Optional(strip_whitespace=True)])

    vsini = FloatField('V_sin_i (km/s)', validators=[Optional(strip_whitespace=True)])
    vsini_error_upper = FloatField('vsini_error_upper', validators=[Optional(strip_whitespace=True)])
    vsini_error_lower = FloatField('vsini_error_lower', validators=[Optional(strip_whitespace=True)])
    vsini_ref = TextAreaField('vsini_ref', validators=[Optional(strip_whitespace=True)])

    p_rot = FloatField('P_rot (days)', validators=[Optional(strip_whitespace=True)])
    p_rot_err_upper = FloatField('P_rot_error_upper', validators=[Optional(strip_whitespace=True)])
    p_rot_err_lower = FloatField('P_rot_error_lower', validators=[Optional(strip_whitespace=True)])
    p_rot_ref = TextAreaField('P_rot_ref', validators=[Optional(strip_whitespace=True)])

    notes = TextAreaField('Notes', validators=[Optional(strip_whitespace=True)])

    submit = SubmitField('Submit', validators=[Optional(strip_whitespace=True)])

class PlanetForm(FlaskForm):
    planet_name = StringField('Name of the planet', validators=[DataRequired()])
    system_name = StringField('Name of the system', validators=[Optional(strip_whitespace=True)])
    discovery_method = StringField('Discovery method', validators=[Optional(strip_whitespace=True)])
    discovery_year = IntegerField('Discovery year', validators=[Optional(strip_whitespace=True)])
    discovery_ref = TextAreaField('Discovery Reference', validators=[Optional(strip_whitespace=True)])

    OrbPer = FloatField('Orbital Period (days)', validators=[Optional(strip_whitespace=True)])
    OrbPer_error_upper = FloatField('Orbital Period_error_upper', validators=[Optional(strip_whitespace=True)])
    OrbPer_error_lower = FloatField('Orbital Period_error_lower', validators=[Optional(strip_whitespace=True)])
    OrbPer_ref = TextAreaField('Orbital Period ref', validators=[Optional(strip_whitespace=True)])

    mass = FloatField('Mass (Mⱼᵤₚ)', validators=[Optional(strip_whitespace=True)])
    mass_error_upper = FloatField('Mass_error_upper', validators=[Optional(strip_whitespace=True)])
    mass_error_lower = FloatField('Mass_error_lower', validators=[Optional(strip_whitespace=True)])
    mass_ref = TextAreaField('Mass ref', validators=[Optional(strip_whitespace=True)])

    min_mass = FloatField('Minimum Mass (Mⱼᵤₚ)', validators=[Optional(strip_whitespace=True)])
    min_mass_error_upper = FloatField('Minimum Mass_error_upper', validators=[Optional(strip_whitespace=True)])
    min_mass_error_lower = FloatField('Minimum Mass_error_lower', validators=[Optional(strip_whitespace=True)])
    min_mass_ref = TextAreaField('Minimum Mass ref', validators=[Optional(strip_whitespace=True)])

    radius = FloatField('Radius (Rⱼᵤₚ)', validators=[Optional(strip_whitespace=True)])
    radius_error_upper = FloatField('Radius_error_upper', validators=[Optional(strip_whitespace=True)])
    radius_error_lower = FloatField('Radius_error_lower', validators=[Optional(strip_whitespace=True)])
    radius_ref = TextAreaField('Radius ref', validators=[Optional(strip_whitespace=True)])

    pl_a = FloatField('semi-major axis, a (AU)', validators=[Optional(strip_whitespace=True)])
    pl_a_error_upper = FloatField('a_error_upper', validators=[Optional(strip_whitespace=True)])
    pl_a_error_lower = FloatField('a_error_lower', validators=[Optional(strip_whitespace=True)])
    pl_a_ref = TextAreaField('a_ref', validators=[Optional(strip_whitespace=True)])

    pl_e = FloatField('Eccentricity', validators=[Optional(strip_whitespace=True)])
    pl_e_error_upper = FloatField('e_error_upper', validators=[Optional(strip_whitespace=True)])
    pl_e_error_lower = FloatField('e_error_lower', validators=[Optional(strip_whitespace=True)])
    pl_e_ref = TextAreaField('e', validators=[Optional(strip_whitespace=True)])

    pl_w = FloatField('w (deg)', validators=[Optional(strip_whitespace=True)])
    pl_w_error_upper = FloatField('w_error_upper', validators=[Optional(strip_whitespace=True)])
    pl_w_error_lower = FloatField('w_error_lower', validators=[Optional(strip_whitespace=True)])
    pl_w_ref = TextAreaField('w', validators=[Optional(strip_whitespace=True)])

    T_per = FloatField('Time of Perisatron Passage (BJD-TDB)', validators=[Optional(strip_whitespace=True)])
    T_per_error_upper = FloatField('T_per_error_upper', validators=[Optional(strip_whitespace=True)])
    T_per_error_lower = FloatField('T_per_error_lower', validators=[Optional(strip_whitespace=True)])
    T_per_ref = TextAreaField('T_per', validators=[Optional(strip_whitespace=True)])

    mean_anomaly = FloatField('Mean Anomaly (deg)', validators=[Optional(strip_whitespace=True)])
    mean_anomaly_error_upper = FloatField('Mean Anomaly_error_upper', validators=[Optional(strip_whitespace=True)])
    mean_anomaly_error_lower = FloatField('Mean Anomaly_error_lower', validators=[Optional(strip_whitespace=True)])
    mean_anomaly_ref = TextAreaField('Mean Anomaly ref', validators=[Optional(strip_whitespace=True)])
    
    notes = TextAreaField('Notes', validators=[Optional(strip_whitespace=True)])

    submit = SubmitField('Submit', validators=[Optional(strip_whitespace=True)])

from flask_login import current_user
from cpc.models import User

class RegistrationForm(FlaskForm):
    username = StringField('Username',
        validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', 
        validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('That username is taken. Please choose a different one.')
    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('That email is taken. Please choose a different one.')

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Sign in')

class UpdateAccountForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    picture = FileField('Update Profile Picture', validators=[FileAllowed(['jpg', 'png'])])
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
                raise ValidationError('That email is taken. Please choose a different one.')
