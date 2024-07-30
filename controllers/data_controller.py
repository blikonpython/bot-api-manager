from flask import Blueprint, jsonify, request
from services.data_service import get_data, process_and_store_data

data_blueprint = Blueprint('data_blueprint', __name__)

@data_blueprint.route('/api/mexicana', methods=['GET'])
def mexicana():
    data = get_data('mexicana')
    return jsonify(data)

@data_blueprint.route('/api/submit_data', methods=['POST'])
def submit_data():
    data = request.json
    process_and_store_data(data)
    response_data = get_data('mensaje')
    return jsonify(response_data)
