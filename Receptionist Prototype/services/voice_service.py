import wave
import winsound

from piper import PiperVoice

from config import (
    PIPER_MODEL,
    OUTPUT_AUDIO_FILE
)


class VoiceService:
    def __init__(self):
        """Load the Piper model once when the application starts."""

        self.voice = PiperVoice.load(PIPER_MODEL)

    def speak(self, text):
        """
        Convert text into speech and play it.
        """
        # print('\nSarah is speaking...')

        try:
            with wave.open(OUTPUT_AUDIO_FILE, "wb") as wav_file:
                self.voice.synthesize_wav(
                    text,
                    wav_file
                )

            winsound.PlaySound(
                OUTPUT_AUDIO_FILE,
                winsound.SND_FILENAME
            )
            # print("Response delivered successfully.")

        except Exception as error:
            print(f"TTS Error: {error}")