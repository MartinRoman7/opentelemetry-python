from fastapi import FastAPI

app = FastAPI()

@app.get("/message")
async def get_message():
    return {"message": "Hello, this is your message with Automatic Instrumentation using Opentelemetry!"}