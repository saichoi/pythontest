from movie_model import MovieModel
import requests

def callMovieApi(page=1):

    url = f'''
        https://yts.mx/api/v2/list_movies.json?sort_by=rating&page_number={page}&limit=20
    '''
    response = requests.get(url)

    responseDict = response.json() 
    movies = responseDict["data"]["movies"] 
    return convert_model(movies)

def convert_model(movies):
    list=[]

    for movie in movies:
        movie_model = MovieModel(movie["title"], movie["rating"], movie["small_cover_image"], movie["summary"])
        list.append(movie_model)

    print("title 데이터타입")
    print(type(movie["title"]))
    print("rating 데이터타입")
    print(type(movie["rating"]))
    print(" small_cover_image 데이터타입")
    print(type(movie["small_cover_image"]))
    print("summary 데이터타입")
    print(type(movie["summary"]))

    print(list)
    return list

print(callMovieApi())