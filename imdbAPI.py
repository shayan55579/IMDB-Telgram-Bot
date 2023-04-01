import requests


def Search_Movie(search_ithem):
    # https://imdb-api.com/en/API/SearchMovie/k_0cgposgg/inception 2010
    global IMDB_USER_KEY
    IMDB_USER_KEY = r'k_0cgposgg'
    # search_ithem = str(input())
    IMDB_API = r'https://imdb-api.com/en/API/Search/{}/{}'.format(IMDB_USER_KEY, search_ithem)
    response = requests.get(IMDB_API)
    feed = response.json()
    result = feed.get('results')
    list_of_movies = []  # list of Movies based on Search
    for i in range(len(result)):
        list_of_movies.append(result[i].get('title'))
    return list_of_movies


def search_imdb_movies(movie_name: str) -> list:
    IMDB_USER_KEY = "k_0cgposgg"

    IMDB_API = f"https://imdb-api.com/en/API/SearchMovie/{IMDB_USER_KEY}/{movie_name}"
    response = requests.get(IMDB_API)
    feed = response.json()
    list_of_movies = []
    global res
    res = feed['results']
    for result in feed.get("results", []):
        title = result.get("title")
        if title:
            list_of_movies.append(title)

    return list_of_movies


def get_movie_info_by_number(number):
    info_dict = {}
    for key, value in res[number].items():
        info_dict[key] = value
    return info_dict




