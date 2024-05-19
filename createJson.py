from flask import Flask, jsonify
from app import app  # Assuming your app initialization is in a separate file
import csv

@app.route('/geojson')
def get_geojson():
  # Read data from CSV and create GeoJSON features
  features = []
  with open('/Data/ForestForecast.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
      # Assuming latitude is in 'latitude' column and longitude is in 'longitude' column
      # and brightness is in 'brightness' column
      latitude = float(row['latitude'])
      longitude = float(row['longitude'])
      brightness = float(row['brightness'])

      # Create a GeoJSON feature with properties for Deck.gl heatmap
      features.append({
          "type": "Feature",
          "geometry": {"type": "Point", "coordinates": [longitude, latitude]},
          "properties": {
              "weight": brightness  # Property for intensity in Deck.gl heatmap
          }
      })

  # Create GeoJSON feature collection
  geojson = {
      "type": "FeatureCollection",
      "features": features
  }

  # Return GeoJSON as JSON response
  return jsonify(geojson)

if __name__ == '__main__':
  app.run(debug=True)