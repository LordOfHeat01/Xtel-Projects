from fastapi import APIRouter
from pydantic import BaseModel

from conversation import ConversationManager
from services.llm_service import LLMService

router = APIRouter()

conversation = ConversationManager()
llm = LLMService()


class ChatRequest(BaseModel):
    message: str


@router.post("/chat")
def chat(request: ChatRequest):

    conversation.add_user_message(request.message)

    reply = llm.generate_response(
        conversation.get_messages()
    )

    conversation.add_assistant_message(reply)

    return {
        "response": reply
    }