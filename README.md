# django-urlShortner

Django app for URL Shortening

API is built using Python 2.7.8 -- Django 1.8.3 -- SQLite 3.2

URL provided is shortened into BASE62 format with encoding consiting of [a-zA-Z0-9]. The URL fed is stored in SQLite database with unique id. This autoincrementing integer id is used for conversion from BASE10 to BASE62 in getshortURL() provided in urlShortener/views.py. If shortened URL is fed to the service, then API checks db for the short-urls like a lookup table and provides full-url back. Same goes for already processed full-urls. You can access full-urls by clicking on the link provided after looking up short-url in db. externalURL in urlShortner/views.py loads the content of the full-url using imported module requests and renders the webpage from urlShortener/templates/urlShortener/externalURL.html

mysite/urls.py specifies the url r'/urlShortener/' which calls the API mentioned in urlShortner/urls.py

You can sync the db using the models and migrations in urlShortner/models.py urlShortner/migrations/..

python manage.py makemigrations

python manage.py migrate


