import assemblyai as aai
import pyttsx3


aai.settings.api_key = "61341f550b5e4a64b889c0409c0f2009"
text_speech = pyttsx3.init()


FILE_URL = "https://github.com/AssemblyAI-Examples/audio-examples/raw/main/20230607_me_canadian_wildfires.mp3"


transcriber = aai.Transcriber()
transcript = transcriber.transcribe(FILE_URL)

print(transcript.text)
# text_speech.say(transcript.text)
audio_file = "output_audio.mp3"
text_speech.save_to_file(transcript.text, audio_file)
text_speech.runAndWait()

