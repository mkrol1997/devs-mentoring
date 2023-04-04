import requests


API_KEY = "e77bd7b7858fecdf900c0286f25d887c"
API_ENDPOINT = "https://api.themoviedb.org/3/search/movie"

params = {
    "api_key": "e77bd7b7858fecdf900c0286f25d887c",
    "query": "titanic"

}
response = requests.get(API_ENDPOINT, params=params)
print(response.text)