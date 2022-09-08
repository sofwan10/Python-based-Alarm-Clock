import datetime   
import pywhatkit    #from playsound import playsound --> you guys can use this code if you guys wanted to use sound from your device
alarmHour = int(input("Enter Hour:  "))
alarmMinute = int(input("Enter Minute:  "))
alarmAm = input("am / pm:   ")

if alarmAm =="pm":
    alarmHour+=12

while True:
    if alarmHour == datetime.datetime.now().hour and alarmMinute == datetime.datetime.now().minute:
        print("Wake Up!! Don't be lazy! We are GIGACHAD!!!")
        pywhatkit.playonyt("https://www.youtube.com/watch?v=Hh5jEQraXaw")
        break