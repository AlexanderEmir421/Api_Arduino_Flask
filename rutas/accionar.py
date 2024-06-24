from models import Accion,db
from flask import Blueprint,request,jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity

accionar=Blueprint("accionar",__name__)

@accionar.route("\Accionar",method=['POST'])
@jwt_required
def accion():
    dato=request.json
    dispo=dato.get("idDispo")
    idAccion=dato.get("idAccion")
    hacer=dato.get("accion")
    accionar=Accion.query.filter_by(id_dispositivo=dispo,id_accion=idAccion).first()
    if accionar:
        topico=accionar.mensaje       
        mqtt.publish(topico, 1)
    
    