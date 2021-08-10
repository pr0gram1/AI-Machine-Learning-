import weather_reporter
import pyjokes
import datetime
import wikipedia
import pyttsx3
import pywhatkit
import speech_recognition as reco



listener = reco.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)



def speech(text):
    engine.say(text)
    engine.runAndWait()



def get_request():
    try:
        #command = ""
        with reco.Microphone as source:
            print('What is your command')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'python' in command:
                command = command.replace('python', '')
                print(command)

    except:
        pass
    return command


def python_enabplerecognition():
    command = get_request()
    print(command)
    if 'Python play' in command:
        song = command.replace('Python play', '')
        speech('playing' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        speech('Current time is' + time)
    elif 'Who is' in command:
        human = command.replace("Who is", '')
        information_result = wikipedia.summary(human, 1)
        print(information_result)
        speech(information_result)
    elif 'How are you today Python' in command:
        speech('Im awesome')
    elif 'Whats 2+2 ' in command:
        speech('2+2 = 4 ')
    elif 'joke' in command:
        speech(pyjokes.get_joke())

    elif 'Whats the weather like' in command:
        speech(weather_reporter)
    else:
        speech('Sorry, I didnt understand what did you say')

while True:
    python_enabplerecognition()
