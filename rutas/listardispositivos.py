from models import Dispositivo,Usuario
from flask import Blueprint,request,jsonify
from flask_login import login_required,current_user
from flask_jwt_extended import jwt_required, get_jwt_identity

listar=Blueprint("listar",__name__)
@listar.route("/ListarDispo",methods=["GET"])
@jwt_required()
def mostrar():
    user_id=get_jwt_identity()
    usuario=Usuario.query.filter_by(id=user_id).first()
    if usuario:
        lista=[]
        for dispositivo in usuario.dispositivos:
            m={
                "idDis": dispositivo.id_dispositivo,
                "Nombre": dispositivo.nombre
            }
            lista.append(m)    
        return jsonify(lista)
    else:
        return jsonify({"msg":"Usuario no encontrado"}),404   
    
    
    
    