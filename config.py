from datetime import timedelta

SECRET_KEY = 'mysecretkey'
SQLALCHEMY_DATABASE_URI = 'mysql://root:my_secret_password@192.168.100.5:6033/app_db'
SQLALCHEMY_TRACK_MODIFICATIONS = False
    # Configuración para Flask-MQTT
MQTT_BROKER_URL = '192.168.100.5'
MQTT_BROKER_PORT = 1883
MQTT_USERNAME = ''
MQTT_PASSWORD = ''
MQTT_KEEPALIVE = 60
MQTT_TLS_ENABLED = False
#FLASK_ENV = 'development'
    
JWT_SECRET_KET="1?1@.f2dAF+13s¨*vas1.c_-1@23-q$%ñsad=?%!3s¨*vas1.c_-1?1@.f2dAF+13s¨*vas1.c_"
JWT_ACCESS_TOKEN_EXPIRES = timedelta(hours=5)
    
    