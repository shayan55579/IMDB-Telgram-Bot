import requests

#https://imdb-api.com/en/API/Search/k_12345678/inception 2010

IMDB_USER_KEY = r'k_12345678'
search_ithem = 'inception'
IMDB_API = r'https://imdb-api.com/en/API/Search/{}/{}'.format(IMDB_USER_KEY,search_ithem)
response = requests.get(IMDB_API)



print(response)