#pygame: computer graphics, sound libraries
#tkinter: graphical user interfaces
#filedialog: open/safe function
#askdirectory: choose directory to use
#os: functions to interact with user operating system

#import modules
import pygame
import tkinter as tkr
from tkinter.filedialog import askdirectory
import os

#create window
musicplayer = tkr.Tk()
musicplayer.title("Music Player")
musicplayer.geometry("450x350")

#choose directory containing music files
#chdir changes directory to specified path
#listbox displays list items to user
directory = askdirectory()
os.chdir(directory)
songlist = os.listdir()
playlist = tkr.Listbox(musicplayer, font ="Helvetica 12 bold", bg="yellow",selectmode= tkr.SINGLE)

for item in songlist:
    pos = 0
    playlist.insert(pos, item)
    pos = pos + 1

#pygame.mixer loads and plays sounds
pygame.init()
pygame.mixer.init()

def play():
    pygame.mixer.music.load(playlist.get(tkr.ACTIVE))
    var.set(playlist.get(tkr.ACTIVE))
    pygame.mixer.music.play()

def ExitMusicPlayer():
    pygame.mixer.music.stop()

def pause():
    pygame.mixer.music.pause()

def unpause():
    pygame.mixer.music.unpause()

Button1 = tkr.Button(musicplayer,width=5,height=3, font="Helvetica 12 bold",text="PLAY",command=play,bg="red",fg="white")
Button2 = tkr.Button(musicplayer,width=5,height=3, font="Helvetica 12 bold",text="STOP",command=ExitMusicPlayer,bg="purple",fg="white")
Button3 = tkr.Button(musicplayer,width=5,height=3, font="Helvetica 12 bold",text="PAUSE",command=pause,bg="green",fg="white")
Button4 = tkr.Button(musicplayer,width=5,height=3, font="Helvetica 12 bold",text="UNPAUSE",command=unpause,bg="blue",fg="white")

#display current songtitle
#StringVar is a class to monitor changes to tkinter variables
var = tkr.StringVar()
songtitle = tkr.Label(musicplayer, font="Helvetica 12 bold", textvariable=var)

#pack into different rows or widgets
#x fills it horizontally, y vertically
songtitle.pack()
Button1.pack(fill="x")
Button2.pack(fill="y")
Button3.pack(fill="x")
Button4.pack(fill="y")
playlist.pack(fill="both",expand="yes")

musicplayer.mainloop()
