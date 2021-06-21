import pyttsx3
from gtts import gTTS
from tkinter import *
import os

speaker=pyttsx3.init()


def talk(text):
    speaker.say(text)
    speaker.runAndWait()

def tts():
    txt=(e1.get())
    str(txt)
    talk(txt)

root=Tk()
a=StringVar()
root.title("Text to speech")
root.configure(bg="grey")
width= root.winfo_screenwidth()
height= root.winfo_screenheight()
root.geometry("%dx%d" % (width, height))

l1=Label(root,text="Text to speech",font=("chiller",40,"bold"),bg="lightgreen")
l2=Label(root,text="made by atul Sharma",font=("Monaco",14,"italic"),bg="lightgreen")
l3=Label(root,text="Enter text-:",font=("Timesnewroman",40,"bold"),bg="lightgreen")

l1.place(x=600,y=100)
l2.place(x=600,y=600)
l3.place(x=5,y=300)

e1=Entry(root,bg="lightyellow",width=30,font=("arial",40,"bold"),selectbackground="red")
e1.place(x=300,y=300)

#  function for downloading
def download():
    language = "en"
    myobj = gTTS(text=e1.get(),
                 lang=language,
                 slow=False)
    myobj.save("convert.wav")
    os.system("convert.wav")


b1=Button(root,text="click to Talk",height=7,width=30,bd=5,cursor="spider",font=("Georgia",8)
          ,activeforeground="green",activebackground="red",command=tts)
b2=Button(root,text="click to download",height=7,width=30,bd=5,cursor="spider",font=("Georgia",8)
          ,activeforeground="green",activebackground="red",command=download)


b1.place(x=600,y=400)
b2.place(x=850,y=400)

root.mainloop()

