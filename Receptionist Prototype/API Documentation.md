# AI Receptionist Prototype API Documentation

Version: 1.0.0

---

# Overview

This document describes all REST APIs and WebSocket endpoints exposed by the AI Receptionist Prototype.

The backend is built using **FastAPI** and currently supports:

- Desktop Voice Prototype
- Chat Testing Endpoint
- Twilio Incoming Call Webhook
- Twilio Media Stream WebSocket

---

# Base URL

Local

```
http://127.0.0.1:8000
```

Development (ngrok)

```
https://<your-ngrok-url>
```

---

# API List

| Method | Endpoint | Purpose |
|---------|----------|---------|
| GET | / | Health Check |
| POST | /webhook | Complete AI Receptionist Pipeline |
| POST | /chat | Test LLM using text |
| POST | /incoming-call | Twilio Incoming Call Webhook |
| WS | /media-stream | Twilio Media Stream |

---

# 1. Health Check

## Endpoint

```
GET /
```

## Purpose

Verify that the backend server is running.

---

## Response

```json
{
    "message": "AI Receptionist Prototype Running"
}
```

---

# 2. Webhook Endpoint

## Endpoint

```
POST /webhook
```

## Purpose

Runs the complete AI Receptionist pipeline using microphone input.

Pipeline

```
Microphone

↓

Audio Recorder

↓

Whisper STT

↓

Conversation Manager

↓

LLM

↓

Piper TTS

↓

JSON Response
```

---

## Response

```json
{
    "status": "success",
    "transcript": "...",
    "response": "..."
}
```

---

# Internal Workflow

1. Record microphone audio
2. Save audio
3. Whisper transcription
4. Store conversation
5. Generate AI response
6. Convert response into speech
7. Return transcript and response

---

# 3. Chat Endpoint

## Endpoint

```
POST /chat
```

---

## Purpose

Testing endpoint.

Allows direct interaction with the LLM without requiring:

- Microphone
- Whisper
- Piper
- Twilio

Useful for

- Prompt Testing
- Frontend Development
- Backend Testing

---

## Request

```json
{
    "message":"Book my appointment tomorrow."
}
```

---

## Response

```json
{
    "response":"Certainly. What time would you prefer?"
}
```

---

# Internal Workflow

```
User Message

↓

Conversation Manager

↓

LLM

↓

Return Response
```

---

# 4. Incoming Call Endpoint

## Endpoint

```
POST /incoming-call
```

---

## Purpose

Entry point for Twilio Incoming Calls.

Twilio sends an HTTP POST request whenever an incoming call is received.

The endpoint returns TwiML instructing Twilio to establish a Media Stream.

---

## Twilio Flow

```
Patient

↓

Twilio Number

↓

POST /incoming-call

↓

Return TwiML

↓

Twilio opens

↓

WebSocket /media-stream
```

---

## Response

Content-Type

```
text/xml
```

Example

```xml
<Response>
    <Connect>
        <Stream url="wss://<ngrok-url>/media-stream"/>
    </Connect>
</Response>
```

---

# 5. Media Stream Endpoint

## Endpoint

```
WS /media-stream
```

---

## Purpose

Receives Twilio Media Stream events over WebSocket.

Current implementation provides the integration skeleton required for future real-time voice communication.

---

# Current Events Supported

## connected

Purpose

Indicates successful WebSocket connection.

Example

```json
{
    "event":"connected"
}
```

---

## start

Purpose

Triggered when Twilio starts streaming audio.

Example

```json
{
    "event":"start",
    "start":{
        "streamSid":"...",
        "callSid":"..."
    }
}
```

Stored Information

- Stream SID
- Call SID

---

## media

Purpose

Contains real-time audio payload.

Example

```json
{
    "event":"media",
    "media":{
        "payload":"Base64 Audio"
    }
}
```

Current Status

Payload is received and logged.

Future Processing

```
Base64

↓

μ-law Decode

↓

PCM Audio

↓

Whisper STT

↓

Conversation Manager

↓

LLM

↓

Piper

↓

Twilio Audio Stream
```

---

## stop

Purpose

Indicates call termination.

Example

```json
{
    "event":"stop"
}
```

Current Action

- Close WebSocket
- Cleanup Resources

---

# Route Responsibilities

---

## routes/webhook.py

Purpose

Desktop AI Receptionist endpoint.

Responsibilities

- Record microphone
- Whisper transcription
- Conversation management
- LLM response
- Piper speech
- JSON response

---

## routes/chat.py

Purpose

Testing endpoint.

Responsibilities

- Receive text
- Generate AI response
- Return JSON

---

## routes/incoming_call.py

Purpose

Twilio webhook.

Responsibilities

- Accept incoming call
- Return TwiML
- Connect Media Stream

---

## routes/media_stream.py

Purpose

Twilio WebSocket endpoint.

Responsibilities

- Accept WebSocket
- Receive Twilio events
- Handle

    - connected

    - start

    - media

    - stop

Future Responsibilities

- Audio Decoding
- Whisper Integration
- LLM Integration
- Piper Integration
- Stream synthesized audio back

---

# API Status

| Endpoint | Status |
|-----------|--------|
| GET / | Complete |
| POST /webhook | Complete |
| POST /chat | Complete |
| POST /incoming-call | Complete |
| WS /media-stream | Skeleton Ready |

---

# Pending Work

Twilio Integration

- Decode Base64 payload

- μ-law → PCM conversion

- Whisper STT

- Conversation Context

- LLM Response

- Piper TTS

- Stream generated audio back to Twilio

---

# Running the API

Start FastAPI

```bash
uvicorn app:app --reload
```

Swagger

```
http://127.0.0.1:8000/docs
```

---

# Public Testing

Expose local server

```bash
ngrok http 8000
```

Example

```
https://abcd1234.ngrok-free.app
```

Incoming Call

```
POST

https://abcd1234.ngrok-free.app/incoming-call
```

Media Stream

```
wss://abcd1234.ngrok-free.app/media-stream
```

---

# Notes

Current implementation is intended as a modular prototype.

The architecture has been designed so that future integrations (Twilio Media Streams, appointment booking, PostgreSQL, calendars, etc.) can be added without major structural changes.

Current AI Pipeline

```
Speech

↓

Whisper

↓

Conversation Manager

↓

LLM

↓

Piper

↓

Speech
```

Future Twilio Pipeline

```
Phone Call

↓

Twilio

↓

Incoming Call

↓

Media Stream

↓

Whisper

↓

Conversation

↓

LLM

↓

Piper

↓

Twilio

↓

Patient
```