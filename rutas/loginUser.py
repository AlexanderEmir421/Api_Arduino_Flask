from flask import Blueprint, request, jsonify, make_response
from flask_login import login_user
from app.models import Usuario
from flask_jwt_extended import create_access_token
from app import db

loginuser = Blueprint("loginuser", __name__)

@loginuser.route("/login", methods=['POST'])
def logear():
    datos = request.json
    usuario = datos.get("usuario")
    password = datos.get("password")
    
    if not usuario or not password:
        return make_response(jsonify({"message": "Usuario y contraseña son requeridos"}), 400)
    
    user = db.session.query(Usuario).filter_by(usuario=usuario).first()  # Utiliza la sesión de db para consultar la base de datos
    
    if user and user.verify_password(password):
        login_user(user)
        access_token = create_access_token(identity=user.id)
        # Devolvemos el token de acceso junto con el usuario
        return jsonify(access_token=access_token, usuario=usuario), 200
    else:
        return make_response(jsonify({"message": "Usuario o contraseña inválidos"}), 401)
