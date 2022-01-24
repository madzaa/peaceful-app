from app import db


class ItemsModel(db.Model):
    """
    Defined the items model
    """

    __tablename__ = "blacklisted"
    id = db.Column(db.Integer, primary_key=True)
    path = db.Column("path", db.String)
    ip = db.Column("ip", db.String)
    date = db.Column("date", db.String)

    def __init__(self,   path, ip, date):
        self.path = path
        self.ip = ip
        self.date = date

    def __repr__(self):
        return f"<Item {self.id}, {self.path}, {self.ip}, {self.date}>"