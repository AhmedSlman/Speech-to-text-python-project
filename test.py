# import speech_recognition 
# import logging
# import pyttsx3
# # import tensorflow as tf


# logging.basicConfig(filename='speech_recognition.log', level=logging.ERROR)

# recognizer = speech_recognition.Recognizer()
# text_speech = pyttsx3.init()

# while True:
#     try:
#         with speech_recognition.Microphone() as mic:
#             recognizer.adjust_for_ambient_noise(mic, duration=0.2)
#             audio = recognizer.listen(mic)

#             if audio is None:
#                 print("No audio detected. Please speak clearly.")
#                 continue

#             text = recognizer.recognize_google(audio)
#             text = text.lower()
#             print(f"Recognized: {text}")

           
#     except speech_recognition.UnknownValueError as e:
#         logging.error(f"UnknownValueError occurred: {str(e)}")
#         print("Sorry, I couldn't understand what you said. Please speak more clearly.")
#         continue
#     except speech_recognition.RequestError as e:
#         logging.error(f"RequestError occurred: {str(e)}")
#         print("Error with the speech recognition service. Please try again later.")
#         break


 
