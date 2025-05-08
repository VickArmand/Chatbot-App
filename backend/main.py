from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import openai
from dotenv import load_dotenv
import os

load_dotenv()
app = FastAPI()
openai.api_key = os.getenv('OPENAI_API_KEY')

class Message(BaseModel):
    message: str

@app.get("/")
def hello():
    return {"message": "Hello World"}

@app.post("/message")
def send_message(message: Message):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": message.message}]
        )
        answer = response.choices[0].message['content']
        return {"answer": answer}
    except Exception as ex:
        raise HTTPException(status_code=500, detail=str(ex))
