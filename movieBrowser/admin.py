from django.contrib import admin
from movieBrowser.models import MovieBrowse, Genre

class GenreAdmin(admin.ModelAdmin):
    list_display = ('id','genre')

class MovieBrowseAdmin(admin.ModelAdmin):
    list_display = ('id','name', 'releaseDate', 'metacriticScore', 'reviews', 'genre')
# Register your models here.
admin.site.register(Genre, GenreAdmin)
admin.site.register(MovieBrowse, MovieBrowseAdmin)
