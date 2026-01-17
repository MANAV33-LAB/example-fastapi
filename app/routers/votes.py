from fastapi import FastAPI, Response, status, HTTPException, Depends, APIRouter
from sqlalchemy.orm import Session

# Try relative imports first (for Render), fallback to absolute (for local)
try:
    from .. import schemas
    from .. import oauth
    from .. import model
    from .. import database
except ImportError:
    import schemas
    import oauth
    import model
    import database

routers = APIRouter(
    prefix="/votes",
    tags=["VOTES"]
)

@routers.post("/", status_code=status.HTTP_201_CREATED)
def vote(vote: schemas.Votes, db: Session = Depends(database.get_db), current_user: int = Depends(oauth.get_current_user)):
    check = db.query(model.Post).filter(model.Post.id == vote.post_id).first()
    if not check:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="post not exist")
    
    vote_query = db.query(model.votes).filter(model.votes.post_id == vote.post_id, model.votes.user_id == current_user.id)
    found = vote_query.first()
    if (vote.dir == 1):
        if found:
            raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="it already voted")
        save = model.votes(post_id = vote.post_id, user_id = current_user.id)
        db.add(save)
        db.commit()
        return "success added"
    else:
        if not found:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="not found")
        
        vote_query.delete(synchronize_session=False)
        db.commit()
        return "deleted successfully"