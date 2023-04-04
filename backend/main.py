from fastapi import FastAPI
from core.config import settings

app = FastAPI(title=settings.PROJECT_NAME,version=settings.PROJECT_VERSION)

# decorator below : used to provide extra functionality to a function
# "/" refers to the home endpoint
@app.get("/") 

def hello_api() : 
    return {"msg" : "Hello API"}