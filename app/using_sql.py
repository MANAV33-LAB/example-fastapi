from fastapi import FastAPI,HTTPException,status
from pydantic import BaseModel
from typing import Optional
import numpy as np
import psycopg2
import time
from psycopg2.extras import RealDictCursor
app = FastAPI()
class posti(BaseModel):
    title : str
    name : str
    boo : bool = True
while True:
    try: 
        conn = psycopg2.connect(host='localhost', database='fastapi_server', user='postgres',
        password="RJTRIXU@#143", cursor_factory = RealDictCursor)
        cursor = conn.cursor()
        print("Database connection was succesfull!")
        break
    except Exception as error:
        print ("Connecting to database failed") 
        print("Error: ", error)
        time. sleep(10)
alpha = [
    {
        
        "title": "Learning FastAPI",
        "name": "John"
        
    },
    {
        
        "title": "Building REST APIs",
        "name": "Sarah"
    },
    {
        
        "title": "Python Web Development",
        "name": "Mike"
    }
]



@app.get ("/")
async def root():
    cursor.execute(""" SELECT * FROM posts """)
    hola = cursor.fetchall()
    return {"ans": hola}


@app.post("/post")
async def create_posti(new: posti): 
    cursor.execute(""" INSERT INTO posts (name,title,boo) VALUES (%s,%s,%s) RETURNING *""",(new.name,new.title,new.boo))
    ans = cursor.fetchone()
    conn.commit()
    
    return ans

@app.get("/posts/{id}")
async def get_posts(id:int):
    for i in alpha:
        if i["id"] == id:
            return i
        
@app.delete("/posts/{id}",status_code=status.HTTP_204_NO_CONTENT)
def delt(id:int):
    mark = 0
    for i in alpha:
        if i["id"] == id:
            mark = i
            break
    if mark == 0:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="no matched id")
    else:
        alpha.remove(mark)
        return

@app.put("/posts/{id}",status_code=status.HTTP_202_ACCEPTED)
def update(id:int,post:posti):
    mark = 0
    for i in alpha:
        if i["id"] == id:
            mark = i
            break
    if mark == 0:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="not found")
    else:
        alpha.remove(mark)
        alpha.append(post.dict())
        return "updated success"
    


    
        
    