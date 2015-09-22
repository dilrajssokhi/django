from django.shortcuts import render, render_to_response, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Movie
from django.db.models import Q

def index(request):
    movies_list = Movie.objects.order_by('-entry_date')
    paginator = Paginator(movies_list, 25)

    page = request.GET.get('page')
    try:
        movies = paginator.page(page)
    except PageNotAnInteger:
        movies = paginator.page(1)
    except EmptyPage:
        movies = paginator.page(paginator.num_pages)

    context = {'movies_list': movies}
    return render_to_response('movies/index.html', context)

def detail(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)
    return render(request, 'movies/detail.html', {'movie': movie})

 
def search(request):
    if request.method == 'GET':
        return render(request, 'movies/search.html', {})
    elif request.method == 'POST':
        formtext = request.POST['search']
        movies_list = []

        formtext_list = formtext.split("=")
        if (len(formtext_list) > 1):
            search_key = formtext_list[0].replace(" ","")
            search_val = formtext_list[1]
            if (search_key == "title"):
                movies_list = Movie.objects.filter(movie_name__contains = search_val)
            elif (search_key == "director"):
                movies_list = Movie.objects.filter(movie_director__contains = search_val)
            elif (search_key == "imdbscore"):
                if (search_val.isnumeric()):
                    movies_list = Movie.objects.filter(movie_imdbscore__gte = search_val)
            elif (search_key == "99popularity"):
                if (search_val.isnumeric()):
                    movies_list = Movie.objects.filter(movie_99popularity__gte = search_val)
            elif (search_key == "genre"):
                genres = search_val.split(",")
                for index,genre in enumerate(genres):
                    if (index == 0):
                        movies_list = Movie.objects.filter(movie_genre__contains = genre)
                    else:
                        movies_list = movies_list.filter(movie_genre__contains = genre)
        else:
            movies_list = Movie.objects.filter(Q(movie_name__contains = formtext) | 
                                                Q(movie_director__contains = formtext) |
                                                Q(movie_genre__contains = formtext))
                 
        context = {'movies_list': movies_list}
        return render(request, 'movies/search.html', context)
