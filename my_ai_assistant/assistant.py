import os
import yaml
from utils.speech_recognition import transcribe_audio
from utils.text_to_speech import speak_text
from utils.llama_integration import get_llama_response

# Load configurations
with open("config.yaml", "r") as f:
    config = yaml.safe_load(f)

def main():
    print("Starting AI Assistant...")
    while True:
        print("Press Enter to start speaking...")
        input()  # Wait for user to press Enter
        text = transcribe_audio()  # Capture and transcribe audio
        print(f"You said: {text}")
        
        response = get_llama_response(text)  # Get Llama response
        print(f"Assistant: {response}")
        
        speak_text(response)  # Speak the response
        
if __name__ == "__main__":
    main()
