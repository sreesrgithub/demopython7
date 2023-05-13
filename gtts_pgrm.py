from gtts import gTTS
import os
from tkinter import *

root = Tk()

canvas = Canvas(root, width=400, height=300)
canvas.pack()


def textspeech():
    text = entry.get()
    output = gTTS(text=text, lang='en', slow=False)
    output.save('output.mp3')
    os.system('start output.mp3')


entry = Entry(root)
canvas.create_window(200, 180, window=entry)
button = Button(root, text="Start", command=textspeech)
canvas.create_window(200, 230, window=button)
root.mainloop()

# text=open('demo.txt','r',encoding='utf-8').read()
