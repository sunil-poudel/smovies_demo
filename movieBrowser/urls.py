from django.urls import path

app_name='movieBrowser'

from movieBrowser import views
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:movie_id>', views.access_movies, name='movie_access'),
    path('genre/<int:genre_id>', views.access_genre, name='genre_access'),
]