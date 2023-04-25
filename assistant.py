import datetime
import pyttsx3
import pywhatkit
import speech_recognition as sr
import speech_recognition.exceptions
from Commands.message import message
from Plugins import chatGPT

# Voice Recognition Initialization
listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


# TTS Function
def talk(text):
    engine.say(text)
    engine.runAndWait()


# Call get_response when needing additional user input via speaking
def get_response():
    try:
        with sr.Microphone() as source:
            print("Listening to your Response")
            voice = listener.listen(source)
            feed = listener.recognize_google(voice)
            feed = feed.lower()
            print(feed)
    except NameError:
        print("An exception occurred")
    return feed


# Gets initial command
def take_command():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            cmd = listener.recognize_google(voice)
            cmd = cmd.lower()
            if "test" in cmd:
                cmd = cmd.replace("test", '')
                print(cmd)
    except NameError:
        print("An exception occurred")
    return cmd


# Alexa
def run_alexa():
    command = take_command()
    try:
        # Said Only Wake word
        if command == "test":
            talk("Sorry, I didn't get that")

        # Will open YouTube with a random video from the channel
        elif 'play' in command:
            song = command.replace('play', '')
            talk('playing ' + song)
            pywhatkit.playonyt(song)

        # Will ask ChatGPT for information on thing
        elif 'what is' in command:
            talk(chatGPT.new_chat(command))

        # Will return time
        elif 'time' in command:
            time = datetime.datetime.now().strftime('%I:%M %p')
            talk('Current time is ' + time)

        # Will message someone (Person will need to be in contact.json file to message)
        elif 'message' in command:
            message(command, talk, get_response)
        # Will tell a joke
        elif 'joke' in command:
            chatGPT.getJoke(command)

        # Will write a paper based on your parameters and store/open the file when done
        elif 'write a paper' in command:
            chatGPT.write_paper(command)

        # Did not understand
        else:
            talk("Sorry I did not understand that.")

    except speech_recognition.UnknownValueError:
        talk("Can you repeat that please?")


while True:
    run_alexa()
