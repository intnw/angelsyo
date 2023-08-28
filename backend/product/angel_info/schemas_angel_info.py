from pydantic import BaseModel
from typing import List, Union

class AngelInfoBare(BaseModel):
    pass

class AngelInfoBase(BaseModel):
    id: int
    key: str
    value: str
    
    class Config:
        orm_mode = True

from pydantic import BaseModel
from typing import List, Union

class AngelInfoCreate(AngelInfoBare):
    key: str
    value: str

    class Config:
        orm_mode = True

class AngelInfoOut(AngelInfoBase):
    pass

# class AllInterests(BaseModel):
#     category: str
#     value: List[AngelInfoBase]

# class CategoryInterestSuggestion(AngelInfotBare):
#     key: str
#     value: str

#     class Config:
#         orm_mode = True