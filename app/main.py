import flask
from flask import request

app = flask.Flask(__name__)
app.config["DEBUG"] = True

@app.route("/") 
def home_view(): 
    return "<h1>Hello Hello !</h1>"
    
@app.route('/search', methods=['GET'])
def search():
    mix = request.args.get('mix')
    artist = request.args.get('artist')
    artist_searches = request.args.get('artist_searches')
    podcasts_page = request.args.get('podcasts_page')
    return f'<h1>{artist} API base route</p>'
