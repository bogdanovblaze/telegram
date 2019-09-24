class ChannelsDb():
    def __init__(self, db):
        self.db = db
        self.collectionName = 'cahnnels'
        self.collection = self.db[self.collectionName]

    # декоратор
    def checkCollection(func):
        def wrapper(self, object):
            if self.collectionName in self.db.list_collection_names():
                return func(self, object)
            else:
                print("ChannelsDb : checkCollection[else]")
                return None
        return wrapper

    @checkCollection
    def add(self, object):
        if self.collection.find_one({"_id": object._id}) is None:
            self.collection.insert_one(object.__dict__)
            print(f"Канал '{object.title}' добавлен в БД")
        else:
            print(f"Канал '{object.title}' уже есть в БД")
