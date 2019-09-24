class AuthorsDb:
    def __init__(self, db):
        self.db = db
        self.collection = self.getCollection(db['authors'])

    def checkCollection(self, nameCollection):
        if nameCollection in self.db.list_collection_names():
            return True
        else:
            return False

    def getCollection(self, collection):
        if not self.checkCollection(collection):
            # так как коллекция не существует до тех пор пока в ней нет документов
            # добавляю в нее документ
            self.collection.insert_one({'init': 'initialization date base'})
        return collection

    def add(self, element):
        # print('AuthorsDb:add()')
        self.collection.insert_one(element.__dict__)

    def getById(self, authorId):
        # print("authorsDb:getById()")
        return self.collection.find_one({"_id": authorId})