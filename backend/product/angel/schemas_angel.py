from typing import List, Union

from pydantic import BaseModel, EmailStr, Field, validator
from sqlalchemy.dialects.postgresql import UUID

class AngelBase(BaseModel):
    pass

class AngelCreate(AngelBase):
    pass

class AngelOut(AngelBase):
    id: str

    class Config:
        orm_mode = True