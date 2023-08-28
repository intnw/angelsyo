from sqlalchemy.orm import Session
from sqlalchemy import update
from sqlalchemy import and_, or_

from typing import List

from .models_angel_info import AngelInfo
from .schemas_angel_info import AngelInfoBase

from sqlalchemy import func

def get_angel_infos(db: Session):
    return db.query(AngelInfo).all()

def get_angel_info(db: Session, angel_id: str):
    res = db.query(AngelInfo).filter(AngelInfo.angel_id == angel_id).all()
    return res

def search_angel_info(db: Session, key: str, value: str):
    res = db.query(AngelInfo) \
        .filter(AngelInfo.key == key, AngelInfo.value == value).first()
    return res

def search_angel_by_keyword(db, search_string):
    all_angels = db.query(AngelInfo) \
        .filter(func.lower(AngelInfo.value).contains(search_string.lower())) \
        .distinct(AngelInfo.angel_id) \
        .all()

    return [str(a.angel_id) for a in all_angels]

def search_angel_by_keywords(db, search_string):
    keywords = [kw.strip().lower() for kw in search_string.split()]
    
    angel_sets = []
    for kw in keywords:
        angels = db.query(AngelInfo.angel_id) \
        .filter(func.lower(AngelInfo.value).contains(kw)) \
        .distinct(AngelInfo.angel_id) \
        .all()
        angel_sets.append(angels)

    all_angels = set(angel_sets[0])
    for angels in angel_sets[1:]:
        all_angels &= set(angels)

    return [str(a.angel_id) for a in all_angels]

def search_angel_by_keywords1(db, search_string):
    keywords = [kw.strip().lower() for kw in search_string.split()]

    if len(keywords) == 1:
        all_angels = db.query(AngelInfo) \
            .filter(func.lower(AngelInfo.value).contains(keywords[0].lower())) \
            .distinct(AngelInfo.angel_id) \
            .all()
    elif len(keywords) == 2:
        all_angels = db.query(AngelInfo.value) \
            .filter(func.lower(AngelInfo.value).contains(keywords[0]),\
                    func.lower(AngelInfo.value).contains(keywords[1])) \
            .distinct(AngelInfo.angel_id) \
            .all()
        
    elif len(keywords) == 3:
        all_angels = db.query(AngelInfo) \
            .filter(func.lower(AngelInfo.value).contains(keywords[0].lower()),\
                    func.lower(AngelInfo.value).contains(keywords[1].lower()), \
                    func.lower(AngelInfo.value).contains(keywords[2].lower())) \
            .distinct(AngelInfo.angel_id) \
            .all()
        
    elif len(keywords) == 4:
        all_angels = db.query(AngelInfo) \
            .filter(func.lower(AngelInfo.value).contains(keywords[0].lower()),\
                    func.lower(AngelInfo.value).contains(keywords[1].lower()), \
                    func.lower(AngelInfo.value).contains(keywords[2].lower()), \
                    func.lower(AngelInfo.value).contains(keywords[3].lower())) \
            .distinct(AngelInfo.angel_id) \
            .all()
        
    elif len(keywords) == 5:
        all_angels = db.query(AngelInfo) \
            .filter(func.lower(AngelInfo.value).contains(keywords[0].lower()),\
                    func.lower(AngelInfo.value).contains(keywords[1].lower()), \
                    func.lower(AngelInfo.value).contains(keywords[2].lower()), \
                    func.lower(AngelInfo.value).contains(keywords[3].lower()), \
                    func.lower(AngelInfo.value).contains(keywords[4].lower())) \
            .distinct(AngelInfo.angel_id) \
            .all()
    else: return []

    return [str(a.angel_id) for a in all_angels]

def get_angel_search_suggestions(db, search_string):
    all_angels = db.query(AngelInfo) \
        .filter(func.lower(AngelInfo.value).contains(search_string.lower())) \
        .distinct(AngelInfo.value) \
        .limit(10)

    return [a.value for a in all_angels]

def create_angel_info(db: Session, angel_info: AngelInfoBase, angel_id: int):
    #check if already exist
    res = db.query(AngelInfo).filter(AngelInfo.angel_id == angel_id, AngelInfo.key == angel_info.key).first()

    if res: 
        raise Exception("not allowed")
    
    angel = AngelInfo()
    angel.key=angel_info.key
    angel.value=angel_info.value
    angel.angel_id = angel_id
    db.add(angel)
        
    db.commit()
    db.refresh(angel)

    return angel

def create_angel_info_batch(db: Session, angel_infos: List[AngelInfoBase], angel_id: str):
    #check if already exist by unique linkedin url
    res = search_angel_info(db, "linkedin", angel_infos[10].value)
    if res:
        print(angel_infos[11].value, angel_infos[9].value, angel_infos[10].value, angel_infos[0].value)
        raise Exception("not allowed duplicate users")

    for angel_info in angel_infos:
        res = db.query(AngelInfo).filter(AngelInfo.angel_id == angel_id, AngelInfo.key == angel_info.key).first()

        if res: 
            raise Exception("not allowed duplicate keys for the same user")
        
        angel = AngelInfo()
        angel.key=angel_info.key
        angel.value=angel_info.value
        angel.angel_id = angel_id
        db.add(angel)
            
        db.commit()
        db.refresh(angel)

    return get_angel_info(db, angel_id)

# def update_profile_more1(db: Session, updated_profile_more1: schemas.ProfileMore1BaseBatch, user_id: int):
#     updated_pr_d = updated_profile_more1.dict()
    
#     for key in PROFILE_MORE1_CONFIG_LST:
#         res = db.execute(
#             update(models.ProfileMore1)
#             .where(models.ProfileMore1.user_id == user_id)
#             .where(models.ProfileMore1.key == key)
#             .values({"value": updated_pr_d[key]})
#         )

#         #For nosql new-field added post it if new
#         if(res.rowcount == 0):
#             pr = models.ProfileMore1()
#             pr.key=key
#             pr.value=updated_pr_d[key]
#             pr.user_id = user_id
#             db.add(pr)

#     db.flush()
#     db.commit()
#     return updated_profile_more1

# def delete_profile_more1(db: Session, user_id: int):
#     profile_more1s = db.query(models.ProfileMore1).filter(models.ProfileMore1.user_id==user_id).all()

    # for profile_more1 in profile_more1s:
    #     db.delete(profile_more1)
    #     db.commit()