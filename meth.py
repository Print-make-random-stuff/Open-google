import pyautogui
from tkinter import *
import time
import os
import webbrowser
root = Tk()
root.geometry('300x200')
root.resizable(width=False, height=False)
root.title('open youtube')
root.iconbitmap("C:\\Users\\pc\\Pictures\\Free times\\Tur.ico.ico")





o =  "C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"

def open_youtube():
    webbrowser.open(o)
    pyautogui.press('/',interval=1)
    pyautogui.write('youtube.com')
    pyautogui.press('Enter')


But = Button(text='open_youtube ?', padx = 50,pady=100, bg="blue" , fg="white")
But.pack(side=LEFT)

Bot = Button(text='Go', padx =70,pady=60,bg='yellow',command=open_youtube)
Bot.pack()

bye = Button(text='Esc',padx=50,pady=50,command=exit)
bye.pack()

root.mainloop()
