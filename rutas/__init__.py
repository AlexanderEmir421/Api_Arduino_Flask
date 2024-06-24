from flask import Blueprint
#from .listardispositivos import listar
#from .loginUser import loginuser
from .registerUser import create_user
from .registerDevice import device_create
#from .historiador import historiador
def rutas(app):
    #app.register_blueprint(loginuser)
    app.register_blueprint(device_create)
    app.register_blueprint(create_user)
    #app.register_blueprint(listar)
    #app.register_blueprint(historiador)
    
    