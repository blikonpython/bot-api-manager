import os
from flask import Flask
from dotenv import load_dotenv
from controllers.data_controller import data_blueprint

# Cargar las variables de entorno desde el archivo .env
load_dotenv()

app = Flask(__name__)

# Registrar Blueprints
app.register_blueprint(data_blueprint)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000, debug=True)
