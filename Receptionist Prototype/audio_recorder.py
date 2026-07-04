# Microphone
#       │
#       ▼
# 20–30 ms Audio Frame
#       │
#       ▼
# Silero VAD
#       │
#       ├── No Speech → Ignore
#       │
#       └── Speech → Keep Recording
# above is the working of silero

import os 
import sounddevice as sd
import soundfile as sf
import numpy as np
import torch
import queue
from silero_vad import load_silero_vad, get_speech_timestamps
from vad import VADService


from config import(
    SAMPLE_RATE,
    CHANNELS,
    AUDIO_DTYPE,
    INPUT_FOLDER,
    INPUT_AUDIO_FILE,

)

class AudioRecorder:
    def __init__(self):
        """Initialize audio recorder."""

        #create input folder if it doesn't exist
        os.makedirs(INPUT_FOLDER,exist_ok=True)

        #Initialize VAD service
        self.vad = VADService()
    
    def record(self,duration=5):
        """
        Record audio using InputStream.
        This is the fist step toward vad integreation
        """
        print("\nListening....")
        
        frames = [] 

        def audio_callback(indata, frames_count,time, status):
            if status:
                print(status)

            frames.append(indata.copy())        

         #Open microphone stream
        with sd.InputStream(
        
        samplerate=SAMPLE_RATE,
        channels=CHANNELS,
        dtype=AUDIO_DTYPE,
        callback=audio_callback
         ):
            
            #record for 5 seconds temporary
             sd.sleep(int(duration * 1000))   

        #Combine all recorded chunks
        recording = np.concatenate(frames, axis=0)      

        #save audio
        sf.write (
            INPUT_AUDIO_FILE,
            recording,
            SAMPLE_RATE 
        )       

        print("Recording Completed")
        print(f"Audio saved at :{INPUT_AUDIO_FILE}")
        return INPUT_AUDIO_FILE


        

    # def record(self,duration=5):
            
    #         """
    #           Record audio from the microphone.

    #         Args:
    #         duration (int): Recording duration in seconds.

    #          Returns:
    #         str: Path of the recorded audio file.
    #          """
            
    #         print("\nListening....")    

    #         recording = sd.rec(
    #              int(duration * SAMPLE_RATE),
    #              samplerate=SAMPLE_RATE,
    #              channels=CHANNELS,
    #              dtype=AUDIO_DTYPE
    #         )


    #         sd.wait()

    #         sf.write(
    #              INPUT_AUDIO_FILE,
    #              recording,
    #              SAMPLE_RATE
    #         )

    #         print("Recording completed")
    #         print(f"Audio saved at:{INPUT_AUDIO_FILE}")

    #         return INPUT_AUDIO_FILE