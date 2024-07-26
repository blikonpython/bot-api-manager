import json
import os

def get_data(data_type):
    file_path = os.path.join(os.getcwd(), 'data', f'{data_type}.json')
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data
