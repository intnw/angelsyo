from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, TIMESTAMP
from sqlalchemy.orm import relationship

from sqlalchemy.dialects.postgresql import UUID
import uuid

from ..database import Base


class AngelInfo(Base):
    __tablename__ = "angelinfo"

    id = Column(Integer, primary_key=True, index=True)
    key = Column(String, nullable=False, index=True)
    value = Column(String, nullable=False, index=True)

    angel_id = Column(UUID, ForeignKey("angel.id"), unique=False)