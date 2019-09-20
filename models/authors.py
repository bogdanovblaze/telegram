from dataclasses import dataclass


# описание БД
@dataclass
class Authors:
    userName: str
    firstName: str
    lastName: str
    _id: int
