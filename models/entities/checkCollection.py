import logging
module_logger = logging.getLogger("app.checkCollection")
logger = logging.getLogger("app.checkCollection")


# декоратор
def checkCollection(func):
    def wrapper(*args, **kwargs):
        self = args[0]

        if self.collectionName in self.db.list_collection_names():
            return func(*args, **kwargs)
        else:
            logger.info(f'Collection "{self.collectionName}" not found')
            return None

    return wrapper