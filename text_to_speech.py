import pyttsx3


def speech(text):
    engine = pyttsx3.init('dummy')
    engine.say(text)
    engine.runAndWait()


speech('Hello')

'''
engine = pyttsx3.init()

voices = engine.getProperty('voices')
for voice in voices:
    print("Voice:")
    print(" - ID: %s" % voice.id)
    print(" - Name: %s" % voice.name)
    print(" - Languages: %s" % voice.languages)
    print(" - Gender: %s" % voice.gender)
    print(" - Age: %s" % voice.age)'''