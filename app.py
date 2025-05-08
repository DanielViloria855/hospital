
from flask import Flask, flash, render_template, request, jsonify, redirect, url_for
from flask_login import LoginManager, current_user, login_required, login_user
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from database import confbd
from sqlalchemy import text
from database.confbd import db, inicializar
from modelos.discapacidad import Discapacidad
from modelos.municipio import Municipio
from modelos.ocupacion import Ocupacion
from modelos.pais import Pais


app = Flask(__name__)
inicializar(app)
migrate = Migrate(app, db)

#RUTA PARA PROBAR CONEXION 
@app.route('/test-db')
def test_db():
    try:
       
        result = db.session.execute(text('SELECT 1'))
        return 'Conexión exitosa a la base de datos 🟢'
    except Exception as e:
        return f'Error al conectar con la base de datos 🔴: {str(e)}'


@app.route('/paises', methods = ["GET"])
def paises ():
    lista_paises = Pais.query.order_by(Pais.nombre).all()
    return render_template("paises.html", paises = lista_paises)

@app.route('/discapacidad', methods = ["GET"])
def discapacidades ():
     lista_discapacidades = Discapacidad.query.order_by(Discapacidad.nombre).all() 
     return render_template("discapacidades.html", discapacidades = lista_discapacidades)

@app.route('/ocupacion', methods = ["GET"])
def ocupaciones ():
    lista_ocupaciones = Ocupacion.query.order_by(Ocupacion.nombre).all()
    return render_template("ocupaciones.html", ocupacion = lista_ocupaciones)

@app.route('/municipio', methods = ["GET"])
def municipios ():
    lista_municipio = Municipio.query.order_by(Municipio.nombre).all()
    return render_template("municipios.html", municipio = lista_municipio)

if __name__ == '__main__':
    with app.app_context():  
        db.create_all()
    app.run(host="0.0.0.0", port=5000, debug=True)