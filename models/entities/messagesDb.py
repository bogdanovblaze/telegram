import pymongo
import logging
logging.basicConfig(filename="sample.log", level=logging.INFO)


class MessagesDb:
    def __init__(self, collection):
        # print('\tMessagesDb : __init__')
        self.collection = collection

    def add(self, element):
        # print('\tMessagesDb : add()', element, end='\n')
        try:
            self.collection.insert_one(element.__dict__)
        except pymongo.errors.DuplicateKeyError:
            print(f"Пользователь {element.id} уже есть в БД")
            logging.info("except pymongo.errors.DuplicateKeyError")

        print(f"{element.createAt} | Сообщение '{element.message}' добавленно в БД")
