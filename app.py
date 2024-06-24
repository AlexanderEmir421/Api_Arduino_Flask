from flask import Flask
from rutas import rutas

app= Flask(__name__)
app.config.from_pyfile('config.py')

from models import db
db.init_app(app)

if __name__=='__main__':
    
    rutas(app)
    app.run(debug=True,host='0.0.0.0')