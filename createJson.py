from flask import Flask, jsonify
from app import app  # Assuming your app initialization is in a separate file
import csv



if __name__ == '__main__':
  app.run(debug=True)