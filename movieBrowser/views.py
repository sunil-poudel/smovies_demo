from django.shortcuts import render

from movieBrowser.models import MovieBrowse, Genre

# Create your views here.
def index(request):
    return render(request, "index.html")

def access_movies(request, movie_id):
    movie = MovieBrowse.objects.filter(pk=movie_id)
    # movie  = MovieBrowse.objects.all()
    print(movie)
    context = {'movie': movie}
    return render(request, "movies_access.html", context)

def access_genre(request, genre_id):
    genre = Genre.objects.get(pk=genre_id)
    movie = MovieBrowse.objects.filter(genre=genre)
    print(movie)
    print(genre)
    context = {'genre': genre, 'movie': movie}
    return render(request, "genre_access.html", context)