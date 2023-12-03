from flask import Flask,request,jsonify
from flask_cors import CORS
from chromac import find_similiar 
import csv
import random

app = Flask(__name__)
CORS(app, resources={r"*": {"origins": "*"}})

def stream_csv_data(file_path):
    with open(file_path, 'r', encoding='utf-8') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            yield row




# Select 24 random objects from the streamed data
def select_random_objects(streamed_data, num_objects):
    random_objects = []
    for i, row in enumerate(streamed_data):
        if i < num_objects:
            random_objects.append(row)
        else:
            break
    return random_objects


@app.route('/')
def hello():
    return 'Hello, World!'


# Route for sending 24 random objects as JSON
@app.route('/getdata', methods=['GET'])
def get_random_objects():
    file_path = 'nyt-metadata.csv'  # Replace with the actual file path
    num_objects = 24
    streamed_data = stream_csv_data(file_path)
    random_objects = select_random_objects(streamed_data, num_objects)
    return jsonify(random_objects)


@app.route('/search', methods=['GET'])
def get_search():
    data = request.headers.get('search')
    results = find_similiar(data)
    return jsonify(results)

if __name__ == '__main__':
    app.run(debug=True)