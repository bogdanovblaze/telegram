from pymongo import MongoClient

client = MongoClient(
    "mongodb+srv://blaze_telegram:zCe-aqC-Ps3-234@telegram-srtxa.mongodb.net/test?retryWrites=true&w=majority"
)
db = client['Telegram']
if "authors" in db.list_collection_names():
    print('in')
else:
    print('not exist')
