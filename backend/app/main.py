from fastapi import FastAPI, Request
app = FastAPI()

import logging

from enum import Enum
class Options(str, Enum):
    option_1 = "option_1"
    option_2 = "option_2"

@app.get("/")
def root():
    return {"message": "Hello World!"}

@app.get('/{option}')
def get_probe_question(option: Options):

    if option == Options.option_1:
        return {"option": option ,"question": "You chose Option 1!"}

    if option == Options.option_2:
        return {"option": option ,"question": "You chose Option 2!"}

    return {"option": option, "question": "Are you lost?"}