import datetime
from uuid import uuid4

from pydantic import BaseModel, Field


class Event(BaseModel):
    id: str = Field(default_factory=lambda: uuid4().hex)
    date: datetime.datetime

e1 = Event(date=datetime.datetime(2023, 10, 1))
print(e1.date.strftime("%d"))