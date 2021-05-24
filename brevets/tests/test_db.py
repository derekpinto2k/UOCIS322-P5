import os
from pymongo import MongoClient


client = MongoClient('mongodb://' + os.environ['MONGODB_HOSTNAME'], 27017)
db = client.brevetsdb

def test_db_insert_and_retrieve():
    times_insert = [{'open': '2021-01-01T05:53', 'close': '2021-01-01T13:20'},
                    {'open': '2021-01-02T03:44', 'close': '2021-01-03T13:53'}]

    print(times_insert)
    db.times.drop()
    for item in times_insert:
        db.times_insert.insert_one(item)

    times_retrieve = list(db.times_insert.find())
    assert times_retrieve
