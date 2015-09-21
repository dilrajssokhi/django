# django-urlShortner
API is built using Python 2.7.8 -- Django 1.8.3 -- SQLite 3.2

Django app for URL Shortening: localhost:8000/urlShortner/

r'^urlShortener/' URLconf is added in mysite/urls.py which directs all '/urlShortner/' API calls to urlShortner/urls.py

URL provided is shortened into BASE62 format with encoding consiting of [a-zA-Z0-9]. The URL fed is stored in SQLite database with unique id. This autoincrementing integer id is used for conversion from BASE10 to BASE62 in getshorturl() provided in urlShortener/views.py.

If shortened URL is fed to the service, then API checks db for the short-urls like a lookup table and provides full-url back. Same goes for already processed full-urls, providing already preocessed short-urls. 

You can access full-urls by clicking on the link provided after looking up short-url in db. externalURL in urlShortner/views.py loads the content of the full-url using requests and renders the webpage at urlShortener/templates/urlShortener/externalURL.html

You can sync the db using the models.py and migration files in urlShortner/migrations/ using:

python manage.py migrate

Django's admin functionality can be used by logging on as admin on localhost:8000/admin/ and manageing full URLs and their subsequent short-URLs from URL shortners on Site administration page.
