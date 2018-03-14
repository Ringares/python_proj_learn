"""
https://docs.mongodb.com/getting-started/python/update/
"""
import pymongo

client = pymongo.MongoClient("localhost", 27017)

# 库
testdb = client.test

# 集合(表)
testdb.mytag

result = testdb.mytag.insert_one(
    {
        "id": 1001,
        "name": "aab"
    }
)

for doc in testdb.mytag.find():
    print(doc)

"""
Query

{ <field1>: <value1>, <field2>: <value2>, ... }
cursor = db.restaurants.find({"grades.score": {"$gt": 30}})
cursor = db.restaurants.find({"grades.score": {"$lt": 10}})

and
cursor = db.restaurants.find({"cuisine": "Italian", "address.zipcode": "10075"})

or
cursor = db.restaurants.find(
    {"$or": [{"cuisine": "Italian"}, {"address.zipcode": "10075"}]})

sort
cursor = db.restaurants.find().sort([
    ("borough", pymongo.ASCENDING),
    ("address.zipcode", pymongo.ASCENDING)
])

"""
for doc in testdb.mytag.find({"name": "aab"}):
    print(doc)
