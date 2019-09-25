from telethon import TelegramClient, sync, events, functions

import configparser
import os
import sys
import argparse
from datetime import datetime

from models.messages import Messages
from models.channels import Channels
from models.db import Entity
from lib.participants import Participants

import logging
logging.basicConfig(filename="sample.log", filemode="w", level=logging.DEBUG)


def createParser():
    parser = argparse.ArgumentParser()
    parser.add_argument('-ns', '--name_session', type=str, required=True)
    parser.add_argument('-ai', '--api_id', type=int, required=True)
    parser.add_argument('-ah', '--api_hash', type=str, required=True)
    parser.add_argument('-uc', '--url_channel', type=str, required=True)
    return parser


def main():
    parser = createParser()
    script_parameters = parser.parse_args(sys.argv[1:])
    script_parameters.name_session += ".session"

    # region config
    path = os.path.join(os.getcwd(), "config", "settings.ini")
    config = configparser.ConfigParser()
    config.read(path)
    # endregion

    # region TelegramConfig
    api_id = script_parameters.api_id
    api_hash = script_parameters.api_hash
    channel_url = script_parameters.url_channel
    # endregion

    with TelegramClient(script_parameters.name_session, api_id, api_hash) as client:
        # Переменная, необходимая для получения channel.titile
        channel = client(functions.channels.GetFullChannelRequest(channel_url))

        # Получение базы данных
        db = Entity()

        # Создание объекта участники для провеки авторов сообщений
        participants = Participants(db, client)
        logging.info("start app.py")

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
            logging.info("app.py:events.NewMessage")

            event = event.message
            check = await participants.check(event.from_id)
            # print('app.py:check = ', check)

            if check:
                logging.info("app.py:if(check[true])")
                db.messages.add(
                    Messages(
                        event.to_id.channel_id,
                        event.from_id,
                        event.message,
                        event.id,
                        datetime.now()
                    )
                )
            else:
                logging.info('app.py:if(check[false])')
                logging.info('Telegram :: Ошибка получения пользователя по Id\n')

            print("\n", "=-> "*20, "\n", sep="")

        client.run_until_disconnected()


if __name__ == '__main__':
    main()
