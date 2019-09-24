from telethon.tl.functions.users import GetFullUserRequest
from models.authors import Authors
# import pdb


class Participants:
    def __init__(self, db, client):
        self.db = db
        self.client = client
        self.list = []

    def find(self, authorId) -> bool:
        print('Participants:find()')
        for author in self.list:
            if author._id == authorId:
                return True
        return False

    async def check(self, authorId) -> bool:
        # pdb.set_trace()
        print('Participants:check()')
        if not self.find(authorId):
            print('Participants:check():if(find[false])')
            author = self.db.authors.getById(authorId)
            if author:

                self.list.append(
                    Authors(
                        userName=author.get("userName", ""),
                        firstName=author.get("firstName", ""),
                        lastName=author.get("lastName", ""),
                        _id=authorId
                    )
                )
                print(
                    'Participants:check():if(find[false]):if(author[true]) author add list ->', author)
                return True
            else:
                # print('Participants:check():if(find[false]):else(author[false])')
                res = await self.client(GetFullUserRequest(authorId))
                # print('Participants:check():if(find[false]):else(author[false]) res = ', res)
                user = res.user

                author = Authors(
                    userName=user.username,
                    firstName=user.first_name,
                    lastName=user.last_name,
                    _id=authorId
                )
                # print(f"Автор '{author.firstName} {author.lastName} ({author.userName})' добавлен в БД")

                print("Participants:check():if(find[false]):else(author[false]) author ->", author)
                self.db.authors.add(author)
                self.list.append(author)
                return True
        else:
            print('Participants:check():if(find[true])')
            return True
