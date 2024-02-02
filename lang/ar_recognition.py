import speech_recognition as sr
from googletrans import Translator
import pyttsx3
import arabic_reshaper

def speech_to_text(language='ar-SA'):
    recognizer = sr.Recognizer()
    translator = Translator()
    text_speech = pyttsx3.init()
    text_speech.setProperty('voice', 'ar')


    with sr.Microphone() as source:
        print("Please speak...")
        recognizer.adjust_for_ambient_noise(source, duration=0.5)
        audio = recognizer.listen(source)

    try:
        text = recognizer.recognize_google(audio, language=language)
        reshaped_said_text=arabic_reshaper.reshape( text)

        print("You Said:", reshaped_said_text)
        
        translated_text = translator.translate(text, src='ar', dest='en')
        print("Translated English Text:", translated_text.text)



        
        
        translated_arabic_text = translator.translate(translated_text.text, src='en', dest='ar')
        reshaped_text=arabic_reshaper.reshape( translated_arabic_text.text)
        print("Translated Arabic Text:", reshaped_text)
        
        # Convert translated Arabic text to speech
        text_speech.say(translated_arabic_text.text)
        text_speech.save_to_file(translated_arabic_text.text, "output_audio.mp3")
        text_speech.runAndWait()

    except sr.UnknownValueError:
        print("Sorry, could not understand audio.")
    except sr.RequestError as e:
        print("Error:", str(e))

if __name__ == "__main__":
    speech_to_text('ar-SA')
