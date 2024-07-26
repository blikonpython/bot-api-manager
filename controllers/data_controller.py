from flask import Blueprint, jsonify
from services.data_services import get_data

data_blueprint = Blueprint('data_blueprint', __name__)

@data_blueprint.route('/api/mexicana', methods=['GET'])
def mexicana():
    data = get_data('mexicana')
    return jsonify(data)

@data_blueprint.route('/api/mostrar_info', methods=['GET'])
def mostrar_info():
    data = get_data('mostrarinfo')
    return jsonify(data)

@data_blueprint.route('/api/mensaje', methods=['GET'])
def mensaje():
    data = get_data('mensaje')
    return jsonify(data)

@data_blueprint.route('/api/respuesta', methods=['GET'])
def respuesta():
    data = get_data('respuesta')
    return jsonify(data)

@data_blueprint.route('/api/formulario', methods=['GET'])
def formulario():
    data = get_data('formulario')
    return jsonify(data)
