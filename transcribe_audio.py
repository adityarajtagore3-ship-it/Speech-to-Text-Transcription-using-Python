import speech_recognition as sr
from datetime import datetime

recognizer = sr.Recognizer()

audio_file = "audio.wav"
output_file = "transcription.txt"

try:
    with sr.AudioFile(audio_file) as source:
        print("Adjusting for background noise...")
        recognizer.adjust_for_ambient_noise(source, duration=1)
        audio_data = recognizer.record(source)

        print("Transcribing audio...")
        text = recognizer.recognize_google(audio_data)

        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        with open(output_file, "w") as f:
            f.write(f"[{timestamp}]\n{text}")

        print("Transcription saved to transcription.txt")

except sr.UnknownValueError:
    print("Audio not clear enough to transcribe.")

except sr.RequestError as e:
    print(f"API request error: {e}")
