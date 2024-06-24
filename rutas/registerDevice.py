from flask import Blueprint, request, jsonify
from models import db,Dispositivo, Topico, Accion

device_create = Blueprint("device_create", __name__)

@device_create.route("/regDevice", methods=["POST"])
def crear():
    #user_id=get_jwt_identity()
    datos = request.json
    ip = datos.get("ip")
    user_id=datos.get("idusuario")
    nameDispo=datos.get("nombre")
    device = Dispositivo(ip=ip, id_usuario=user_id,nombre=nameDispo)
    db.session.add(device)
    db.session.commit()
    if device.id_dispositivo:
        message = []
        for category, names in datos["Topicos"].items():
            for name in names:
                topic = Topico(nombre=name, categoria=category, id_dispositivo=device.id_dispositivo)
                db.session.add(topic)
                db.session.commit()  # Confirmar la creación del tema antes de obtener su ID
                mensaje = f"{user_id}/{device.id_dispositivo}/{topic.id_topico}/{topic.nombre}"
                message.append(mensaje)
                if category == "Accion":
                    tableAction = Accion(id_dispositivo=device.id_dispositivo, mensaje=mensaje, nombre=topic.nombre)
                    db.session.add(tableAction)
                    db.session.commit()
        db.session.commit()
        return jsonify({"mensaje": message}), 201  # Devolver una respuesta JSON con el mensaje y el código 201 para indicar éxito
    else:
        return jsonify({"error": "No se pudo crear el dispositivo"}), 400  # Devolver una respuesta JSON con el error y el código 400 para indicar un error de cliente

    