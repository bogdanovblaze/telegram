from telethon import TelegramClient, sync, events, functions

import configparser
import os

from models.messages import Messages
from models.channels import Channels
from models.db import Entity
from lib.participants import Participants

import logging
logging.basicConfig(filename="sample.log", filemode="w", level=logging.DEBUG)


def main():
    # region config
    path = os.path.join(os.getcwd(), "config", "settings.ini")
    config = configparser.ConfigParser()
    config.read(path)
    # endregion

    # region TelegramConfig
    api_id = config.get("Settings", "api_id")
    api_hash = config.get("Settings", "api_hash")
    channel_url = config.get("Settings", "channel_url")
    # endregion

    with TelegramClient('anon', api_id, api_hash) as client:
        # Переменная, необходимая для получения channel.titile
        channel = client(functions.channels.GetFullChannelRequest(channel_url))

        # Получение базы данных
        db = Entity()

        # Создание объекта участники для провеки авторов сообщений
        participants = Participants(db, client)
        print('start\n')

        db.channels.add(
            Channels(
                channel.chats[0].title,
                channel_url,
                channel.chats[0].id,
            )
        )

        # создание события, которое срабатывает при появлении нового сообщения
        @client.on(events.NewMessage(channel_url))
        async def handlerNewMessage(event):
            print('app.py:events.NewMessage')

            event = event.message
            check = await participants.check(event.from_id)
            # print('app.py:check = ', check)

            if check:
                print('app.py:if(check[true])')
                db.messages.add(
                    Messages(
                        event.to_id.channel_id,
                        event.from_id,
                        event.message,
                        event.id
                    )
                )
            else:
                print('app.py:if(check[false])')
                print('Telegram :: Ошибка получение пользователя по Id\n')

            print("\n", "=-> "*20, "\n", sep="")

        client.run_until_disconnected()


if __name__ == '__main__':
    main()
