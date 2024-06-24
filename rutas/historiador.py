from datetime import datetime
from models import db,Dispositivo,Usuario,Historiador
from flask import Blueprint,request,jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity

historiador=Blueprint("historiador",__name__)
@historiador.route("/Historiador",methods=["POST"])
@jwt_required()
def mostrar():
    fecha_actual = datetime.now().date()
    mensaje=[]
    dato=request.json
    idDevice=dato.get("id-device")
    user=Usuario.query.filter_by(id=get_jwt_identity()).first()
    if user:
        dispositivo=Dispositivo.query.filter_by(id_dispositivo=idDevice,id_usuario=user.id).first()
        if dispositivo:
            for sensores in dispositivo.topicos:
                if sensores.categoria == "accion":
                    m={
                        "Nombre":sensores.nombre,
                    }   
                    mensaje.append(m) 
                else:
                    data=[]
                    Historiadores=Historiador.query.filter_by(id_topico=sensores.id_topico, fechayhora=fecha_actual).all()
                    for d in Historiadores:
                        data.append(d.dato)
                    m={
                        "Nombre":sensores.nombre,
                        "Dato": data
                    }      
                    mensaje.append(m)
            return jsonify(mensaje)
        else:
            pass
    else:
        pass
            
    