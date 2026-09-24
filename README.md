# 🦷 AI Dental Receptionist

An AI-powered voice receptionist prototype designed for dental clinics. The system enables patients to interact with a virtual receptionist through natural voice conversations for common clinic-related queries and appointment-related interactions.

The project was developed as part of the **Xtel Global internship** and focuses on building a modular foundation that can later be extended into a production-ready AI receptionist platform.

---

## 📖 Introduction

Traditional dental reception systems require patients to wait for a receptionist to become available, especially for routine queries such as clinic timings, doctor information, appointment enquiries, and other frequently asked questions.

The **AI Dental Receptionist** aims to automate these interactions using a conversational voice-based AI system.

The prototype combines:

- 🎙️ Speech-to-Text
- 🧠 Large Language Models
- 💬 Conversation Management
- 🔊 Text-to-Speech
- 📞 Voice/Telephony Integration
- ⚡ Backend APIs
- 🧩 Intent Detection
- 📅 Appointment-oriented business logic

The architecture is designed to keep the AI layer, business logic, and infrastructure modular so that individual components can be improved or replaced independently.

---
## 🏗️ High-Level Architecture

The AI Receptionist follows a modular, event-driven architecture where each component is responsible for a specific part of the conversation pipeline.

### 🔹 1. Voice & Telephony Layer
- **Twilio** handles incoming and outgoing phone calls.
- **Vapi** acts as the voice orchestration layer, managing the real-time interaction between the caller and the AI receptionist.

### 🔹 2. Speech-to-Text Layer
- **Whisper STT** converts the caller's speech into text.
- **VAD (Voice Activity Detection)** helps identify when the caller starts and stops speaking, reducing unnecessary transcription and improving responsiveness.

### 🔹 3. Conversation & Intent Layer
- The **Conversation Manager** maintains the conversation history and contextual information.
- The system performs **early intent detection** while the caller is speaking, allowing potential intents such as booking, cancellation, or general enquiries to be identified early.

### 🔹 4. AI / LLM Layer
- **Qwen 2.5 1.5B Instruct** processes the user's message along with the conversation context.
- The LLM generates a concise, professional response while following the receptionist's instructions and safety rules.

### 🔹 5. Business Logic Layer
- Handles receptionist-specific operations such as:
  - 📅 Appointment booking
  - ❌ Appointment cancellation
  - 🩺 Doctor-related enquiries
  - 🏥 Clinic information
  - ❓ Frequently asked questions
- Business actions are separated from the LLM so that the model does not directly control critical operations.

### 🔹 6. Data & Event Layer
- **PostgreSQL** is intended to store persistent application data such as patients and appointments.
- **Kafka** is used for event-driven communication and temporary conversation/event storage with retention requirements.

### 🔹 7. Text-to-Speech Layer
- **Piper TTS** converts the AI-generated response back into natural speech.
- The generated audio is returned to the voice pipeline and delivered to the caller.

### 🔹 8. Backend & Integration Layer
- **FastAPI** provides the backend API and webhook endpoints.
- It connects the voice pipeline with the AI, business logic, and external services.

### 🔹 9. Deployment Layer
- The application is designed to be containerized using **Docker**.
- **Kubernetes** can be used for deployment, scaling, and managing the application in a production environment.
# 🚀 Explore the Final Prototype

The repository contains multiple stages of development, experiments, and supporting projects.

> ⭐ **The final refined AI Receptionist prototype is available in the [`Receptionist Prototype`](./Receptionist%20Prototype) folder.**

If you want to explore the complete AI Receptionist implementation, **start with this folder**.

## 📂 Repository Structure

```text
Xtel-Projects/
│
├── 📁 Calculator/
├── 📁 FASTAPI-CRASH/
├── 📁 Receptionist Prototype/   ⭐ Final AI Receptionist Prototype
└── 📁 Test Receptionist/
