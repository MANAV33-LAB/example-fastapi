#ye alag table hai,post is just name,means see post and user -> 2 alag table and both table have some add,delete,get and many different function
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import model
import oauth,schemas
from schemas import PostCreate,responsE
from typing import List
from fastapi import FastAPI, Response, status, HTTPException, Depends,APIRouter

from sqlalchemy.orm import Session
from sqlalchemy import func
from database import get_db
routers = APIRouter(
    tags=['POSTS'] #ye bas in our url open by /docs,toh wahan organise rahega ,means sab Posts table ka ye ,and user wale ka alag organise
)
@routers.get("/posts",response_model=List[responsE])#we can add owner related get post like we did in post,deelete and update but we like to make it simple
async def get_all(db:Session=Depends(get_db),limit:int = 10,steps:int = 0,search:str = ''):#parameters jo hamlo'?' krke batate
    posti = db.query(model.Post).filter(model.Post.title.contains(search)).limit(limit).offset(steps).all()
    return posti

@routers.post("/posts",status_code=status.HTTP_201_CREATED,response_model=responsE)
async def create_post(post:PostCreate,db:Session=Depends(get_db),curr_user:model.User = Depends(oauth.get_current_user)):#ye woh user ka like pura detail aagaya jo token demand kiya like its email and hashed password
    
    #save = model.Post(title = post.title,content = post.content,published = post.published)
    save = model.Post(owner_id = curr_user.id,**post.dict())#woh foreign key wala owner id
    db.add(save)
    db.commit()
    db.refresh(save)
    print(curr_user.email)
    return save
    #results = db.query(models.Post, func.count (models. Vote.post_id)) . join(
    #models. Vote, models.Vote.post_id == models.Post.id, isouter=True)• group_by(models.Post.id).all(),   but we need to make correct response model in schmeas,woh krlena ,ydd se
    #print (results)  -> ye haii toh get number of likes of post,by hel of "join" and "groubg_by" nand "counts"
@routers.get("/posts/{id}",response_model=responsE)
def get_post(id:int,db:Session=Depends(get_db)):
    save = db.query(model.Post).filter(model.Post.id == id).first()
    if not save:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="id with the give {}not found".format(id))
    else:
        
        return save
    
    
@routers.delete("/posts/{id}")
def delete_post(id:int,db:Session=Depends(get_db),curr_user:model.User = Depends(oauth.get_current_user)):
    save = db.query(model.Post).filter(model.Post.id == id)
    alpha = save.first()
    if not alpha:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="id with the give {}not found".format(id))
    else:
        if alpha.owner_id != curr_user.id :
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="you are not authorized")
        
        save.delete(synchronize_session=False)
        db.commit()
        return Response(status_code=status.HTTP_204_NO_CONTENT)
    



@routers.put("/posts/{id}",response_model=responsE)
def update(id:int,posti:PostCreate, db:Session=Depends(get_db),curr_user:model.User = Depends(oauth.get_current_user)):
    save = db.query(model.Post).filter(model.Post.id == id)
    alpha = save.first()
    if not alpha:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"data not found for id = {id}")
    else:
        if alpha.owner_id != curr_user.id :
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="you are not authorized")
        save.update(posti.dict(),synchronize_session=False)
        db.commit()
        return {"success":save.first()}
        
        