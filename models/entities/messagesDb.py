import pymongo
import logging
module_logger = logging.getLogger("app.messagesDb")
logger = logging.getLogger("app.messagesDb")


class MessagesDb:
    def __init__(self, collection):
        # logger.info('\tMessagesDb : __init__')
        self.collection = collection

    def add(self, element):
        # logger.info('\tMessagesDb : add()', element, end='\n')
        try:
            self.collection.insert_one(element.__dict__)
        except pymongo.errors.DuplicateKeyError:
            print(f"Пользователь {element.id} уже есть в БД")
            logger.info("except pymongo.errors.DuplicateKeyError")

        print(f"{element.createAt} | Сообщение '{element.message}' добавленно в БД")
