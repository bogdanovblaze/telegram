from models.entities.checkCollection import checkCollection


class AuthorsDb:
    def __init__(self, db):
        self.db = db
        self.collectionName = 'authors'
        self.collection = self.db[self.collectionName]

    def add(self, element):
        # print('AuthorsDb:add()')
        self.collection.insert_one(element.__dict__)

    @checkCollection
    def getById(self, authorId):
        # print("authorsDb:getById()")
        return self.collection.find_one({"_id": authorId})
