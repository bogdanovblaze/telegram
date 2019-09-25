from telethon.tl.functions.users import GetFullUserRequest
from models.authors import Authors
import logging
module_logger = logging.getLogger("app.participants")
logger = logging.getLogger("app.participants")

class Participants:

    def __init__(self, db, client):
        self.db = db
        self.client = client
        self.list = []

    def find(self, authorId) -> bool:

        logger.info('find()')
        for author in self.list:
            if author._id == authorId:
                return True
        return False

    async def check(self, authorId) -> bool:
        logger.info('check()')
        if not self.find(authorId):
            logger.info('check():if(find[false])')
            author = self.db.authors.getById(authorId)
            if author:

                self.list.append(author)
                logger.info('check():if(find[false]):if(author[true]) author add list')
                return True
            else:
                # logger.info('check():if(find[false]):else(author[false])')
                res = await self.client(GetFullUserRequest(authorId))
                # logger.info('check():if(find[false]):else(author[false]) res = ', res)
                user = res.user

                author = Authors(
                    userName=user.username,
                    firstName=user.first_name,
                    lastName=user.last_name,
                    _id=authorId
                )
                # print(f"Автор '{author.firstName} {author.lastName} ({author.userName})' добавлен в БД")

                logger.info("check():if(find[false]):else(author[false]) author")
                self.db.authors.add(author)
                self.list.append(author)
                return True
        else:
            logger.info('check():if(find[true])')
            return True
