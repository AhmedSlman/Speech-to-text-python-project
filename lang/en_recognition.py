
import speech_recognition as sr
import pyttsx3

def speech_to_text(language='en-US'):
    recognizer = sr.Recognizer()
    text_speech = pyttsx3.init()


    with sr.Microphone() as source:
        print("Please speak...")
        recognizer.adjust_for_ambient_noise(source, duration=0.5)
        audio = recognizer.listen(source)

    try:
        text = recognizer.recognize_google(audio, language=language)
        print("You said:", text)
        #
        #هنا هيتم العمليات  جوا الموديل بعدين ناخد الناتج نكمل بيه 
        #
        #
        text_speech.say(text)
        audio_file = "output_audio.mp3"
        text_speech.save_to_file(text, audio_file)
        text_speech.runAndWait()


    except sr.UnknownValueError:
        print("Sorry, could not understand audio.")
    except sr.RequestError as e:
        print("Error:", str(e))

if __name__ == "__main__":
    speech_to_text('en-US')      
