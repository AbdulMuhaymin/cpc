from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, FloatField
from wtforms.validators import DataRequired, Optional

class SystemForm(FlaskForm):
    system_name = StringField('Name of the System', validators=[DataRequired()])
    gaia_id = StringField('Gaia Designation', validators=[Optional(strip_whitespace=True)])

    sp_type = StringField('Spectral Type', validators=[Optional(strip_whitespace=True)])
    sp_type_ref = TextAreaField('SP_type_ref', default='', validators=[Optional(strip_whitespace=True)])

    ra = FloatField('RA (deg)', validators=[Optional(strip_whitespace=True)])
    ra_error_upper = FloatField('RA_error_upper', validators=[Optional(strip_whitespace=True)])
    ra_error_lower = FloatField('RA_error_lower', validators=[Optional(strip_whitespace=True)])
    dec = FloatField('DEC (deg)', validators=[Optional(strip_whitespace=True)])
    dec_error_upper = FloatField('DEC_error_upper', validators=[Optional(strip_whitespace=True)])
    dec_error_lower = FloatField('DEC_error_lower', validators=[Optional(strip_whitespace=True)])
    ra_dec_ref = TextAreaField('RA_DEC_ref', default='', validators=[Optional(strip_whitespace=True)])

    parallax = FloatField('Parallax (mas)', validators=[Optional(strip_whitespace=True)])
    parallax_error = FloatField('Parallax_error', validators=[Optional(strip_whitespace=True)])
    distance = FloatField('Distance (pc)', validators=[Optional(strip_whitespace=True)])
    distance_error_upper = FloatField('Distance_error_upper', validators=[Optional(strip_whitespace=True)])
    distance_error_lower = FloatField('Distance_error_lower', validators=[Optional(strip_whitespace=True)])
    distance_ref = TextAreaField('Distance_ref', default='', validators=[Optional(strip_whitespace=True)])

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
    radial_velocity_upper = FloatField('RV_error_upper', validators=[Optional(strip_whitespace=True)])
    radial_velocity_lower = FloatField('RV_error_lower', validators=[Optional(strip_whitespace=True)])
    radial_velocity_ref = TextAreaField('RV_ref', default='', validators=[Optional(strip_whitespace=True)])

    a = FloatField('Orbit Semi-major Axis (au)', validators=[Optional(strip_whitespace=True)])
    a_error_upper = FloatField('a_error_upper', validators=[Optional(strip_whitespace=True)])
    a_error_lower = FloatField('a_error_lower', validators=[Optional(strip_whitespace=True)])
    a_ref = TextAreaField('a_ref', default='', validators=[Optional(strip_whitespace=True)])

    incl = FloatField('Inclination (deg)', validators=[Optional(strip_whitespace=True)])
    incl_error_upper = FloatField('incl_error_upper', validators=[Optional(strip_whitespace=True)])
    incl_error_lower = FloatField('incl_error_lower', validators=[Optional(strip_whitespace=True)])
    incl_ref = TextAreaField('incl_ref', default='', validators=[Optional(strip_whitespace=True)])

    e = FloatField('Eccentricity', validators=[Optional(strip_whitespace=True)])
    e_error_upper = FloatField('e_error_upper', validators=[Optional(strip_whitespace=True)])
    e_error_lower = FloatField('e_error_lower', validators=[Optional(strip_whitespace=True)])
    e_ref = TextAreaField('e_ref', default='', validators=[Optional(strip_whitespace=True)])
    
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
