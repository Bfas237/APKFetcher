from datetime import datetime, timezone, date

from pony.orm import *
from utils.db import db


class Admin(db.Entity):
    id = PrimaryKey(int, auto=False)
    first_name = Required(str)
    last_name = Optional(str)
    username = Optional(str)
    #added = Set("Scammer")
    super_admin = Optional(bool, default=False)
    created = Required(datetime, default=datetime.now)

    def __str__(self):
        s = self.first_name
        if self.last_name:
            s += " " + self.last_name

        if self.username:
            s += " (@%s)" % self.username

        return s
