import speech_recognition as sr

recognizer = sr.Recognizer()

with sr.Microphone() as source:
    print("Calibrating microphone...")
    recognizer.adjust_for_ambient_noise(source, duration=1)

    print("Speak now...")
    audio = recognizer.listen(source)

    try:
        text = recognizer.recognize_google(audio)
        print("You said:")
        print(text)

    except sr.UnknownValueError:
        print("Could not understand the audio.")

    except sr.RequestError as e:
        print(f"Service error: {e}")
