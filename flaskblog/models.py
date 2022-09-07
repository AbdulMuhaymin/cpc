# In this file, we will code all the database models. In our case, we have four types of models: user, system, star, planet 
from flaskblog import db, login_manager
from flask_login import UserMixin


# The following code is to initiate a user session so that s/he can add/modify entry
@login_manager.user_loader
def laod_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), default='default.png', nullable=False) 
    password = db.Column(db.String(60), nullable = False)
    systems = db.relationship('System', backref='author', lazy=True)

    def __repr__(self):
        return f"User('{self.username}', {self.email}', {self.image_file}')"

     
# The following code is to create a system class with parameters that is only valid for a system  
class System(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    system_name = db.Column(unique=True, nullable=False)
    gaia_id = db.Column(unique=True)

    sp_type = db.Column()
    sp_type_ref = db.Column()

    ra = db.Column()
    ra_error_upper = db.Column()
    ra_error_lower = db.Column()
    dec = db.Column()
    dec_error_upper = db.Column()
    dec_error_lower = db.Column()
    ra_dec_ref = db.Column()

    parallax = db.Column()
    parallax_error = db.Column()
    distance = db.Column()
    distance_error_upper = db.Column()
    distance_error_lower = db.Column()
    distance_ref = db.Column()

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
    pm_ref = db.Column()

    radial_velocity = db.Column()
    radial_velocity_upper = db.Column()
    radial_velocity_lower = db.Column()
    radial_velocity_ref = db.Column()

    a = db.Column()
    a_error_upper = db.Column()
    a_error_lower = db.Column()
    a_ref = db.Column()

    incl = db.Column()
    incl_error_upper = db.Column()
    incl_error_lower = db.Column()
    incl_ref = db.Column()

    e = db.Column()
    e_error_upper = db.Column()
    e_error_lower = db.Column()
    e_ref = db.Column()
    
    w = db.Column()
    w_error_upper = db.Column()
    w_error_lower = db.Column()
    w_ref = db.Column()

    age = db.Column()
    age_error_upper = db.Column()
    age_error_lower = db.Column()
    age_ref = db.Column()

    alt_names = db.Column()
    notes = db.Column()

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"System('This is a multiple star planetary System: {self.system_name}', ' with Gaia DR3 ID', '{self.gaia_id}')"


# The following code is to create a star class with parameters that is only valid for a star  
class Star(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    
    star_name = db.Column( unique=True, nullable=False)
    system_name = db.Column()

    mass = db.Column()
    mass_error_upper = db.Column()
    mass_error_lower = db.Column()
    mass_ref = db.Column()

    radius = db.Column()
    radius_error_upper = db.Column()
    radius_error_lower = db.Column()
    radius_ref = db.Column()

    log_g = db.Column()
    log_g_err_upper = db.Column()
    log_g_err_lower = db.Column()
    log_g_ref = db.Column()

    T_eff = db.Column()
    T_eff_error_upper = db.Column()
    T_eff_error_lower = db.Column()
    T_eff_ref = db.Column()
    
    sp_type = db.Column()

    Fe_H = db.Column()
    Fe_H_error_upper = db.Column()
    Fe_H_error_lower = db.Column()
    M_H = db.Column()
    M_H_error_upper = db.Column()
    M_H_error_lower = db.Column()
    metallicity_ref = db.Column()

    vsini = db.Column()
    vsini_error_upper = db.Column()
    vsini_error_lower = db.Column()
    vsini_ref = db.Column()
    
    Prot= db.Column()
    Prot_err_upper = db.Column()
    Prot_err_lower = db.Column()
    Prot_ref = db.Column()
    
    notes = db.Column()

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"System('This is a star in a multiple star system: {self.star_name}', ' of spectral type', '{self.sp_type}')"


# The following code is to create a planet class with parameters that is only valid for a planet  
class Planet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    
    planet_name = db.Column()
    system_name = db.Column()
    discovery_method = db.Column()
    discovery_ref = db.Column()

    OrbPer = db.Column()
    OrbPer_error_upper = db.Column()
    OrbPer_error_lower = db.Column()
    OrbPer_ref = db.Column()

    mass = db.Column()
    mass_error_upper = db.Column()
    mass_error_lower = db.Column()
    mass_ref = db.Column()

    min_mass = db.Column()
    min_mass_error_upper = db.Column()
    min_mass_error_lower = db.Column()
    min_mass_ref = db.Column()

    radius = db.Column()
    radius_error_upper = db.Column()
    radius_error_lower = db.Column()
    radius_ref = db.Column()

    pl_a = db.Column()
    pl_a_error_upper = db.Column()
    pl_a_error_lower = db.Column()
    pl_a_ref = db.Column()

    pl_e = db.Column()
    pl_e_error_upper = db.Column()
    pl_e_error_lower = db.Column()
    pl_e_ref = db.Column()

    pl_w = db.Column()
    pl_w_error_upper = db.Column()
    pl_w_error_lower = db.Column()
    pl_w_ref = db.Column()

    T_per = db.Column()
    T_per_error_upper = db.Column()
    T_per_error_lower = db.Column()
    T_per_ref = db.Column()

    mean_anomaly = db.Column()
    mean_anomaly_error_upper = db.Column()
    mean_anomaly_error_lower = db.Column()
    mean_anomaly_ref = db.Column()
    
    notes = db.Column()

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"System('This is an exoplanet in a multiple star system: {self.planet_name}', ' discovered using ', '{self.discovery_method}')"

