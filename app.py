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
    app.run(debug=True)
