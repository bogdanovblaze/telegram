from dataclasses import dataclass
from datetime import datetime


@dataclass
class Messages:
    channelId: int
    authorId: int
    message: str
    _id: int
    createAt: datetime = datetime.now()
