from flask import Flask, jsonify, send_from_directory, send_file
from flask_cors import CORS
import csv

app = Flask(__name__, static_folder='static')
CORS(app, origins=['http://localhost:5173', 'forestforecast.lat', 'www.forestforecast.lat', 'forest-forecast.vercel.app'])

@app.route('/', methods=['GET'])
def get_root():
    return '<b><h1>T H E <br/> G A M E</h1></b>'

@app.route('/polygon', methods=['GET'])
def get_polygon():
    coordinates = [
        [-104.15874197858471,20.26589466411704],
        [-104.15127470868725,20.270000995339878],
        [-104.14990141767163,20.267988101457057],
        [-104.14681151288647,20.26975944945283],
        [-104.15136053937573,20.276200544395646],
        [-104.15410712140698,20.273624138514418],
        [-104.15685370343823,20.27740821991942],
        [-104.16406348127026,20.273060544023103],
        [-104.16088774579663,20.268793262143998],
        [-104.15874197858471,20.26589466411704]
    ]
    geojson = {
        "type": "Feature",
        "geometry": {
            "type": "Polygon",
            "coordinates": [coordinates]
        },
        "properties": {}
    }
    return jsonify(geojson)

@app.route('/assets/<path:path>')
def serve_static(path):
    return send_from_directory('assets/', path)

@app.route('/image1', methods=['GET'])
def get_image1():
    return send_file('./assets/image1.png', mimetype='image/png')

@app.route('/data')  # Changed endpoint name to avoid confusion with GeoJSON
def get_data():
  # Read data from CSV and create JSON data
  data = []
  with open('./Data/ForestForecast.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
      # Assuming latitude is in 'latitude' column and longitude is in 'longitude' column
      # and other desired properties are in their corresponding columns
      data.append({
          "coordinates": [float(row['longitude']), float(row['latitude'])],  # Swap order for standard GeoJSON
          "brightness": float(row['brightness']),
          "track": float(row['track']),
          "scan": float(row['scan']),
      })

      if len(data) >= 30000:
         return jsonify(data)

  return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
