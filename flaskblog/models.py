from flaskblog import db, login_manager
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), default='default.png', nullable=False) 
    password = db.Column(db.String(60), nullable = False)

    stars = db.relationship('Star', backref='author', lazy=True)
    planets = db.relationship('Planet', backref='author', lazy=True)

    def __repr__(self):
        return f"User('{self.username}', {self.email}', {self.image_file}')"

class System(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    system_name = db.Column(db.String, nullable=False)
    gaia_id = db.Column(db.String)

    sp_type = db.Column(db.String)
    sp_type_ref = db.Column(db.String)

    ra = db.Column(db.Float)
    ra_error_upper = db.Column(db.Float)
    ra_error_lower = db.Column(db.Float)
    dec = db.Column(db.Float)
    dec_error_upper = db.Column(db.Float)
    dec_error_lower = db.Column(db.Float)
    ra_dec_ref = db.Column(db.Text)

    parallax = db.Column(db.Float)
    parallax_error = db.Column(db.Float)
    distance = db.Column(db.Float)
    distance_error_upper = db.Column(db.Float)
    distance_error_lower = db.Column(db.Float)
    distance_ref = db.Column(db.Text)

    distance_gspphot = db.Column(db.Float)
    distance_gspphot_upper = db.Column(db.Float)
    distance_gspphot_lower = db.Column(db.Float)

    pmra = db.Column(db.Float)
    pmra_error_upper = db.Column(db.Float)
    pmra_error_lower = db.Column(db.Float)
    pmdec = db.Column(db.Float)
    pmdec_error_upper = db.Column(db.Float)
    pmdec_error_lower = db.Column(db.Float)
    pm = db.Column(db.Float)
    pm_ref = db.Column(db.Text)

    radial_velocity = db.Column(db.Float)
    radial_velocity_error_upper = db.Column(db.Float)
    radial_velocity_error_lower = db.Column(db.Float)
    radial_velocity_ref = db.Column(db.Text)

    a = db.Column(db.Float)
    a_error_upper = db.Column(db.Float)
    a_error_lower = db.Column(db.Float)
    a_ref = db.Column(db.Text)

    incl = db.Column(db.Float)
    incl_error_upper = db.Column(db.Float)
    incl_error_lower = db.Column(db.Float)
    incl_ref = db.Column(db.Text)

    e = db.Column(db.Float)
    e_error_upper = db.Column(db.Float)
    e_error_lower = db.Column(db.Float)
    e_ref = db.Column(db.Text)
    
    w = db.Column(db.Float)
    w_error_upper = db.Column(db.Float)
    w_error_lower = db.Column(db.Float)
    w_ref = db.Column(db.Text)

    age = db.Column(db.Float)
    age_error_upper = db.Column(db.Float)
    age_error_lower = db.Column(db.Float)
    age_ref = db.Column(db.Text)

    alt_names = db.Column(db.String)
    notes = db.Column(db.Text)

    def __repr__(self):
        return f"System - '{self.system_name}')"

class Star(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    
    star_name = db.Column(db.String, unique=True, nullable=False)
    system_name = db.Column(db.String)
    sp_type = db.Column(db.String)

    mass = db.Column(db.Float)
    mass_error_upper = db.Column(db.Float)
    mass_error_lower = db.Column(db.Float)
    mass_ref = db.Column(db.Text)

    radius = db.Column(db.Float)
    radius_error_upper = db.Column(db.Float)
    radius_error_lower = db.Column(db.Float)
    radius_ref = db.Column(db.Text)

    log_g = db.Column(db.Float)
    log_g_error_upper = db.Column(db.Float)
    log_g_error_lower = db.Column(db.Float)
    log_g_ref = db.Column(db.Text)

    T_eff = db.Column(db.Float)
    T_eff_error_upper = db.Column(db.Float)
    T_eff_error_lower = db.Column(db.Float)
    T_eff_ref = db.Column(db.Text)

    Fe_H = db.Column(db.Float)
    Fe_H_error_upper = db.Column(db.Float)
    Fe_H_error_lower = db.Column(db.Float)
    Fe_H_ref = db.Column(db.Text)

    M_H = db.Column(db.Float)
    M_H_error_upper = db.Column(db.Float)
    M_H_error_lower = db.Column(db.Float)
    M_H_ref = db.Column(db.Text)

    vsini = db.Column(db.Float)
    vsini_error_upper = db.Column(db.Float)
    vsini_error_lower = db.Column(db.Float)
    vsini_ref = db.Column(db.Text)
    
    p_rot= db.Column(db.Float)
    p_rot_error_upper = db.Column(db.Float)
    p_rot_error_lower = db.Column(db.Float)
    p_rot_ref = db.Column(db.Text)
    
    notes = db.Column(db.Text)

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"System - '{self.star_name}')"

class Planet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    
    planet_name = db.Column(db.String)
    system_name = db.Column(db.String)
    discovery_method = db.Column(db.String)
    discovery_year = db.Column(db.Integer)
    discovery_ref = db.Column(db.Text)

    OrbPer = db.Column(db.Float)
    OrbPer_error_upper = db.Column(db.Float)
    OrbPer_error_lower = db.Column(db.Float)
    OrbPer_ref = db.Column(db.Text)

    mass = db.Column(db.Float)
    mass_error_upper = db.Column(db.Float)
    mass_error_lower = db.Column(db.Float)
    mass_ref = db.Column(db.Text)

    min_mass = db.Column(db.Float)
    min_mass_error_upper = db.Column(db.Float)
    min_mass_error_lower = db.Column(db.Float)
    min_mass_ref = db.Column(db.Text)

    radius = db.Column(db.Float)
    radius_error_upper = db.Column(db.Float)
    radius_error_lower = db.Column(db.Float)
    radius_ref = db.Column(db.Text)

    pl_a = db.Column(db.Float)
    pl_a_error_upper = db.Column(db.Float)
    pl_a_error_lower = db.Column(db.Float)
    pl_a_ref = db.Column(db.Text)

    pl_e = db.Column(db.Float)
    pl_e_error_upper = db.Column(db.Float)
    pl_e_error_lower = db.Column(db.Float)
    pl_e_ref = db.Column(db.Text)

    pl_w = db.Column(db.Float)
    pl_w_error_upper = db.Column(db.Float)
    pl_w_error_lower = db.Column(db.Float)
    pl_w_ref = db.Column(db.Text)

    T_per = db.Column(db.Float)
    T_per_error_upper = db.Column(db.Float)
    T_per_error_lower = db.Column(db.Float)
    T_per_ref = db.Column(db.Text)

    mean_anomaly = db.Column(db.Float)
    mean_anomaly_error_upper = db.Column(db.Float)
    mean_anomaly_error_lower = db.Column(db.Float)
    mean_anomaly_ref = db.Column(db.Text)
    
    notes = db.Column(db.Text)

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"System - '{self.planet_name}')"

