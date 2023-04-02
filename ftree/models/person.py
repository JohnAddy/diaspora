from ftree.database import Base
import sqlalchemy as sa


class Member(Base):
    __tablename__ = 'members'
    id = sa.Column(sa.Integer, primary_key=True)
    first_name = sa.Column(sa.String)
    last_name = sa.Column(sa.String)
    image_path = sa.Column(sa.String)

    def __init__(self, first_name=None, last_name=None, image_path=None):
        self.first_name = first_name
        self.last_name = last_name
        self.image_path = image_path

    def __repr__(self):
        return f'<Member {self.first_name!r}>'