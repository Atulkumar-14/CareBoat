
from fastapi import FastAPI
from fastapi import Query
from typing import List,Annotated
from utility.predict import predict
from pydantic import BaseModel
from enum import Enum
from typing import List

class Symptoms(str,Enum):
    anxiety_nervousness='anxiety and nervousness'
    depression='depression'
    dizziness='dizziness'
    insomnia='insomnia'	


class reqSymptoms(BaseModel):
    values: List[Symptoms]

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/predicts")
async def predicts(q: Annotated[reqSymptoms ,Query()]=None):
    if q is None:
        return {"message": "No predictions provided"}
    return predict(q)
    
# @app.get("/predicts")
# async def predicts(query: list[str] | None = Query(default=None)):
#     return {"message": f"Predictions for {query}"}