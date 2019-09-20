class AuthorsDb:
    def __init__(self, collection):
        self.collection = collection

    def add(self, element):
        # print('AuthorsDb:add()')
        self.collection.insert_one(element.__dict__)

    def getById(self, authorId):
        # print("authorsDb:getById()")
        return self.collection.find_one({"_id": authorId})
