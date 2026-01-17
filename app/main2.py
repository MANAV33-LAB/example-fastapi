from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# Simple imports
from routers import post, user, auth, votes

app = FastAPI()

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