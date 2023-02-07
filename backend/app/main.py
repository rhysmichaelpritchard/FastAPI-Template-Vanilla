from fastapi import FastAPI
from enum import Enum

app = FastAPI()

class ModelName(str, Enum):
    likes = "likes"
    dislikes = "dislikes"

@app.get("/")
def root():
    return {"message": "Hello World"}

@app.get('/probe/{question}')
def get_probe_question(question: ModelName):
    if question == ModelName.likes:
        return {"model_name": question ,"question": "What do you like about your new car?"}
    if question == ModelName.dislikes:
        return {"model_name": question ,"question": "What do you dislike about your new car?"}
    return {"model_name": question, "question": "This should not be possible?"}