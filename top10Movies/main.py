from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import requests

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///new-books-collection.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
Bootstrap(app)
db = SQLAlchemy(app)

API_KEY = "e77bd7b7858fecdf900c0286f25d887c"
API_SEARCH_MOVIES_ENDPOINT = "https://api.themoviedb.org/3/search/movie"
API_MOVIE_DETAILS_ENDPOINT = "https://api.themoviedb.org/3/movie/"
MOVIE_URL = "https://image.tmdb.org/t/p/w500"


class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), unique=False, nullable=False)
    year = db.Column(db.String(4), unique=False, nullable=False)
    description = db.Column(db.String(280), unique=True, nullable=False)
    rating = db.Column(db.Float, nullable=True)
    ranking = db.Column(db.Integer, nullable=True)
    review = db.Column(db.String(280), unique=True, nullable=True)
    img_url = db.Column(db.String(280), unique=True, nullable=True)


app.app_context().push()


class AddMovieForm(FlaskForm):
    title = StringField('Movie Title')
    submit = SubmitField("Add Movie")

class UpdateForm(FlaskForm):
    rating = StringField('Your Rating Out of 10 e.g. 7.5')
    review = StringField('Your review')
    submit = SubmitField("Submit")


def search_movie(movie_title):
    params = {
        "api_key": API_KEY,
        "query": movie_title,
    }
    response = requests.get(API_SEARCH_MOVIES_ENDPOINT, params=params)
    return response.json()["results"]


def get_movie_details(movie_id):
    params = {
        "api_key": API_KEY,
        "language": "en-US",
    }
    response = requests.get(API_MOVIE_DETAILS_ENDPOINT+movie_id, params=params)
    return response.json()


@app.route("/")
def home():
    all_movies = Movie.query.order_by("rating").all()
    return render_template("index.html", movies=all_movies)


@app.route("/update", methods=["GET", "POST"])
def update():
    if request.method == "GET":
        form = UpdateForm()
        movie_id = request.args.get("id")
        movie = Movie.query.filter_by(id=movie_id).first()
        return render_template("edit.html", movie=movie, form=form)
    else:
        form = UpdateForm()
        if form.validate_on_submit():
            new_rating = form.rating.data
            new_review = form.review.data
            movie_id = request.form["id"]
            movie = Movie.query.filter_by(id=movie_id).first()
            if new_rating:
                movie.rating = new_rating
            if len(new_review) != 0:
                movie.review = new_review
            db.session.commit()
            return redirect(url_for("home"))


@app.route("/delete")
def delete():
    movie_id = request.args.get("id")
    movie_to_delete = Movie.query.filter_by(id=movie_id).first()
    db.session.delete(movie_to_delete)
    db.session.commit()
    return redirect(url_for("home"))


@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "GET":
        form = AddMovieForm()
        return render_template("add.html", form=form)
    else:
        form = AddMovieForm()
        title = form.title.data
        movies_data = search_movie(title)
        return render_template("select.html", movies=movies_data)


@app.route("/add_movie")
def add_movie():
    movie_id = request.args.get("id")
    movie_details = get_movie_details(movie_id)
    movie = Movie(title=movie_details["original_title"], year=movie_details["release_date"], rating=None,
                  description=movie_details["overview"], img_url=MOVIE_URL+movie_details["poster_path"])
    db.session.add(movie)
    db.session.commit()
    return redirect(url_for("update", id=movie.id))


if __name__ == '__main__':
    app.run(debug=True)
