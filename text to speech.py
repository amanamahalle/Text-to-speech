import tkinter as tk
from tkinter import *
from tkinter import filedialog
from tkinter.ttk import Combobox  # Corrected the import to tkinter.ttk
import pyttsx3
import os

# Initialize root window
root = Tk()  # Use 'Tk', not 'TK'
root.title("Text to Speech")
root.geometry("900x450+200+200")  # Corrected '*' to 'x' for dimensions
root.resizable(False, False)  # Corrected 'rootresizable' to 'root.resizable'
root.configure(bg="#305065")

# Initialize text-to-speech engine
engine = pyttsx3.init()

def speaknow():
    text = text_area.get(1.0, END)
    gender = gender_combobox.get()
    speed = speed_combobox.get()
    voices = engine.getProperty('voices')

    def setvoice():
        if gender == 'Male':
            engine.setProperty('voice', voices[0].id)
        else:
            engine.setProperty('voice', voices[1].id)
        engine.say(text)
        engine.runAndWait()

    if text.strip():  # Check if the text is not empty
        if speed == "Fast":
            engine.setProperty('rate', 250)
        elif speed == 'Normal':
            engine.setProperty('rate', 150)
        else:
            engine.setProperty('rate', 60)
        setvoice()

def download():
    text = text_area.get(1.0, END)
    gender = gender_combobox.get()
    speed = speed_combobox.get()
    voices = engine.getProperty('voices')

    def setvoice():
        if gender == 'Male':
            engine.setProperty('voice', voices[0].id)
        else:
            engine.setProperty('voice', voices[1].id)

        path = filedialog.askdirectory()  # Ask user to select a directory
        if path:
            os.chdir(path)
            engine.save_to_file(text, 'text.mp3')
            engine.runAndWait()

    if text.strip():  # Check if the text is not empty
        if speed == "Fast":
            engine.setProperty('rate', 250)
        elif speed == 'Normal':
            engine.setProperty('rate', 150)
        else:
            engine.setProperty('rate', 60)
        setvoice()

# Icon
image_icon = PhotoImage(file="speak.png")  # Corrected 'photoimag' to 'PhotoImage'
root.iconphoto(False, image_icon)

# Top Frame
Top_frame = Frame(root, bg="white", width=900, height=100)
Top_frame.place(x=0, y=0)

logo = PhotoImage(file="speaker logo.png")  # Ensure the file name is correct
Label(Top_frame, image=logo, bg="white").place(x=10, y=5)

Label(Top_frame, text="TEXT TO SPEECH", font="arial 20 bold", bg="white", fg="black").place(x=100, y=30)

# Text Area
text_area = Text(root, font="Roboto 20", bg="white", relief=GROOVE, wrap=WORD)  # Corrected 'text_areaText'
text_area.place(x=10, y=150, width=500, height=250)

# Labels
Label(root, text="VOICE", font="arial 15 bold", bg="#305065", fg="white").place(x=580, y=160)
Label(root, text="SPEED", font="arial 15 bold", bg="#305065", fg="white").place(x=760, y=160)

# Gender Combobox
gender_combobox = Combobox(root, values=['Male', 'Female'], font="arial 14", state='r', width=10)
gender_combobox.place(x=550, y=200)
gender_combobox.set('Male')

# Speed Combobox
speed_combobox = Combobox(root, values=['Fast', 'Normal', 'Slow'], font="arial 14", state='r', width=10)
speed_combobox.place(x=730, y=200)
speed_combobox.set('Normal')

# Speak Button
imageicon = PhotoImage(file="speak.png")  # Ensure the image path is correct
btn = Button(root, text="Speak", compound=LEFT, image=imageicon, padx=10, pady=10,bg="#39c790", font="arial 14 bold", command=speaknow)
btn.place(x=550, y=280, width=130, height=60)

# Save Button
imageicon2 = PhotoImage(file="download.png")  # Ensure the image path is correct
save = Button(root, text="Save", compound=LEFT, image=imageicon2, padx=10, pady=10, bg="#39c790", font="arial 14 bold", command=download)
save.place(x=730, y=280, width=130, height=60)  # Adjusted position to avoid overlapping with the speak button

# Main loop
root.mainloop()