import speech_recognition as sr
from googletrans import Translator
import pyttsx3
import gtts


def speech_to_text(language='en-US'):
    recognizer = sr.Recognizer()
    translator = Translator()
    text_speech = pyttsx3.init()

    with sr.Microphone() as source:
        print("Please speak...")
        recognizer.adjust_for_ambient_noise(source, duration=0.5)
        audio = recognizer.listen(source)

    try:
        text = recognizer.recognize_google(audio, language=language)
        print("You said:", text)

        

        if language.startswith('ar'):
            translation = translator.translate(text, src='ar', dest='en')
            print("Translated text:", translation.text)
       

    except sr.UnknownValueError:
        print("Sorry, could not understand audio.")
    except sr.RequestError as e:
        print("Error:", str(e))


if __name__ == "__main__":
    speech_to_text('ar-SA')  

    