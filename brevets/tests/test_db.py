import os
from pymongo import MongoClient
import arrow

client = MongoClient('mongodb://' + os.environ['MONGODB_HOSTNAME'], 27017)
db = client.brevetsdb

def test_db_insert_and_retrieve():
    times_insert = {'open': arrow.get(2021).format('YYYY-MM-DDTHH:mm'),
                    'close': arrow.get(2022).format('YYYY-MM-DDTHH:mm')}
    db.times.drop()
    for item in times_insert:
        db.times_insert.insert_one(item)

    times_retrieve = list(db.times_insert.find())
    assert times_retrieve

