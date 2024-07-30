import json
import os


def write_json_to_file(data, file_path):
    # Crear el directorio si no existe
    os.makedirs(os.path.dirname(file_path), exist_ok=True)

    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)
