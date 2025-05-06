
from flask import Flask, flash, render_template, request, jsonify, redirect, url_for
from flask_login import LoginManager, current_user, login_required, login_user
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from database import confbd
from sqlalchemy import text
from database.confbd import db, inicializar

app = Flask(__name__)
confbd.inicializar(app)


#RUTA PARA PROBAR CONEXION 
@app.route('/test-db')
def test_db():
    try:
       
        result = db.session.execute(text('SELECT 1'))
        return 'Conexión exitosa a la base de datos 🟢'
    except Exception as e:
        return f'Error al conectar con la base de datos 🔴: {str(e)}'

if __name__ == '__main__':
    app.run(debug=True)