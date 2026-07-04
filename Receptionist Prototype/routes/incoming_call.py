from fastapi import APIRouter
from fastapi.responses import Response

router = APIRouter()

@router.post("/incoming-call")
async def incoming_call():
    twiml = """
    <?xml version="1.0" encoding="UTF-8"?>
    <Response>
        <Connect>
            <Stream url="wss://batboy-unloving-tattered.ngrok-free.dev/media-stream"/>
        </Connect>
    </Response>
    """
    return Response(
        content = twiml,
        media_type = "text/xml"
    )