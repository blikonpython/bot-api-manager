import json
import os
import firebase_admin
from firebase_admin import credentials, firestore
from dotenv import load_dotenv

# Cargar las variables de entorno desde el archivo .env
load_dotenv()

# Inicializar Firebase Admin SDK con variable de entorno
firebase_credentials = os.getenv('FIREBASE_CREDENTIALS')
if firebase_credentials:
    cred = credentials.Certificate(json.loads(firebase_credentials))
    firebase_admin.initialize_app(cred)
else:
    raise ValueError("La variable de entorno FIREBASE_CREDENTIALS no está configurada.")

db = firestore.client()

def get_data(data_type):
    file_path = os.path.join(os.getcwd(), 'data', f'{data_type}.json')
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data

def process_and_store_data(data):
    collection_ref = db.collection('mexicanna-music')
    document_data = {
        "trigger": data.get("trigger"),
        "elementoId": data.get("elementoId"),
        "placeId": data.get("placeId"),
        "data": data.get("data")
    }
    collection_ref.add(document_data)
    processed_data = {
        "processed_elements": len(data.get("data", [])),
        "elements": data
    }
    storage_path = os.path.join(os.getcwd(), 'storage', 'processed_data.json')
    write_json_to_file(processed_data, storage_path)

def write_json_to_file(data, file_path):
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)
