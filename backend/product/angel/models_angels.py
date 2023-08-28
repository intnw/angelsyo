from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import Column
import uuid

from ..database import Base

class Angel(Base):
    __tablename__ = "angel"

    id = Column(UUID(as_uuid=True), primary_key=True, 
                index=True,
                nullable=False,
                default=uuid.uuid4)