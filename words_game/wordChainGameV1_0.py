from tkinter import *
import enchant

wordlist = []
dic = enchant.Dict("en_US")
desc = "Players input english words alternately. Each word must start with the last letter of the previous word."
error = "Not a valid word. Try again."
existerror = "Already entered. Try a new word."


def pass1():
    e1.config(state=DISABLED)
    e2.config(state=NORMAL)
    e2.focus_set()
    b1.config(state=DISABLED)
    b2.config(state=NORMAL)
    btnpass1.config(state=DISABLED)
    btnpass2.config(state=NORMAL)


def pass2():
    e1.config(state=NORMAL)
    e2.config(state=DISABLED)
    e1.focus_set()
    b1.config(state=NORMAL)
    b2.config(state=DISABLED)
    btnpass1.config(state=NORMAL)
    btnpass2.config(state=DISABLED)


def check_and_enter1():
    if not e1.get() or not dic.check(e1.get()):
        lbl.config(text=error, fg='red')
        e1.delete(0, END)
        return

    if wordlist and e1.get()[0] != wordlist[-1][-1]:
        lbl.config(text=error, fg='red')
        e1.delete(0, END)
        return

    if e1.get() in wordlist:
        lbl.config(text=existerror, fg='red')
    else:
        wordlist.append(e1.get())
        e1.config(state=DISABLED)
        e2.config(state=NORMAL)
        b1.config(state=DISABLED)
        b2.config(state=NORMAL)
        e2.delete(0, END)
        e2.focus_set()
        lbl.config(text=desc, fg="grey")


def check_and_enter2():
    if not e2.get() or not dic.check(e2.get()):
        lbl.config(text=error, fg='red')
        e2.delete(0, END)
        return

    if wordlist and e2.get()[0] != wordlist[-1][-1]:
        lbl.config(text=error, fg='red')
        e2.delete(0, END)
        return

    if e2.get() in wordlist:
        lbl.config(text=existerror, fg='red')
    else:
        wordlist.append(e2.get())
        e1.config(state=NORMAL)
        e2.config(state=DISABLED)
        b2.config(state=DISABLED)
        b1.config(state=NORMAL)
        e1.delete(0, END)
        e1.focus_set()
        lbl.config(text=desc, fg="grey")


def show():
    lbl.config(text=wordlist, fg="green")
    print(wordlist)


def end_game():
    e1.config(state=DISABLED)
    e2.config(state=DISABLED)
    b1.config(state=DISABLED)
    b2.config(state=DISABLED)
    btnpass1.config(state=DISABLED)
    btnpass2.config(state=DISABLED)
    pass


def start():
    e1.config(state=NORMAL)
    b1.config(state=NORMAL)
    btnpass1.config(state=NORMAL)


root = Tk()
w = 400
h = 300

ws = root.winfo_screenwidth()
hs = root.winfo_screenheight()

x = (ws/2) - w/2
y = (hs/2) - h/2

root.geometry("%dx%d+%d+%d" % (w, h, x, y))

root.title("Word Chain Game v1.0")

row = Frame(root)

lbl1 = Label(row, text="Zaahida", font=("Arial Bold", 15))
e1 = Entry(row, width=10, bg='cyan')
b1 = Button(row, text='OK', width=5, highlightbackground="blue", fg="orange", command=check_and_enter1)
btnpass1 = Button(row, bg="black", text='Pass', width=5, highlightbackground="blue", fg="orange", command=pass1)
timer1 = Label(row, fg="green")
#row.place(anchor=CENTER)
row.pack(anchor=CENTER, fill=X, padx=10, pady=5)
lbl1.pack(side=LEFT)
#timer1.pack(RIGHT)
btnpass1.pack(side=RIGHT)
b1.pack(side=RIGHT)
e1.pack(side=RIGHT)

row = Frame(root)

lbl2 = Label(row, text="Khubaib", font=("Arial Bold", 15))
e2 = Entry(row, width=10, bg='cyan', state=DISABLED)
b2 = Button(row, text='OK', width=5, highlightbackground="blue", fg="orange", command=check_and_enter2, state=DISABLED)
btnpass2 = Button(row, text='Pass', width=5, highlightbackground="blue", fg="orange", command=pass2, state=DISABLED)
timer2 = Label(row, fg="green")
row.pack(side=TOP, fill=X, padx=10, pady=5)
lbl2.pack(side=LEFT)
#timer2.pack(RIGHT)
btnpass2.pack(side=RIGHT)
b2.pack(side=RIGHT)
e2.pack(side=RIGHT)

row = Frame(root)
btnquit = Button(row, text='Quit', width=5, highlightbackground='#3E4149', fg="orange", command=root.quit)
btnend = Button(row, text='End Game', width=10, highlightbackground='#3E4149', fg="orange", command=end_game)
btnshow = Button(row, text='History', width=10, highlightbackground='#3E4149', fg="orange", command=show)
btnstart = Button(row, text='Start', width=5, highlightbackground='#3E4149', fg="orange", command=start)
row.pack(side=TOP, fill=X, padx=10, pady=5)
btnquit.pack(side=RIGHT)
btnend.pack(side=RIGHT)
btnstart.pack(side=LEFT)
btnshow.pack(side=LEFT)

row = Frame(root)
lbl = Label(row, text=desc, fg="grey", width=40, height=10, wraplength=250, justify=LEFT)
row.pack(side=TOP, fill=X, padx=10, pady=5)
lbl.pack(side=LEFT)

"""
lbl1 = Label(root, text="Zaahida", font=("Arial Bold", 15))
lbl2 = Label(root, text="Khubaib", font=("Arial Bold", 15))
lbl1.grid(row=0)
lbl2.grid(row=1)

e1 = Entry(root)
e2 = Entry(root)

e1.grid(row=0, column=1)
e2.grid(row=1, column=1)

b1 = Button(root, bg="black", text='OK', command=check_and_enter1)
b2 = Button(root, bg="black", text='OK', command=check_and_enter2)
b1.grid(row=0, column=2, sticky=W, pady=4)
b2.grid(row=1, column=2, sticky=W, pady=4)

btnquit = Button(root, text='Quit', bg="black", fg="blue", command=root.quit)
btnshow = Button(root, text='Show', bg="black", fg="blue", command=show)
btnquit.grid(row=3, column=0, sticky=W, pady=4)
btnshow.grid(row=3, column=1, sticky=W, pady=4)

lbl = Label(root, text="Result")
lbl.grid(row=4)
"""
mainloop()
