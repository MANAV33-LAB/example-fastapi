from fastapi import FastAPI

import model
from database import engine,get_db
from routers import post,user,auth,votes
from fastapi.middleware.cors import CORSMiddleware
#model.Base.metadata.create_all(bind = engine) # ye line hatana hoga when i use alembic ,bcoz alembic will create all database and yahan bas uvicorn se server activate krenge
app = FastAPI()
# List of allowed origins (frontend URLs)
origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,           # Which origins are allowed
    allow_credentials=True,          # Allow cookies/auth headers
    allow_methods=["*"],             # Allow all HTTP methods
    allow_headers=["*"],             # Allow all headers
)

#router object so split our all path operations

app.include_router(post.routers) 
app.include_router(user.routers)
app.include_router(auth.routers)
app.include_router(votes.routers)



