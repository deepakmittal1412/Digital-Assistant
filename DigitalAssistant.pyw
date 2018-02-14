import wolframalpha
import wikipedia
from tkinter import *


def display(event):
    try:
        client = wolframalpha.Client("8EAEY4-7GTLWY84VY")
        res = client.query(ent.get())
        ans = next(res.results).text
    except:
        ans = wikipedia.summary(ent.get(), sentences=2)
    finally:
        win = Tk()
        win.title("Digital Assistant")
        win.resizable(0, 0)
        win.propagate()
        win.minsize(width=400, height=150)
        win.config(bg='peach puff')
        Label(win, text=ans, bg='peach puff').pack(expand=YES, fill=BOTH)
        win.mainloop()


root = Tk()
root.title("Digital Assistant")
root.resizable(0, 0)
root.propagate()
root.minsize(width=400, height=150)
root.config(bg='peach puff')
l = Label(root, text="How may i assist you ?\nEnter below", bg='light yellow', font=('Helvetica', 20, 'italic')).pack(
    expand=YES)
ent = Entry(root, bd=5, relief=SOLID)
ent.insert(0, '')
ent.bind('<Return>', display)
ent.pack(expand=YES, fill=X)

root.mainloop()
