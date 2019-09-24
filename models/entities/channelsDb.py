from models.entities.checkCollection import checkCollection


class ChannelsDb:
    def __init__(self, db):
        self.db = db
        self.collectionName = 'channels'
        self.collection = self.db[self.collectionName]

    @checkCollection
    def add(self, object):
        if self.collection.find_one({"_id": object._id}) is None:
            self.collection.insert_one(object.__dict__)
            print(f"Канал '{object.title}' добавлен в БД")
        else:
            print(f"Канал '{object.title}' уже есть в БД")
