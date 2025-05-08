from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def inicializar(app):
    # Configuración de la base de datos
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://hospital_sma9_user:IrmNLA30D2FAKrpdK7rjbkHX2F6Rb3UJ@dpg-d0dcubqdbo4c738e0un0-a.oregon-postgres.render.com/hospital_sma9'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)

