import whisper
import sounddevice as sd
import numpy as np
import torch

# Load the Whisper model
model = whisper.load_model("base.en")

def transcribe_audio():
    print("Listening...")

    # Record audio (sample rate 16000)
    audio = sd.rec(int(16000 * 5), samplerate=16000, channels=1, dtype=np.int16)
    sd.wait()  # Wait until the recording is finished

    # Convert audio to floating-point format (normalize between -1 and 1)
    audio = audio.astype(np.float32) / 32768.0

    # Transcribe the audio using Whisper
    result = model.transcribe(np.squeeze(audio))
    return result['text']
