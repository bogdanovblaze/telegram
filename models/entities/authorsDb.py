class AuthorsDb:
    def __init__(self, db):
        self.db = db
        self.collectionName = 'authors'
        self.collection = self.db[self.collectionName]

    # декоратор
    def checkCollection(func):
        def wrapper(self, authorId):
            if self.collectionName in self.db.list_collection_names():
                return func(self, authorId)
            else:
                return None
        return wrapper

    def add(self, element):
        # print('AuthorsDb:add()')
        self.collection.insert_one(element.__dict__)

    @checkCollection
    def getById(self, authorId):
        # print("authorsDb:getById()")
        return self.collection.find_one({"_id": authorId})
