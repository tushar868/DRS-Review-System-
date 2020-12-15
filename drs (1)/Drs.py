# All media file is available for download as a zip file (See description)
import tkinter
from tkinter import Label, Tk
from tkinter.constants import CENTER 
import cv2 # pip install opencv-python
import PIL.Image, PIL.ImageTk # pip install pillow
from functools import partial
import threading
import time
import imutils # pip install imutil
import speech_recognition as sr
import pyttsx3
import tkinter.messagebox
from playsound import playsound
import webbrowser

#from convenience import translate
import numpy as np

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[1].id)
engine.setProperty('voice',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


flag = True
def play(speed):
    global flag
    print(f"You clicked on play. Speed is {speed}")
    
    

    # Play the video in reverse mode
    
    frame1 =cv1.get(cv2.CAP_PROP_POS_FRAMES)
    cv1.set(cv2.CAP_PROP_POS_FRAMES, frame1 + speed)

    grabbed, frame = cv1.read()
    if not grabbed:
        exit()
    frame = imutils.resize(frame, width=SET_WIDTH, height=SET_HEIGHT)
    frame = PIL.ImageTk.PhotoImage(image = PIL.Image.fromarray(frame))
    canvas.image = frame
    canvas.create_image(0,0, image=frame, anchor=tkinter.NW)
    if flag:
        canvas.create_text(134, 26, fill="black", font="Times 26 bold", text="Decision Pending")
        
    flag = not flag
    

def pending(decision):
    # 1. Display decision pending image
    frame = cv2.cvtColor(cv2.imread("D:\\drs (1)\\pending.png"), cv2.COLOR_BGR2RGB)
    frame = imutils.resize(frame, width=SET_WIDTH, height=SET_HEIGHT)
    frame = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
    canvas.image = frame
    canvas.create_image(0,0, image=frame, anchor=tkinter.NW)
    # 2. Wait for 1 second
    time.sleep(1)
    speak('Decision Pending')

    # 3. Display sponsor image
    frame = cv2.cvtColor(cv2.imread("D:\\drs (1)\\sponsor.png"), cv2.COLOR_BGR2RGB)
    frame = imutils.resize(frame, width=SET_WIDTH, height=SET_HEIGHT)
    frame = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
    canvas.image = frame
    canvas.create_image(0,0, image=frame, anchor=tkinter.NW)

    # 4. Wait for 1.5 second
    time.sleep(1)
    # 5. Display out/notout image
    if decision == 'out':
        decisionImg = "D:\\drs (1)\\out.png"
        speak("Player is out")
        playsound('D:\\drs (1)\\s.mp3')
    else:
        decisionImg = "D:\\drs (1)\\not_out.png"
        speak("Player is not out")
        playsound('D:\\drs (1)\\s.mp3')

    frame = cv2.cvtColor(cv2.imread(decisionImg), cv2.COLOR_BGR2RGB)
    frame = imutils.resize(frame, width=SET_WIDTH, height=SET_HEIGHT)
    frame = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
    canvas.image = frame
    canvas.create_image(0,0, image=frame, anchor=tkinter.NW)


def out():
    thread = threading.Thread(target=pending, args=("out",))
    thread.daemon = 1
    thread.start()
    print("Player is out")
    


def not_out():
    thread = threading.Thread(target=pending, args=("not out",))
    thread.daemon = 1
    thread.start()
    print("Player is not out")
    

# Width and height of our main screen
SET_WIDTH = 625
SET_HEIGHT = 300

# Tkinter gui starts here
#root =Tk()
#root.geometry("1500x1000")
window = tkinter.Tk()
window.configure(background='#34495E')
window.title("Third Umpire Decision Review Kit")
cv1 = cv2.VideoCapture("D:\drs (1)\\clip.mp4")

cv = cv2.cvtColor(cv2.imread("D:\\drs (1)\\IPL Teams.png"), cv2.COLOR_BGR2RGB)
canvas = tkinter.Canvas(window, width=SET_WIDTH, height=SET_HEIGHT)
photo = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(cv))
image_on_canvas = canvas.create_image(0, 0, ancho=tkinter.NW, image=photo)
canvas.pack()




# Buttons to control playback
btn = tkinter.Button(window, text="<< Previous (fast)",bg='Black', fg='Dark Orange', width=50, command=partial(play, -25))
btn.pack()

btn = tkinter.Button(window, text="<< Previous (slow)",bg='Black', fg='Dark Orange', width=50, command=partial(play, -2))
btn.pack()

btn = tkinter.Button(window, text="Next (slow) >>",bg='Black', fg='Dark Orange', width=50, command=partial(play, 2))
btn.pack()

btn = tkinter.Button(window, text="Next (fast) >>",bg='Black', fg='Dark Orange', width=50, command=partial(play, 25))
btn.pack()

btn = tkinter.Button(window, text="Give Out",bg='Black', fg='Red', width=50, command=out)
btn.pack()

btn = tkinter.Button(window, text="Give Not Out",bg='Black', fg='Light Green', width=50, command=not_out)
btn.pack()
window.mainloop()
