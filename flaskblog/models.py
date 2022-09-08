from flaskblog import db

class User(db.Model):
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

    system_name = db.Column(db.String(100), nullable=False)
    gaia_id = db.Column(db.String(100), unique=True)

    sp_type = db.Column(db.String(100))
    sp_type_ref = db.Column(db.Text)

    ra = db.Column(db.Float(60))
    ra_error_upper = db.Column(db.Float(60))
    ra_error_lower = db.Column(db.Float(60))
    dec = db.Column(db.Float(60))
    dec_error_upper = db.Column(db.Float(60))
    dec_error_lower = db.Column(db.Float(60))
    ra_dec_ref = db.Column(db.Text)

    parallax = db.Column(db.Float(60))
    parallax_error = db.Column(db.Float(60))
    distance = db.Column(db.Float(60))
    distance_error_upper = db.Column(db.Float(60))
    distance_error_lower = db.Column(db.Float(60))
    distance_ref = db.Column(db.Text)

    distance_gspphot = db.Column(db.Float(60))
    distance_gspphot_upperper = db.Column(db.Float(60))
    distance_gspphot_lower = db.Column(db.Float(60))

    pmra = db.Column(db.Float(60))
    pmra_error_upper = db.Column(db.Float(60))
    pmra_error_lower = db.Column(db.Float(60))
    pmdec = db.Column(db.Float(60))
    pmdec_error_upper = db.Column(db.Float(60))
    pmdec_error_lower = db.Column(db.Float(60))
    pm = db.Column(db.Float(60))
    pm_ref = db.Column(db.Text)

    radial_velocity = db.Column(db.Float(60))
    radial_velocity_upper = db.Column(db.Float(60))
    radial_velocity_lower = db.Column(db.Float(60))
    radial_velocity_ref = db.Column(db.Text)

    a = db.Column(db.Float(60))
    a_error_upper = db.Column(db.Float(60))
    a_error_lower = db.Column(db.Float(60))
    a_ref = db.Column(db.Text)

    incl = db.Column(db.Float(60))
    incl_error_upper = db.Column(db.Float(60))
    incl_error_lower = db.Column(db.Float(60))
    incl_ref = db.Column(db.Text)

    e = db.Column(db.Float(60))
    e_error_upper = db.Column(db.Float(60))
    e_error_lower = db.Column(db.Float(60))
    e_ref = db.Column(db.Text)
    
    w = db.Column(db.Float(60))
    w_error_upper = db.Column(db.Float(60))
    w_error_lower = db.Column(db.Float(60))
    w_ref = db.Column(db.Text)

    age = db.Column(db.Float(60))
    age_error_upper = db.Column(db.Float(60))
    age_error_lower = db.Column(db.Float(60))
    age_ref = db.Column(db.Text)

    alt_names = db.Column(db.Text)
    notes = db.Column(db.Text)

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"System('System: {self.system_name}', ' with Gaia DR3 ID', '{self.gaia_id}')"
