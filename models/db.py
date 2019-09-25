from __future__ import annotations
from pymongo import MongoClient

from models.entities.authorsDb import AuthorsDb
from models.entities.messagesDb import MessagesDb
from models.entities.channelsDb import ChannelsDb

import logging
logging.basicConfig(filename="sample.log", filemode="w", level=logging.DEBUG)


class EntityMeta(type):
    _instance: Optional[Entity] = None

    def __call__(self) -> Entity:
        if self._instance is None:
            self._instance = super().__call__()
        return self._instance


class Entity(metaclass=EntityMeta):
    def __init__(self):
        # self.client = None
        self.db = None
        self._authors = None
        self._messages = None
        self._channels = None

        self.connectDb()

    def connectDb(self):
        client = MongoClient(
            "mongodb+srv://blaze_telegram:zCe-aqC-Ps3-234@telegram-srtxa.mongodb.net/test?retryWrites=true&w=majority"
        )

        self.db = client.Telegram
        # print(self.db)
        logging.info('mongo : [ connected ]')

    @property
    def authors(self):
        if self._authors is None:
            self._authors = AuthorsDb(self.db)
            logging.info('Entyty : AuthorsDb: [ Create object ]')
        return self._authors

    @property
    def messages(self):
        if self._messages is None:
            self._messages = MessagesDb(self.db['message'])
            logging.info('Entyty : MessagesDb: [ Create object ]')
        return self._messages

    @property
    def channels(self):
        if self._channels is None:
            self._channels = ChannelsDb(self.db)
            logging.info('Entyty : ChannelsDb: [ Create object ]')
        return self._channels
