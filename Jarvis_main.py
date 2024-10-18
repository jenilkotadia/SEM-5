import datetime
import os
import pyttsx3
import speech_recognition
from SearchNow import searchGoogle, searchYoutube, searchWikipedia
import pyautogui
import time
from jarvis_gui import window_1 
from window_2 import window_2
import threading
import tkinter as tk
from tkinter import messagebox
from ai_handler import ask_rapidapi

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
engine.setProperty("rate", 170)


is_muted = False

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def takeCommand():
    r = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:
        print("Listening.....")
        r.pause_threshold = 0.8  
        r.energy_threshold = 300
        audio = r.listen(source, 0, 4)

    try:
        print("Understanding..")
        query = r.recognize_google(audio, language='en-in')
        print(f"You Said: {query}\n")
    except Exception as e:
        print("Say that again")
        return "None"
    return query

def toggle_mute():
    global is_muted
    pyautogui.press("m")
    if is_muted:
        speak("Video unmuted")
    else:
        speak("Video muted")
    is_muted = not is_muted

def confirm_action(action):
    
    root = tk.Tk()
    root.withdraw()  
    response = messagebox.askquestion("Confirm Action", f"Do you wish to {action} your computer?", parent=root)
    root.destroy()
    return response == 'yes'

def executeCommand(query):
    global is_muted

    if "wake up" in query:
        from GreetMe import greetMe
        greetMe()

        while True:
            query = takeCommand().lower()

            if "go to sleep" in query:
                speak("Ok sir, you can call me anytime")
                break

            elif 'using ai' in query or 'using AI' in query or 'using aI' in query or 'using Ai' in query: 
                query = query.replace("using ai", "")
                query = query.replace("using AI", "")
                query = query.replace("using aI", "")
                query = query.replace("using Ai", "")
                print("Processing your request via AI...")
                speak("Processing your request via AI...")
                answer = ask_rapidapi(query)  
                print(f"Here is your answer: {answer}")  
                speak("Here is your answer.")

            elif "show screenshot" in query:  
                screenshot_path = "ss.jpg"  
                if os.path.exists(screenshot_path):
                    os.startfile(screenshot_path)  
                    speak("Here is the screenshot")  
                    pyautogui.sleep(3) 
                    pyautogui.hotkey("alt", "f4") 
                else:
                    speak("Screenshot not found")

            elif "screenshot" in query:
                    im = pyautogui.screenshot()
                    im.save("ss.jpg")
                    pyautogui.sleep(2)
                    speak("Screenshot taken")

            elif "click my photo" in query:
                    pyautogui.press("super")
                    pyautogui.typewrite("camera",0.1)
                    pyautogui.press("enter")
                    pyautogui.sleep(2)
                    speak("SMILE")
                    pyautogui.press("enter")
                    pyautogui.sleep(2) 
                    pyautogui.hotkey("alt", "f4") 
                    pyautogui.sleep(2)
                    speak("Photo Taken")

            elif "hello" in query:
                speak("Hello sir, how are you?")
            elif "i am fine" in query:
                speak("That's great, sir")
            elif "how are you" in query:
                speak("Perfect, sir")
            elif "thank you" in query:
                speak("You're welcome, sir")

            elif "pause" in query:
                pyautogui.press("k")
                speak("Video paused")
            elif "play" in query:
                pyautogui.press("k")
                speak("Video played")
            elif "mute" in query or "unmute" in query:
                toggle_mute()

            elif "volume up" in query:
                from keyboard import volumeup
                speak("Turning volume up, sir")
                volumeup()
            elif "volume down" in query:
                from keyboard import volumedown
                speak("Turning volume down, sir")
                volumedown()

            elif 'open chrome' in query:
                os.startfile('C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe')
                speak("Google Chrome is open, sir")
                
            elif 'maximize the window' in query:
                pyautogui.hotkey('alt', 'space')
                time.sleep(1)
                pyautogui.press('x')
                speak("window is maximized")
                
            elif 'new window' in query:
                pyautogui.hotkey('ctrl', 'n')
                speak("new window is open")

            elif 'incognito window' in query:
                pyautogui.hotkey('ctrl', 'shift', 'n')
                speak("incognito window is open")
                
            elif 'minimise the window' in query:
                pyautogui.hotkey('alt', 'space')
                time.sleep(1)
                pyautogui.press('n')
                speak("window is minimized")
        
            elif 'history' in query:
                pyautogui.hotkey('ctrl', 'h')
                speak("history is open")
    
            elif 'downloads' in query:
                pyautogui.moveTo(1887, 71, duration=1.5)  
                pyautogui.click()  
                pyautogui.moveTo(1728, 431, duration=1.5)  
                pyautogui.click() 
                speak("downloads is open")

            elif 'previous tab' in query:
                pyautogui.hotkey('ctrl', 'shift', 'tab')
                speak("previous tab")
                
            elif 'next tab' in query:
                pyautogui.hotkey('ctrl', 'tab')
                speak("next tab")
                
            elif 'close window' in query:
                pyautogui.hotkey('ctrl', 'shift', 'w')
                speak("window is closed")
            
            elif 'close chrome' in query:
                os.system("taskkill /f /im chrome.exe")
                speak("chrome is closed")

            elif 'maximize the paint' in query:
                pyautogui.hotkey('win', 'up')
                time.sleep(1)
                speak("paint is maximized")

            elif "open" in query:
                from Dictapp import openappweb
                openappweb(query)
            elif "close" in query:
                from Dictapp import closeappweb
                closeappweb(query)    

            elif "google" in query:
                searchGoogle(query)
            elif "youtube" in query:
                searchYoutube(query)
            elif "wikipedia" in query:
                searchWikipedia(query)

            elif "news" in query:
                from NewsRead import latestnews
                latestnews()

            elif "calculate" in query:
                from Calculatenumbers import WolfRamAlpha
                from Calculatenumbers import Calc
                query = query.replace("calculate","")
                query = query.replace("echo","")
                Calc(query)

            elif "whatsapp" in query:
                from Whatsapp import sendMessage
                sendMessage()

            elif "the time" in query:
                strTime = datetime.datetime.now().strftime("%H:%M")    
                speak(f"Sir, the time is {strTime}")  

            elif "refresh" in query:
                pyautogui.hotkey('win', 'd')
                time.sleep(1)
                pyautogui.press('f5')
                time.sleep(1)
                speak("pc is refreshed")
                pyautogui.rightClick()
                pyautogui.rightClick()

            elif "scroll down" in query:
                speak("Scrolling down")
                for _ in range(5):  
                    pyautogui.scroll(100)  
                    time.sleep(0.5)  
                speak("Scrolled down")

            elif "scroll up" in query:
                speak("Scrolling up")
                for _ in range(5):  
                    pyautogui.scroll(-100)  
                    time.sleep(0.5)  
                speak("Scrolled up")

            elif 'type' in query: 
                query = query.replace("type", "")
                pyautogui.write(f"{query}",interval=0.1)
                pyautogui.press("enter")
                speak("Typed")

            elif "draw a line" in query:
                pyautogui.moveTo(x=267, y=387, duration=1)
                pyautogui.leftClick
                pyautogui.dragRel(267, 0, 1)
                speak("Line drawn")

            elif "draw a square" in query:
                pyautogui.moveTo(x=1308, y=376, duration=1) 
                pyautogui.click()  
                distance = 300  
                for i in range(1):  
                    pyautogui.dragRel(distance, 0, duration=0.5)  
                    pyautogui.dragRel(0, distance, duration=0.5)  
                    pyautogui.dragRel(-distance, 0, duration=0.5)  
                    pyautogui.dragRel(0, -distance, duration=0.5)  
                speak("Square Drawn")

            elif "red colour" in query:
                pyautogui.moveTo(x=1074, y=105, duration=1)
                pyautogui.click(x=1074, y=105, clicks=1, interval=0, button='left')
                speak("Red colour picked")

            elif "draw a rectangular spiral" in query:
                pyautogui.moveTo(x=300, y=393, duration=1)
                pyautogui.leftClick
                distance = 300
                while distance > 0:
                    pyautogui.dragRel(distance, 0, 0.1, button="left")
                    distance = distance - 10
                    pyautogui.dragRel(0, distance, 0.1, button="left")
                    pyautogui.dragRel(-distance, 0, 0.1, button="left")
                    distance = distance - 10
                    pyautogui.dragRel(0, -distance, 0.1, button="left")
                speak("Rectangural spiral drawn")

            elif "erase it" in query:
                pyautogui.hotkey('ctrl', 'z')
                speak("it is erase")

            elif "shutdown the system" in query:
                speak("Are you sure you want to shutdown?")
                if confirm_action("shutdown"):
                    os.system("shutdown /s /t 1")
                else:
                    speak("Shutdown canceled.")

            elif "restart the system" in query:
                speak("Are you sure you want to restart?")
                if confirm_action("restart"):
                    os.system("shutdown /r /t 5")
                else:
                    speak("Restart canceled.")

            
            elif "finally sleep" in query:
                speak("Going to sleep, sir")
                exit()    
 

if __name__ == "__main__":
    window_1()  
    thread_window_2 = threading.Thread(target=window_2)
    thread_window_2.start()
    speak("Echo initialized...")
    speak("Waiting for commands...")
    
    while True:
        query = takeCommand().lower()
        if query == "None":
            continue
        executeCommand(query)
