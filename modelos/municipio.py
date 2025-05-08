from werkzeug.security import generate_password_hash, check_password_hash
from database.confbd import db

class Municipio(db.Model):
    __tablename__ = 'municipio'
    id = db.Column(db.Integer, primary_key =  True)
    divipola = db.Column(db.String(10), nullable = False)
    nombre = db.Column(db.String(100), nullable = False)

    def __init__(self, divipola, nombre):
        self.divipola = divipola;
        self.nombre = nombre;
