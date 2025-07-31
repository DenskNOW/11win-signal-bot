from sqlalchemy import Column, Integer, String, Boolean, DateTime
from datetime import datetime
from database.db import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    telegram_id = Column(String, unique=True, index=True)
    username = Column(String)
    language = Column(String)
    is_registered = Column(Boolean, default=False)
    has_deposit = Column(Boolean, default=False)
    created_at = Column(DateTime, default=datetime.utcnow)