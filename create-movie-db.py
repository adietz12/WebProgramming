import json
from mongita import MongitaClientDisk

client = MongitaClientDisk()

move_db = client.movie_db

scifi_collection = move_db.scifi_collection

scifi_collection.insert_many(classic_sci_fi_movies)

#Empty collection
scifi_collection.delete_many({})

scifi_collection.count_documents({})