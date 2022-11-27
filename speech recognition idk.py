import speech_recognition as sr
from speech_recognition import Microphone

r = sr.Recognizer()

def Stop():
    quit()
print("Say something!!!")
m = None
for i, microphone_name in enumerate(Microphone.list_microphone_names()):
    if microphone_name == "Microphone Array (IntelÂ® Smart Sound Technology for Digital Microphones)":
        m = Microphone(device_index=i)
while True:
    with m as source:
        audio = r.listen(source)


    try:
        print(r.recognize_google(audio))
    except sr.UnknownValueError:
        print("Please Try Again.")
    #keyboard.on_press_key('q', Stop())
    # except sr.UnknownValueError:
    #    print("Google Speech Recognition could not understand audio")

    #keyboard.on_press_key('q', Stop())