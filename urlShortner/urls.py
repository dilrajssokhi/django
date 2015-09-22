from django.conf.urls import url
from . import views

urlpatterns = [
    # ex: /urlShortner/
    url(r'^$', views.index, name='index'),
    # ex: /urlShortner/<some_url>
    url(r'^(?P<external_url>.*)$', views.externalURL, name='externalURL'),
]
