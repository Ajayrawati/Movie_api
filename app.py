from flask import Flask,jsonify,json,send_file
from main import extract_info
import json


app = Flask(__name__)



@app.route('/api/movie/<title>', methods=['GET'])
def fetch_movie_details(title):
    url = f"https://www.imdb.com/find/?q={title}"
    movieData =extract_info(url)
    return jsonify(movieData);


@app.route('/api/movie/top250',methods=['GET'])
def fetch_top_250_movies():
    return send_file('static/movieData.json', mimetype='application/json')




