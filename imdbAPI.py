import requests


def Search_Movie():
    #https://imdb-api.com/en/API/SearchMovie/k_0cgposgg/inception 2010
    IMDB_USER_KEY = r'k_0cgposgg'
    search_ithem = str(input())
    IMDB_API = r'https://imdb-api.com/en/API/Search/{}/{}'.format(IMDB_USER_KEY,search_ithem)
    response = requests.get(IMDB_API)
    feed = response.json()
    result = feed.get('results')
    list_of_movies = [] # list of Movies based on Search
    for i in range(len(result)):
        list_of_movies.append(result[i].get('title'))
    return list_of_movies