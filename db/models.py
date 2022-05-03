from sqlalchemy import Column, Integer, String, DECIMAL, UniqueConstraint
from .db import Base


class CallTouch(Base):
    __tablename__ = 'call_touch_dev'
    __table_args__ = (UniqueConstraint('call_id', name='call_id_index'),)

    id = Column(Integer, autoincrement=True, unique=True, primary_key=True)
    call_id = Column(Integer, unique=True)
    date = Column(String)
    time = Column(String)
    host = Column(String)
    client_number = Column(String)
    phone_number = Column(String)
    status = Column(String)
    uniq_target_call = Column(String)
    city = Column(String)
    source = Column(String)
    medium = Column(String)
    campaign = Column(String)
    keyword = Column(String)
    ga_client_id = Column(String)
    device = Column(String)
    os = Column(String)

