#!/usr/bin/python
import json
import datetime

#read json file data and deserialize
data = []
with open('/tmp/imdb.json', 'r') as f_json:
    data = json.load(f_json)

new_data = []
for index,element in enumerate(data):
    new_data.append({"fields": {"movie_name": str(element["name"]),
                                "movie_director": str(element["director"]),
                                "movie_99popularity": str(element["99popularity"]),
                                "movie_imdbscore": str(element["imdb_score"]),
                                "entry_date": datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%SZ"),
                                "movie_genre": ",".join(element["genre"])},
                     "model": "movies.movie",
                     "pk": index+1 })

#write serialized json data to fixture file
with open('/tmp/imdb_fixture.json','w') as f_fixture:
    json.dump(new_data,f_fixture,indent = 2)
