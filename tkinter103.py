from tkinter import *
from tkinter.messagebox import showinfo

def reply(name):
    showinfo(title='Reply', message='Hello %s!' % name)
    
    
top = Tk()
top.title('Echo')
#top.iconbitmap('py-blue-trans-out.ico')
Label(top, text='Enter your name:').pack(side=TOP)
#Label(top, text='second line').pack(side=TOP)
ent = Entry(top)
Label(top, text='second line').pack(side=LEFT)
ent2 = Entry(top)

ent.pack(side=TOP)
ent2.pack(side=TOP)
btn = Button(top, text='Submit', command=(lambda: reply(ent.get())))
btn.pack(side=BOTTOM)
top.mainloop()