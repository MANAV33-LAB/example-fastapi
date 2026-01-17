from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import post, user, auth, votes
import app.model
from app.database import engine

app = FastAPI()

# Create all tables (UNCOMMENT THIS LINE FOR FIRST DEPLOYMENT)
app.model.Base.metadata.create_all(bind=engine)

origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(post.routers) 
app.include_router(user.routers)
app.include_router(auth.routers)
app.include_router(votes.routers)