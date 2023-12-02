from flask import Flask,request,jsonify
from flask_cors import CORS

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


@app.route('/fifa', methods=['GET'])
def get_fifa():
    data = [
    {
      "url": "https://www.nytimes.com/2000/01/01/sports/yacht-racing-elite-survivors-race-toward-cup.html",
      "abstract": "Cruising World exec editor Herb McCormick article notes that victor in Louis Vuitton challengers series will challenge Team New Zealand for America's Cup; photo (M)"
    },
    {
      "url": "https://www.nytimes.com/2000/01/01/sports/transactions-165557.html",
      "abstract": " BASKETBALL    National Basketball Association  ATLANTA HAWKS--Activated G Isaiah Rider .    FOOTBALL    National Football League  NFL--Fined Detroit FS Ron Rice $5,000 for unnecessary roughness against Denver.  CHICAGO BEARS--Signed OL Keno Hills. Placed RB Curtis Enis on injured reserve.  PITTSBURGH STEELERS--Placed TE Mitch Lyons on injured reserve. Signed OLB Reggie Lowe from the practice squad."
    },
    {
      "url": "https://www.nytimes.com/2000/01/01/sports/pro-football-playoffs-or-no-dallas-provides-the-motivation.html",
      "abstract": "Article on upcoming New York Giants-Dallas Cowboys game; photo (M)"
    },
    {
      "url": "https://www.nytimes.com/2000/01/01/opinion/l-on-this-first-day-a-fanfare-for-the-new-era-a-german-century-165689.html",
      "abstract": "Sol Gittleman letter, commenting on Dec 22 editorial, says 21st century could well be the German century; drawing"
    },
    {
      "url": "https://www.nytimes.com/2000/01/01/opinion/l-on-this-first-day-a-fanfare-for-the-new-era-an-asian-century-165670.html",
      "abstract": "Jeffrey Ballinger letter questions Ian Buruma's optimism about Asia's prospects in next century (Op-Ed, Dec 29); drawing"
    }
    ]
    return data

if __name__ == '__main__':
    app.run(debug=True)