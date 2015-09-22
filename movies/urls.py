from django.conf.urls import url
from . import views

urlpatterns = [
    # ex: /movies/
    url(r'^$', views.index, name='index'),
    # ex: /movies/5/
    url(r'^(?P<movie_id>[0-9]+)/$', views.detail, name='detail'),
    # ex: /movies/search/
    url(r'^search/$', views.search, name='search'),
]

