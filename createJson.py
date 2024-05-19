from flask import Flask, jsonify
from app import app
import csv

@app.route('/geojson')
def get_geojson():
  # Read data from CSV and create GeoJSON features
  features = []
  with open('/Data/ForestForecast.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
      # Assuming latitude is in 'latitude' column and longitude is in 'longitude' column
      latitude = float(row['latitude'])
      longitude = float(row['longitude'])
      # Add other properties from the CSV row to the feature dictionary
      properties = {key: value for key, value in row.items() if key not in ['latitude', 'longitude']}
      features.append({
          "type": "Feature",
          "geometry": {"type": "Point", "coordinates": [longitude, latitude]},
          "properties": properties
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