import source
import json

def import_data():
    raw_data = open('data.json')
    final_data = json.load(raw_data)
    return(final_data)
