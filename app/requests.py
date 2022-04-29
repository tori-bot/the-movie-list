
import urllib.request,json#fetch data from api and renders it in json format
from .models import Movie

#getting api key
api_key=None

#getting movie base url
base_url=None

def configure_request(app):
    global api_key,base_url
    api_key=app.config['MOVIE_API_KEY']
    base_url=app.config['MOVIE_API_BASE_URL']

def get_movies(category):
    #function[args:category] gets json response to our url request

    get_movies_url=base_url.format(category,api_key)#replace {}s in base_url with category and api-key to get final url

    with urllib.request.urlopen(get_movies_url) as url:
        get_movies_data=url.read()#read response & store it in this variable
        get_movies_response=json.loads(get_movies_data)#convert json response to python dictionary

        movie_results=None

        if get_movies_response['results']:
            movie_results_list=get_movies_response['results']
            movie_results=process_results(movie_results_list)
    return movie_results


def process_results(movie_list):
    #function processes movie result and transform them to a list of objects
    movie_results=[]

    #loop through the list of dictionaries using the get() method and pass in the keys so that we can access the values.
    for movie_item in movie_list:
        index=movie_item.get('id')
        title=movie_item.get('original_title')
        overview=movie_item.get('overview')
        poster=movie_item.get('poster_path')
        vote_average=movie_item.get('vote_average')
        vote_count=movie_item.get('vote_count')

        if poster:
            movie_object=Movie(index,title,overview,poster,vote_average,vote_count)

            movie_results.append(movie_object)

    return movie_results

def get_movie(index):
    get_movie_details_url=base_url.format(index,api_key)

    with urllib.request.urlopen(get_movie_details_url) as url:
        movie_details_data=url.read()
        movie_details_response=json.loads(movie_details_data)

        movie_object=None

        if movie_details_response:
            index=movie_details_response.get('id')
            title=movie_details_response.get('original_title')
            overview=movie_details_response.get('overview')
            poster=movie_details_response.get('poster_path')
            vote_average=movie_details_response.get('vote_average')
            vote_count=movie_details_response.get('vote_count')

            movie_object=Movie(index,title,overview,poster,vote_average,vote_count)
            print(movie_object)

    return movie_object

def search_movie(movie_name):
    search_movie_url='https://api.themoviedb.org/3/search/movie?api_key={}&query={}'.format(api_key,movie_name)

    with urllib.request.urlopen(search_movie_url) as url:
        search_movie_data=url.read()
        search_movie_response=json.loads(search_movie_data)

        search_movie_results=None

        if search_movie_response['results']:
            search_movie_list=search_movie_response['results']
            search_movie_results=process_results(search_movie_list)

    return search_movie_results

