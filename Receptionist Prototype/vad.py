# the task of this file is to detect speech
# Opening microphone
# Running Silero VAD
# Returning the recorded audio

from silero_vad import load_silero_vad,get_speech_timestamps
import torch

class VADService:
    """Handles Voice Activity Detection (VAD) using Silero VAD."""


    def __init__(self):
        print("Loading Silero VAD model...")

        self.model = load_silero_vad()

        print("Silero VAD model loaded successfully.")


    # def detect_speech(self,audio):
    #     """
    #     Detects wether the given audio contains speech.
    #     Args:
    #     auidio (numpy.ndarray): The audio data to analyze.
        
    #     Returns:
    #     bool: True if speech is detected, False otherwise.
    #     """

    #     #convert numpy array to torch tensor

    #     audio_tensor = torch.from_numpy(audio).float()    

    #     speech = get_speech_timestamps(audio_tensor, self.model, sampling_rate=16000)
    #     return len(speech) > 0