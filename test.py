from models.db import Entity
from models.channels import Channels


db = Entity()
db.channels.add(
            Channels(
                "Двач",
                "https://t.me/twochannel",
                1003073997,
            )
        )





