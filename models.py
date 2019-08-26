from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()


class Review(Base):
    __tablename__ = 'review'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    emailid = Column(String)
    message = Column(String)

    def to_dict(self):
        return {"id": self.id, "name": self.name, "emailid": self.emailid, "message": self.message}
