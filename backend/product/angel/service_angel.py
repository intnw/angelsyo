from sqlalchemy.orm import Session

from typing import List

from ..angel_info.schemas_angel_info import AngelInfoCreate

from .models_angels import Angel
from  ..angel_info.models_angel_info import AngelInfo

from ..angel_info import service_angel_info

def get_angel(db: Session, angel_id: int):
    return db.query(Angel).filter(Angel.id == angel_id).first()

def get_angels(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Angel).offset(skip).limit(limit).all()

def get_angels_info(db: Session, num: int):
    angels = db.query(Angel).offset(0).limit(num).all()

    #now for each id fetch corresponding info and return the list
    angel_infos = []
    for angel in angels:
        angel_infos.append(service_angel_info.get_angel_info(db, str(angel.id)))
    
    return angel_infos

def search_angels_by_keyword(db: Session, keyword: str):
    angels = service_angel_info.search_angel_by_keyword(db, keyword)

    #now for each id fetch corresponding info and return the list
    angel_infos = []
    for angel_id in angels:
        angel_infos.append(service_angel_info.get_angel_info(db, str(angel_id)))
    
    return angel_infos


def search_angels_by_keywords(db: Session, keywords: str, pagenum: int):
    angels = service_angel_info.search_angel_by_keywords(db, keywords)

    #now for each id fetch corresponding info and return the list
    angel_infos = []
    for angel_id in angels[(pagenum-1)*10:(pagenum)*10]:
        angel_infos.append(service_angel_info.get_angel_info(db, str(angel_id)))
    
    return {"total": len(angels), "data": angel_infos}

def create_angel_blank(db: Session):
    db_angel = Angel()
    db.add(db_angel)
    db.commit()
    db.refresh(db_angel)
    return db_angel

def create_angel_with_info(db: Session, angel_info: List[AngelInfoCreate]):
    db_angel = Angel()
    db.add(db_angel)
    db.commit()
    db.refresh(db_angel)

    #now also create corresponding nosql info
    angel_info = service_angel_info.create_angel_info_batch(db, angel_info, str(db_angel.id))
    return angel_info