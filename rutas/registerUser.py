from flask import Blueprint, request, jsonify
from models import db,Usuario

create_user = Blueprint("create_user", __name__)

@create_user.route("/RegisterUser", methods=["POST"])
def crearUser():
    datos = request.json
    correo = datos.get("correo")

    # Verificar si el correo electrónico ya está registrado
    usuario_existente = Usuario.query.filter_by(correo=correo).first()
    if usuario_existente:
        return "<h1>ESTE EMAIL YA SE ENCUENTRA REGISTRADO</h1>"

    # Crear el nuevo usuario
    nuevo_usuario = Usuario(usuario=datos.get("usuario"),
                            correo=correo,
                            password=datos.get("password"))

    # Agregar teléfono al usuario si está presente en la solicitud
    if "telefono" in datos:
        nuevo_usuario.telefono = datos.get("telefono")

    db.session.add(nuevo_usuario)
    db.session.commit()

    return jsonify({"mensaje": "Usuario creado exitosamente"}), 201