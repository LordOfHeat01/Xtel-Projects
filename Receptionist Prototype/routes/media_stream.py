from fastapi import APIRouter, WebSocket, WebSocketDisconnect
import json

router = APIRouter()


@router.websocket("/media-stream")
async def media_stream(websocket: WebSocket):

    await websocket.accept()
    print("\n========== Twilio Media Stream Connected ==========\n")

    try:
        while True:

            message = await websocket.receive_text()
            data = json.loads(message)

            event = data.get("event")

            # Connection established
            if event == "connected":
                print("Twilio Connected")

            # Call started
            elif event == "start":
                print("Call Started")

                stream_sid = data["start"].get("streamSid")
                call_sid = data["start"].get("callSid")

                print(f"Stream SID : {stream_sid}")
                print(f"Call SID   : {call_sid}")

            # Audio packet received
            elif event == "media":
                payload = data["media"].get("payload")

                print(f"Media Packet Received ({len(payload)} bytes)")

                # TODO:
                # 1. Base64 Decode
                # 2. μ-law -> PCM
                # 3. Whisper STT
                # 4. Conversation Manager
                # 5. LLM
                # 6. Piper TTS
                # 7. Send audio back to Twilio

            # Call ended
            elif event == "stop":
                print("Call Ended")
                break

            else:
                print(f"Unknown Event : {event}")

    except WebSocketDisconnect:
        print("Twilio Disconnected")

    except Exception as e:
        print(f"Error : {e}")

    finally:
        print("Media Stream Closed\n")