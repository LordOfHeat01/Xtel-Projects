from conversation import ConversationManager

from services.llm_service import LLMService
from services.voice_service import VoiceService
from services.audio_recorder import AudioRecorder
from services.whisper_service import WhisperService

class Receptionist:

    def __init__(self):
        """Initialize the AI Receptionist prototype."""

        # Initialize all services
        self.conversation = ConversationManager()
        self.llm = LLMService()
        self.voice = VoiceService()
        self.whisper = WhisperService()
        self.recorder = AudioRecorder()

    def handle_conversation(self):    
        """
        Execut one complete receptionist interation"""

        #Record patient's audio
        audio_file = self.recorder.record(duration=10)
        
        #Convert speech to text
        transcript = self.whisper.transcribe(audio_file)

        print("\nPatient:")
        print(transcript)

        #Exit command
        if any(word in transcript.lower() for word in ["exit", "quit", "goodbye", "stop"]):
           
            return {
                "status": "exit",
                "transcript": transcript,
            }
        
        #store patient's message
        self.conversation.add_user_message(transcript)

        #Generate AI response
        reply = self.llm.generate_response(
            self.conversation.get_messages())
        
        #store AI response
        self.conversation.add_assistant_message(reply)

        print("\nSarah:")
        print(reply)

        #speak reply
        self.voice.speak(reply)

        return {
            "status":"success",
            "transcript": transcript,
            "response": reply
        }
    
    def clear(self):
        """Clear the conversation history."""
        self.conversation.clear()