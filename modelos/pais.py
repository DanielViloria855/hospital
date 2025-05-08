
from werkzeug.security import generate_password_hash, check_password_hash
from database.confbd import db
class Pais(db.Model):
    __tablename__ = 'pais' 
    id       = db.Column(db.Integer, primary_key=True)
    nombre   = db.Column(db.String(15), nullable=False)
    iso_code = db.Column(db.String(20), nullable=False)  

    def __init__(self, nombre, iso_code = None):
        self.nombre = nombre
        self.iso_code = iso_code

