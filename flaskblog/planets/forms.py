from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, IntegerField, FloatField
from wtforms.validators import DataRequired, Optional

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

