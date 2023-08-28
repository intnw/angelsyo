from fastapi import APIRouter
from fastapi import Depends, status, HTTPException

from ..angel_info.schemas_angel_info import AngelInfoCreate

from typing import List

from .schemas_angel import AngelOut, AngelCreate
from . import service_angel

import json

from ..database import get_db

from sqlalchemy.orm import Session

router = APIRouter(
prefix='/angel',
tags = ['angel']
)

@router.get("/all")
async def get_angels(db: Session = Depends(get_db)):
    angels = service_angel.get_angels(db)
    if not angels:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Not found")
    return angels

@router.get("")
async def get_angels_info(num: int, db: Session = Depends(get_db)):
    angels_infos = service_angel.get_angels_info(db, num)
    if not angels_infos:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Not found")
    return angels_infos

@router.get("/search")
async def search_angels_by_keyword(keyword: str, db: Session = Depends(get_db)):
    angels_infos = service_angel.search_angels_by_keyword(db, keyword)
    if not angels_infos:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Not found")
    return angels_infos

@router.get("/search/multikw")
async def search_angels_by_keywords(keywords: str, pagenum: int, db: Session = Depends(get_db)):
    angels_infos = service_angel.search_angels_by_keywords(db, keywords, pagenum)
    if not angels_infos:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Not found")
    return angels_infos

#TODO TESTING Search/browse profile
@router.get("/{angel_id}")
async def get_angel(angel_id, db: Session = Depends(get_db)):
    angel = service_angel.get_angel(db, angel_id)
    if not angel:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Not found")
    return angel

@router.post("", status_code=status.HTTP_201_CREATED)
async def create_angel(db: Session = Depends(get_db)):
    try:
        return service_angel.create_angel_blank(db)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail="Invalid data")
    
@router.post("/batch", status_code=status.HTTP_201_CREATED)
async def create_angel(angel_infos: List[AngelInfoCreate], db: Session = Depends(get_db)):
    try:
        return service_angel.create_angel_with_info(db, angel_infos)
    except Exception as e:
        print("---", e)
        raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail="Invalid data")

# @router.put("", response_model=schemas.ProfileUpdate)
# async def update_profile(updated_profile: schemas.ProfileUpdate,
#                         current_user: user_schema.User = Depends(auth.get_current_active_user),
#                         db: Session = Depends(get_db)):
#     profile = service.get_profile(db, current_user.id)
#     if not profile:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Not found")
#     return service.update_profile(db, updated_profile, current_user.id)

# @router.delete("", status_code=status.HTTP_204_NO_CONTENT)
# async def delete_profile(current_user: user_schema.User = Depends(auth.get_current_active_user), db: Session = Depends(get_db)):
#     service.delete_profile(db, current_user.id)
