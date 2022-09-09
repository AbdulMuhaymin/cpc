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

    systems = db.relationship('System', backref='author', lazy=True)

    def __repr__(self):
        return f"User('{self.username}', {self.email}', {self.image_file}')"

class System(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    system_name = db.Column(db.String, nullable=False)
    gaia_id = db.Column(db.String)

    sp_type = db.Column(db.String)
    sp_type_ref = db.Column(db.String)

    ra = db.Column(db.String)
    ra_error_upper = db.Column(db.String)
    ra_error_lower = db.Column(db.String)
    dec = db.Column(db.String)
    dec_error_upper = db.Column(db.String)
    dec_error_lower = db.Column(db.String)
    ra_dec_ref = db.Column(db.Text)

    parallax = db.Column(db.String)
    parallax_error = db.Column(db.String)
    distance = db.Column(db.String)
    distance_error_upper = db.Column(db.String)
    distance_error_lower = db.Column(db.String)
    distance_ref = db.Column(db.Text)

    distance_gspphot = db.Column(db.String)
    distance_gspphot_upper = db.Column(db.String)
    distance_gspphot_lower = db.Column(db.String)

    pmra = db.Column(db.String)
    pmra_error_upper = db.Column(db.String)
    pmra_error_lower = db.Column(db.String)
    pmdec = db.Column(db.String)
    pmdec_error_upper = db.Column(db.String)
    pmdec_error_lower = db.Column(db.String)
    pm = db.Column(db.String)
    pm_ref = db.Column(db.Text)

    radial_velocity = db.Column(db.String)
    radial_velocity_upper = db.Column(db.String)
    radial_velocity_lower = db.Column(db.String)
    radial_velocity_ref = db.Column(db.Text)

    a = db.Column(db.String)
    a_error_upper = db.Column(db.String)
    a_error_lower = db.Column(db.String)
    a_ref = db.Column(db.Text)

    incl = db.Column(db.String)
    incl_error_upper = db.Column(db.String)
    incl_error_lower = db.Column(db.String)
    incl_ref = db.Column(db.Text)

    e = db.Column(db.String)
    e_error_upper = db.Column(db.String)
    e_error_lower = db.Column(db.String)
    e_ref = db.Column(db.Text)
    
    w = db.Column(db.String)
    w_error_upper = db.Column(db.String)
    w_error_lower = db.Column(db.String)
    w_ref = db.Column(db.Text)

    age = db.Column(db.String)
    age_error_upper = db.Column(db.String)
    age_error_lower = db.Column(db.String)
    age_ref = db.Column(db.Text)

    alt_names = db.Column(db.String)
    notes = db.Column(db.String)

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"System('System: {self.system_name}', ' with Gaia DR3 ID', '{self.gaia_id}')"

class Star(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    system_name = db.Column(db.String, nullable=False)
    gaia_id = db.Column(db.String)

    sp_type = db.Column(db.String)
    sp_type_ref = db.Column(db.String)

    ra = db.Column(db.String)
    ra_error_upper = db.Column(db.String)
    ra_error_lower = db.Column(db.String)
    dec = db.Column(db.String)
    dec_error_upper = db.Column(db.String)
    dec_error_lower = db.Column(db.String)
    ra_dec_ref = db.Column(db.Text)

    parallax = db.Column(db.String)
    parallax_error = db.Column(db.String)
    distance = db.Column(db.String)
    distance_error_upper = db.Column(db.String)
    distance_error_lower = db.Column(db.String)
    distance_ref = db.Column(db.Text)

    distance_gspphot = db.Column(db.String)
    distance_gspphot_upper = db.Column(db.String)
    distance_gspphot_lower = db.Column(db.String)

    pmra = db.Column(db.String)
    pmra_error_upper = db.Column(db.String)
    pmra_error_lower = db.Column(db.String)
    pmdec = db.Column(db.String)
    pmdec_error_upper = db.Column(db.String)
    pmdec_error_lower = db.Column(db.String)
    pm = db.Column(db.String)
    pm_ref = db.Column(db.Text)

    radial_velocity = db.Column(db.String)
    radial_velocity_upper = db.Column(db.String)
    radial_velocity_lower = db.Column(db.String)
    radial_velocity_ref = db.Column(db.Text)

    a = db.Column(db.String)
    a_error_upper = db.Column(db.String)
    a_error_lower = db.Column(db.String)
    a_ref = db.Column(db.Text)

    incl = db.Column(db.String)
    incl_error_upper = db.Column(db.String)
    incl_error_lower = db.Column(db.String)
    incl_ref = db.Column(db.Text)

    e = db.Column(db.String)
    e_error_upper = db.Column(db.String)
    e_error_lower = db.Column(db.String)
    e_ref = db.Column(db.Text)
    
    w = db.Column(db.String)
    w_error_upper = db.Column(db.String)
    w_error_lower = db.Column(db.String)
    w_ref = db.Column(db.Text)

    age = db.Column(db.String)
    age_error_upper = db.Column(db.String)
    age_error_lower = db.Column(db.String)
    age_ref = db.Column(db.Text)

    alt_names = db.Column(db.String)
    notes = db.Column(db.String)

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"System('System: {self.system_name}', ' with Gaia DR3 ID', '{self.gaia_id}')"

class Planet(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    system_name = db.Column(db.String, nullable=False)
    gaia_id = db.Column(db.String)

    sp_type = db.Column(db.String)
    sp_type_ref = db.Column(db.String)

    ra = db.Column(db.String)
    ra_error_upper = db.Column(db.String)
    ra_error_lower = db.Column(db.String)
    dec = db.Column(db.String)
    dec_error_upper = db.Column(db.String)
    dec_error_lower = db.Column(db.String)
    ra_dec_ref = db.Column(db.Text)

    parallax = db.Column(db.String)
    parallax_error = db.Column(db.String)
    distance = db.Column(db.String)
    distance_error_upper = db.Column(db.String)
    distance_error_lower = db.Column(db.String)
    distance_ref = db.Column(db.Text)

    distance_gspphot = db.Column(db.String)
    distance_gspphot_upper = db.Column(db.String)
    distance_gspphot_lower = db.Column(db.String)

    pmra = db.Column(db.String)
    pmra_error_upper = db.Column(db.String)
    pmra_error_lower = db.Column(db.String)
    pmdec = db.Column(db.String)
    pmdec_error_upper = db.Column(db.String)
    pmdec_error_lower = db.Column(db.String)
    pm = db.Column(db.String)
    pm_ref = db.Column(db.Text)

    radial_velocity = db.Column(db.String)
    radial_velocity_upper = db.Column(db.String)
    radial_velocity_lower = db.Column(db.String)
    radial_velocity_ref = db.Column(db.Text)

    a = db.Column(db.String)
    a_error_upper = db.Column(db.String)
    a_error_lower = db.Column(db.String)
    a_ref = db.Column(db.Text)

    incl = db.Column(db.String)
    incl_error_upper = db.Column(db.String)
    incl_error_lower = db.Column(db.String)
    incl_ref = db.Column(db.Text)

    e = db.Column(db.String)
    e_error_upper = db.Column(db.String)
    e_error_lower = db.Column(db.String)
    e_ref = db.Column(db.Text)
    
    w = db.Column(db.String)
    w_error_upper = db.Column(db.String)
    w_error_lower = db.Column(db.String)
    w_ref = db.Column(db.Text)

    age = db.Column(db.String)
    age_error_upper = db.Column(db.String)
    age_error_lower = db.Column(db.String)
    age_ref = db.Column(db.Text)

    alt_names = db.Column(db.String)
    notes = db.Column(db.String)

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"System('System: {self.system_name}', ' with Gaia DR3 ID', '{self.gaia_id}')"

