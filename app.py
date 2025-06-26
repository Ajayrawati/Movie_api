from flask import Flask,jsonify,json,send_file,Response
from main import extract_info
import json


app = Flask(__name__)



@app.route('/',methods=['GET'])
def base_file():
    return send_file('static/html/index.html')


@app.route('/api/movie/<title>', methods=['GET'])
def fetch_movie_details(title):
    url = f"https://www.imdb.com/find/?q={title}"
    movieData =extract_info(url)
    response = Response(
        json.dumps(movieData, indent=4),
        content_type='application/json'
    )
    return response

@app.route('/api/movie/horrer250',methods=['GET'])
def fetch_top_250_horrer():
    return send_file('static/cleanedMovieData.json')

@app.route('/api/movie/top250',methods=['GET'])
def fetch_top_250_movies():
    return send_file('static/movieData.json', mimetype='application/json')





