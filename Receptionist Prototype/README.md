# 🦷 AI Receptionist Prototype

A voice-based AI Receptionist built using **FastAPI**, **Whisper Speech-to-Text**, **Hugging Face LLM**, and **Piper Text-to-Speech**.

This project demonstrates an end-to-end conversational AI receptionist capable of receiving speech, generating intelligent responses, and speaking back to the user. It also provides REST APIs and WebSocket endpoints for future Twilio Media Streams integration.

---

# Features

- 🎤 Speech Recording
- 📝 Whisper Speech-to-Text
- 🤖 Hugging Face LLM
- 🔊 Piper Text-to-Speech
- 💬 Conversation Memory
- ⚡ FastAPI REST APIs
- 🌐 WebSocket Endpoint for Twilio Media Streams
- 📖 Swagger API Documentation

---

# Tech Stack

- Python 3.13
- FastAPI
- OpenAI Whisper
- Hugging Face Inference API
- Piper TTS
- Silero VAD (Prototype Stage)
- SoundDevice
- SoundFile
- Uvicorn
- WebSockets

---

# Project Structure

```
Receptionist Prototype
│
├── models/
│   ├── en_US-lessac-medium.onnx
│   └── en_US-lessac-medium.onnx.json
│
├── output/
│
├── routes/
│   ├── webhook.py
│   ├── incoming_call.py
│   ├── media_stream.py
│   └── chat.py
│
├── services/
│   ├── audio_recorder.py
│   ├── whisper_service.py
│   ├── llm_service.py
│   └── voice_service.py
│
├── app.py
├── main.py
├── receptionist.py
├── conversation.py
├── prompts.py
├── config.py
├── requirements.txt
└── README.md
```

---

# Module Description

## app.py

Main FastAPI application.

Responsibilities

- Creates FastAPI application
- Registers API routes
- Exposes Swagger Documentation

---

## main.py

Desktop prototype entry point.

Pipeline

Microphone

↓

Whisper

↓

Conversation Manager

↓

LLM

↓

Piper

---

## receptionist.py

Core receptionist controller.

Responsibilities

- Coordinate complete AI pipeline
- Manage services
- Return structured responses

---

## conversation.py

Maintains complete conversation history between patient and Sarah.

---

## prompts.py

Stores the system prompt used by the LLM.

---

## config.py

Contains all configurable project constants including

- Sample Rate
- Audio Paths
- Whisper Model
- Piper Model
- Hugging Face API Configuration

---

# Services

## audio_recorder.py

Responsible for

- Recording microphone audio
- Saving WAV file
- Returning recorded file path

---

## whisper_service.py

Responsible for

- Loading Whisper
- Speech-to-text transcription

---

## llm_service.py

Responsible for

- Sending prompt to Hugging Face
- Receiving AI response

---
## Download Piper Model

Download the Piper model:

en_US-lessac-medium.onnx

Place it inside:

models/

## voice_service.py

Responsible for

- Piper Text-to-Speech
- Playing generated audio

---

# API Endpoints

## GET /

Health Check

Response

```json
{
  "message": "AI Receptionist Prototype Running"
}
```

---

## POST /webhook

Runs the complete receptionist pipeline.

Pipeline

Patient Speech

↓

Whisper

↓

Conversation

↓

LLM

↓

Piper

↓

Response

---

## POST /chat

Testing endpoint.

Allows direct interaction with the LLM without requiring speech recognition.

Request

```json
{
    "message":"Book appointment tomorrow."
}
```

Response

```json
{
    "response":"Certainly. What time would you prefer?"
}
```

---

## POST /incoming-call

Twilio Incoming Call Webhook.

Returns TwiML instructing Twilio to connect the call to the Media Stream WebSocket.

---

## WebSocket /media-stream

Twilio Media Streams endpoint.

Current Responsibilities

- Accept WebSocket connection
- Receive Twilio Events
- Handle
  - connected
  - start
  - media
  - stop

Future Responsibilities

- Decode Base64 payload
- μ-law → PCM conversion
- Whisper STT
- Conversation Manager
- LLM
- Piper TTS
- Stream synthesized audio back to Twilio

---

# Running Desktop Prototype

Create Virtual Environment

```bash
python -m venv .venv
```

Activate Environment

Windows

```bash
.venv\Scripts\activate
```

Install Dependencies

```bash
pip install -r requirements.txt
```

Run Desktop Prototype

```bash
python main.py
```

---

# Running FastAPI

```bash
uvicorn app:app --reload
```

Swagger

```
http://127.0.0.1:8000/docs
```

---

# Twilio Development

Expose local server

```bash
ngrok http 8000
```

Configure Twilio Incoming Call URL

```
https://<ngrok-url>/incoming-call
```

Media Stream Endpoint

```
wss://<ngrok-url>/media-stream
```

---

# Current Project Status

Completed

- Whisper STT
- Hugging Face LLM
- Piper TTS
- Conversation Manager
- Desktop Voice Prototype
- FastAPI Backend
- Swagger Documentation
- Chat Testing Endpoint
- Incoming Call Webhook
- Twilio Media Stream Skeleton

Pending

- Twilio Audio Stream Processing
- μ-law Audio Decoding
- Real-time Whisper Transcription
- Streaming Audio Response
- Appointment Backend Integration
- PostgreSQL Integration
- Calendar Integration
- Production Logging
- Authentication
- Docker Deployment

---

# Future Roadmap

- Real-time Twilio Voice Conversation
- Appointment Booking API
- Patient Database
- Calendar Integration
- Doctor Availability
- Multi-language Support
- Multi-clinic Support
- Production Deployment
- Kubernetes Deployment

---

# Author

Tapendra Verma

AI Receptionist Prototype

Xtel Global Internship