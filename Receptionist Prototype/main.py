# this main.py should orchestrate, not implement 
from conversation import ConversationManager
from llm import LLMService
from voice import VoiceService
from whisper_stt import WhisperService
from audio_recorder import AudioRecorder



def main():
    """Run the AI Receptionist protoype."""


    print("Welcome to the AI Receptionist Prototype!")
    print("=" * 50)
    print("      AI Receptionist Prototype Started")
    print("=" * 50)
    print("Say 'exit' to end the conversation.")

    # Initialize allservices
    conversation = ConversationManager()
    llm = LLMService()
    voice = VoiceService()
    whisper = WhisperService()
    recorder = AudioRecorder()
    #vad = VADService()


    while True:
        #Record audio
        audio_file  = recorder.record(duration=20)

        # audio, samplerate = sf.read(audio_file)
        # print(f"Speech Detected:{vad.detect_speech(audio)}")

        # #convert speech to text
        transcript =  whisper.transcribe(audio_file)

        print("\nPatient:")
        print(transcript)

        #exit command 
        if any(word in transcript.lower() for word in ["exit", "quit", "goodbye", "stop"]):
              print("\nExit command received.")
              break
        
        #save patient's message
        conversation.add_user_message(transcript)
        
        #generate AI response

        reply = llm.generate_response(conversation.get_messages())

        #save ai response
        conversation.add_assistant_message(reply)

        #display reply
        print("\nSarah:")
        print(reply)

        #convert reply to speech
        voice.speak(reply)
        

    conversation.clear()
    print("\nConversation deleted.")
    print("Goodbye!")

    
if __name__=="__main__":
    main()
