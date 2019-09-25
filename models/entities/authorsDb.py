from models.entities.checkCollection import checkCollection
from models.authors import Authors

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
        author = self.collection.find_one({"_id": authorId})
        if author:
            return Authors(
                userName=author["userName"],
                firstName=author["firstName"],
                lastName=author["lastName"],
                _id=authorId
            )
        return None
