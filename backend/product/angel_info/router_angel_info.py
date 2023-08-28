from fastapi import APIRouter
from fastapi import Depends, status, HTTPException
from fastapi.responses import JSONResponse

from typing import List

from . import schemas_angel_info
from . import service_angel_info

from ..database import get_db

from sqlalchemy.orm import Session

from . import nosql_config

router = APIRouter(
prefix='/angel-info',
tags = ['angel-info']
)

# def k-v-pairs to just dict
# TODO Ofcourse sql to nosql will require some extra operations like below; but still need to see this in a different way
#or distribute this to client
# def nosql_to_sql_resp(lst):
#     new_d = {}

#     for cat in nosql_config.ANGEL_CONFIG_LST:
#         new_d[cat] = []
    
#     for intr in lst:
#         if intr.key in new_d:
#             new_d[intr.key].append({"id": intr.id, "value": intr.value})
#         else:
#             new_d[intr.key] = [{"id": intr.id, "value": intr.value}]

#     #sort by id desc
#     new_new_d = {}
#     for cat in nosql_config.ANGEL_CONFIG_LST:
#         if cat in new_d:
#             new_new_d[cat] = sorted(new_d[cat], key=lambda x: x["id"], reverse = True)
    
#     # print(new_new_d)
#     return new_new_d

@router.get("/all",)
async def get_all_angel_infos(db: Session = Depends(get_db)):
    angel_infos = service_angel_info.get_angel_infos(db)
    if not angel_infos:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Not found")
    return angel_infos

@router.get("",)
async def get_angel_info(angel_id: str, db: Session = Depends(get_db)):
    try:
        angel_infos = service_angel_info.get_angel_info(db, angel_id)
        
        if not angel_infos:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Not found")
        return angel_infos#nosql_to_sql_resp(angel_infos)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail="Invalid data")
    
@router.get("/suggestions",)
async def get_angel_search_suggestions(query: str, db: Session = Depends(get_db)):
    try:
        suggestions = service_angel_info.get_angel_search_suggestions(db, query)
        
        if not suggestions:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Not found")
        return suggestions#nosql_to_sql_resp(angel_infos)
    except Exception as e:
        print(e)
        raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail="Invalid data")

@router.post("", response_model=schemas_angel_info.AngelInfoCreate, status_code=status.HTTP_201_CREATED)
async def create_angel_info(angel_id: str, angel_info: schemas_angel_info.AngelInfoCreate, db: Session = Depends(get_db)):
    try:
        return service_angel_info.create_angel_info(db, angel_info, angel_id)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail="Invalid data")
    
# @router.put("", response_model=schemas.InterestBase)
# async def update_interest(updated_interest: schemas.InterestBaseUpdate,
#                         current_user: user_schema.User = Depends(auth.get_current_active_user),
#                         db: Session = Depends(get_db)):
#     # intrs = service.get_interests(db, current_user.id)
#     # if not intrs:
#     #     raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail="Invalid data")
#     # return service.update_interest(db, updated_interest, current_user.id)
#     try:
#         return service.update_interest(db, updated_interest, current_user.id)
#     except Exception as e:
#         raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail="Invalid data")
    
# @router.delete("", status_code=status.HTTP_200_OK)
# async def delete_interest(interest: schemas.InterestBaseDelete, current_user: user_schema.User = Depends(auth.get_current_active_user),
#                           db: Session = Depends(get_db)):
#     try:
#         service.delete_interest(db, interest)
#         return {}
#     except Exception as e:
#         raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail="Invalid data")