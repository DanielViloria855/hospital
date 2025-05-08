
from werkzeug.security import generate_password_hash, check_password_hash
from database.confbd import db

class Discapacidad(db.Model):
    __tablename__ = 'discapacidad'
    id = db.Column(db.Integer, primary_key =True)
    nombre = db.Column(db.String(30), nullable =False)
    codigo = db.Column(db.String(10), nullable =False)
    descripcion = db.Column(db.String(50), nullable = False) 

    def __init__(self, nombre, codigo, descripcion):
        self.nombre =  nombre;
        self.codigo = codigo;
        self.descripcion = descripcion;
        