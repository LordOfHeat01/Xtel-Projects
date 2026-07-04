import whisper
from config import (
    WHISPER_MODEL,
    INPUT_AUDIO_FILE
)


class WhisperService:
    def __init__(self):
        """Load the Whisper model once when the application starts."""

        self.model = whisper.load_model(WHISPER_MODEL)


    def transcribe(self, audio_file=INPUT_AUDIO_FILE):
        """
        Covnert speech from an audio file into text.
        
        Args:
        audio_file(str): Path to the audio file.
        
        Returns:
        str: Transcribed text from the audio.
        
        """
        try:
            result = self.model.transcribe(audio_file)
            return result["text"].strip()
        
        except Exception as error:
            print(f"Whisper Error:{error}")
            return ""

# flow patient.wav ->whisperservice ->whisper model ->transcript -> return text
#         