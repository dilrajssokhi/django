from django.contrib import admin
from .models import Movie

# Register your models here.
class MovieAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['movie_name','movie_director','movie_genre','movie_99popularity','movie_imdbscore']}),
        ('Date information', {'fields': ['entry_date'], 'classes': ['collapse']}),
    ]
    list_display = ('movie_name', 'movie_director', 'movie_imdbscore', 'movie_genre', 'entry_date')
    list_filter = ['entry_date']
    search_fields = ['movie_name', 'movie_director', 'movie_genre']

admin.site.register(Movie, MovieAdmin)

