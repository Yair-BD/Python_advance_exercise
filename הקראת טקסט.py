import pyttsx3
engine = pyttsx3.init()
engine.say("first time i'm using a package in next.py course ")
engine.runAndWait()
rate = engine.getProperty('rate')   # getting details of current speaking rate
print(rate)                        #printing current voice rate
engine.setProperty('rate', 125)