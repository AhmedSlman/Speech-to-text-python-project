import assemblyai as aai
import pyttsx3
from googletrans import Translator
import gtts

aai.settings.api_key = "61341f550b5e4a64b889c0409c0f2009"
text_speech = pyttsx3.init()


# convirting voice to text

FILE_URL = "https://github.com/AssemblyAI-Examples/audio-examples/raw/main/20230607_me_canadian_wildfires.mp3"


transcriber = aai.Transcriber()
transcript = transcriber.transcribe(FILE_URL)
print(transcript.text) #printing text 

# text_speech.say(transcript.text)#هنا بيطبق اي نص بكتبه بس اتا اديته النص اللي طلع لما حولنا الصوت 
audio_file = "output_audio.mp3"
text_speech.save_to_file(transcript.text, audio_file)
text_speech.runAndWait()


def translate_to_arabic(text):
    translator = Translator()
    try:
        translation = translator.translate(text, src='en', dest='ar')
        return translation.text
    except Exception as e:
        print("Translation Error:", e)
        return None

if __name__ == "__main__":
    arabic_translation = translate_to_arabic(transcript.text)
    if arabic_translation:
        print("Arabic translation:", arabic_translation)
    else:
        print("Translation failed.")



tts=gtts.gTTS(arabic_translation,lang="ar")
tts.save("hello.mp3")
text_speech.say(tts)
text_speech.runAndWait()
