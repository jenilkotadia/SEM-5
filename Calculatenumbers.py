import wolframalpha
import pyttsx3

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
rate = engine.setProperty("rate",170)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def WolfRamAlpha(query):
    apikey = "YVLUA4-YT29E72X5T"
    requester = wolframalpha.Client(apikey)
    requested = requester.query(query)

    try:
        answer = next(requested.results).text
        return answer
    except:
        speak("The value is not answerable")

def Calc(query):
    Term = str(query)
    Term = Term.replace("echo","")
    Term = Term.replace("multiply","*")
    Term = Term.replace("into", "*")
    Term = Term.replace("plus","+")
    Term = Term.replace("add", "+")
    Term = Term.replace("minus","-")
    Term = Term.replace("subtract", "-")
    Term = Term.replace("divide","/")
    Term = Term.replace("by", "/")

    Final = str(Term)
    try:
        result = WolfRamAlpha(Final)
        print(f"{result}")
        speak(result)

    except:
        speak("The value is not answerable")