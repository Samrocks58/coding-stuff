import speech_recognition as sr, keyboard

r = sr.Recognizer()

def Stop():
    quit()
print("Say something!!!")
while True:
    with sr.Microphone() as source:
        audio = r.listen(source)


    try:
        print(r.recognize_google(audio))
    except sr.UnknownValueError:
        print("Please Try Again.")
    #keyboard.on_press_key('q', Stop())
    # except sr.UnknownValueError:
    #    print("Google Speech Recognition could not understand audio")

    #keyboard.on_press_key('q', Stop())