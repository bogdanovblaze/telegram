class MessagesDb:
    def __init__(self, collection):
        # print('\tMessagesDb : __init__')
        self.collection = collection

    def add(self, element):
        # print('\tMessagesDb : add()', element, end='\n')
        self.collection.insert_one(element.__dict__)
        print(f"{element.createAt} | Сообщение '{element.message}' добавленно в БД")
