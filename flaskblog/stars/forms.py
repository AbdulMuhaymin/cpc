from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, FloatField
from wtforms.validators import DataRequired, Optional

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
    p_rot_error_upper = FloatField('P_rot_error_upper', validators=[Optional(strip_whitespace=True)])
    p_rot_error_lower = FloatField('P_rot_error_lower', validators=[Optional(strip_whitespace=True)])
    p_rot_ref = TextAreaField('P_rot_ref', validators=[Optional(strip_whitespace=True)])

    notes = TextAreaField('Notes', validators=[Optional(strip_whitespace=True)])

    submit = SubmitField('Submit', validators=[Optional(strip_whitespace=True)])
