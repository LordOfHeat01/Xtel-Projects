# this file is made to do only three things
# create the fastapi application
# register the webhook route
# add a root endpoint for health check

from fastapi import FastAPI
from routes.webhook import router as webhook_router
from routes.media_stream import router as media_stream_router
from routes.incoming_call import router as incoming_call_router
from routes.chat import router as chat_router

app = FastAPI(
    title="Receptionist Prototype",
    description="Voice-base AI Receptionist API built using FASTAPI,Whisper,Hugging Face LLM, and Piper TTS",
    version="1.0.0",
)

#Register routes
app.include_router(webhook_router)
app.include_router(media_stream_router)
app.include_router(incoming_call_router)
app.include_router(chat_router)

@app.get("/")
def home():
    """
    Health check endpoint.
    
    """
    return {
        "message":"AI Receptionist Prototype is running successfully.",
        "status":"OK"
    }


