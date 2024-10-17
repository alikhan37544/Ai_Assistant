import whisper
import sounddevice as sd
import numpy as np

# Load the Whisper model
model = whisper.load_model("base.en")

def transcribe_audio():
    print("Listening...")

    # Record audio (sample rate 16000)
    audio = sd.rec(int(16000 * 5), samplerate=16000, channels=1, dtype=np.int16)
    sd.wait()  # Wait until the recording is finished

    # Transcribe the audio using Whisper
    result = model.transcribe(np.squeeze(audio))
    return result['text']
