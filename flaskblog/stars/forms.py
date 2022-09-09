from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired

class StarForm(FlaskForm):
    system_name = StringField('Name of the System', validators=[DataRequired()])
    gaia_id = StringField('Gaia Designation')

    sp_type = StringField('Spectral Type')
    sp_type_ref = TextAreaField('SP_type_ref')

    ra = StringField('RA (deg)')
    ra_error_upper = StringField('RA_error_upper')
    ra_error_lower = StringField('RA_error_lower')
    dec = StringField('DEC (deg)')
    dec_error_upper = StringField('DEC_error_upper')
    dec_error_lower = StringField('DEC_error_lower')
    ra_dec_ref = TextAreaField('RA_DEC_ref')

    parallax = StringField('Parallax (mas)')
    parallax_error = StringField('Parallax_error')
    distance = StringField('Distance (pc)')
    distance_error_upper = StringField('Distance_error_upper')
    distance_error_lower = StringField('Distance_error_lower')
    distance_ref = TextAreaField('Distance_ref')

    distance_gspphot = StringField('Distance_gspphot (pc)')
    distance_gspphot_upper = StringField('Distance_gspphot_error_upper')
    distance_gspphot_lower = StringField('Distance_gspphot_error_lower')

    pmra = StringField('PMRA (mas/yr')
    pmra_error_upper = StringField('PMRA_error_upper')
    pmra_error_lower = StringField('PMRA_error_lower')
    pmdec = StringField('PMDEC (mas/yr)')
    pmdec_error_upper = StringField('PMDEC_error_upper')
    pmdec_error_lower = StringField('PMDEC_error_lower')
    pm = StringField('PM (mas/yr)')
    pm_ref = TextAreaField('PM_ref')

    radial_velocity = StringField('Radial Velocity (km/s)')
    radial_velocity_upper = StringField('RV_error_upper')
    radial_velocity_lower = StringField('RV_error_lower')
    radial_velocity_ref = TextAreaField('RV_ref')

    a = StringField('Orbit Semi-major Axis (au)')
    a_error_upper = StringField('a_error_upper')
    a_error_lower = StringField('a_error_lower')
    a_ref = TextAreaField('a_ref')

    incl = StringField('Inclination (deg)')
    incl_error_upper = StringField('incl_error_upper')
    incl_error_lower = StringField('incl_error_lower')
    incl_ref = TextAreaField('incl_ref')

    e = StringField('Eccentricity')
    e_error_upper = StringField('e_error_upper')
    e_error_lower = StringField('e_error_lower')
    e_ref = TextAreaField('e_ref')
    
    w = StringField('Argument of Periastron (deg)')
    w_error_upper = StringField('w_error_upper')
    w_error_lower = StringField('w_error_lower')
    w_ref = TextAreaField('w_ref')

    age = StringField('Age (Gyr)')
    age_error_upper = StringField('Age_error_upper')
    age_error_lower = StringField('Age_error_lower')
    age_ref = TextAreaField('Age_ref')

    alt_names = TextAreaField('Alternative names')
    notes = TextAreaField('Notes')

    submit = SubmitField('Submit')