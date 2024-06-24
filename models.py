from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from flask_sqlalchemy import SQLAlchemy

db=SQLAlchemy()

class Usuario(db.Model, UserMixin):
    __tablename__ = 'usuario'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    usuario = db.Column(db.String(255), unique=True, nullable=False)
    correo = db.Column(db.String(255), unique=True, nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)
    telefono = db.Column(db.String(20), nullable=True)
    dispositivos = db.relationship('Dispositivo', backref='usuario', lazy=True)

    @property
    def password(self):
        raise AttributeError('password is not a readable attribute')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

class Dispositivo(db.Model):
    __tablename__ = 'dispositivo'
    id_dispositivo = db.Column(db.Integer, primary_key=True, autoincrement=True)
    id_usuario = db.Column(db.Integer, db.ForeignKey('usuario.id'), nullable=False)
    ip = db.Column(db.String(15), nullable=False)
    nombre = db.Column(db.String(255), nullable=False)
    topicos = db.relationship('Topico', backref='dispositivo', lazy=True)
    acciones = db.relationship('Accion', backref='dispositivo', lazy=True)

class Topico(db.Model):
    __tablename__ = 'topicos'
    id_topico = db.Column(db.Integer, primary_key=True, autoincrement=True)
    id_dispositivo = db.Column(db.Integer, db.ForeignKey('dispositivo.id_dispositivo'), nullable=False)
    nombre = db.Column(db.String(255), nullable=False)
    categoria = db.Column(db.Enum('accion', 'estado'), nullable=False)
    historiador = db.relationship('Historiador', backref='topico', lazy=True)

class Historiador(db.Model):
    __tablename__ = 'historiador'
    id_historiador = db.Column(db.Integer, primary_key=True, autoincrement=True)
    id_topico = db.Column(db.Integer, db.ForeignKey('topicos.id_topico'), nullable=False)
    dato = db.Column(db.String(255), nullable=False)
    fechayhora = db.Column(db.DateTime, server_default=db.func.now())

class Accion(db.Model):
    __tablename__ = 'accion'
    id_accion = db.Column(db.Integer, primary_key=True, autoincrement=True)
    id_dispositivo = db.Column(db.Integer, db.ForeignKey('dispositivo.id_dispositivo'), nullable=False)
    mensaje = db.Column(db.String(255), nullable=False)
    nombre = db.Column(db.String(255), nullable=False)
