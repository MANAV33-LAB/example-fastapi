from fastapi import FastAPI

import model
from database import engine,get_db
from routers import post,user,auth,votes
from fastapi.middleware.cors import CORSMiddleware
model.Base.metadata.create_all(bind = engine) # ye line hatana hoga when i use alembic ,bcoz alembic will create all database and yahan bas uvicorn se server activate krenge
app = FastAPI()
# List of allowed origins (frontend URLs)
origins = [
    "http://localhost",          # Localhost without port
    "http://localhost:3000",     # React default port
    "http://localhost:5173",     # Vite default port
    "http://localhost:8080",     # Vue default port
    "http://127.0.0.1:3000",    # React with IP
    "http://127.0.0.1:5173",    # Vite with IP
    # Add your production frontend URL:
    # "https://yourfrontend.com",
    # "https://www.yourfrontend.com",
    "https://www.google.com"
]

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



