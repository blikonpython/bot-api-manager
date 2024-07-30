import json
import os
import firebase_admin
from firebase_admin import credentials, firestore

# Inicializar Firebase Admin SDK
cred = credentials.Certificate(os.path.join(os.getcwd(), 'firebase_credentials.json'))
firebase_admin.initialize_app(cred)
db = firestore.client()


def get_data(data_type):
    file_path = os.path.join(os.getcwd(), 'data', f'{data_type}.json')
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data


def process_and_store_data(data):
    # Procesar y almacenar datos en Firestore
    collection_ref = db.collection('mexicanna-music')
    document_data = {
        "trigger": data.get("trigger"),
        "elementoId": data.get("elementoId"),
        "placeId": data.get("placeId"),
        "data": data.get("data")
    }
    collection_ref.add(document_data)

    # Guardar en un archivo local (opcional)
    processed_data = {
        "processed_elements": len(data.get("data", [])),
        "elements": data
    }
    storage_path = os.path.join(os.getcwd(), 'storage', 'processed_data.json')
    write_json_to_file(processed_data, storage_path)


def write_json_to_file(data, file_path):
    # Crear el directorio si no existe
    os.makedirs(os.path.dirname(file_path), exist_ok=True)

    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)
