
from werkzeug.security import generate_password_hash, check_password_hash
from database.confbd import db

class Ocupacion(db.Model):
    __tablename__ = 'ocupacion'

    id = db.Column(db.Integer, primary_key = True)
    ciuo88 = db.Column(db.String(10), nullable =False)
    nombre = db.Column(db.String(150), nullable = False)

    def __init__(self, ciuo88, nombre):
        self.ciuo88 = ciuo88;
        self.nombre = nombre;