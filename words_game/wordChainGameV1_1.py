from tkinter import *
import enchant

wordlist = []
playerlist = []
dic = enchant.Dict("en_US")
desc = "Players input english words alternately.\nEach word must start with the last letter of the previous word."
error = "Not a valid word. Try again."
existerror = "Already entered. Try a new word."
english_error = "Not an english word. Try again."
copyright = "Copyright 2019 - Aamil Farooq"


class Player:

    def __init__(self, name):
        row = Frame(root)
        self.name = name

        self.count = 0
        self.lblname = Label(row, text=name, font=("Arial Bold", 15))
        self.txtbox = Entry(row, width=10, bg='yellow')
        self.txtbox.bind("<Return>", self.enter)
        self.btnOK = Button(row, text='OK', width=5, fg='black', command=self.enter, relief=RIDGE)
        self.btnpass = Button(row, text='Pass', width=5, fg='black', command=self.pass_it)
        self.txtscore = Label(row, text='0', width=3)

        row.pack(padx=5, pady=10)
        self.lblname.pack(side=LEFT)
        self.txtscore.pack(side=RIGHT)
        self.btnpass.pack(side=RIGHT)
        self.btnOK.pack(side=RIGHT)
        self.txtbox.pack(side=RIGHT)

    def get_name(self):
        return self.name

    def disable(self):
        self.txtbox.config(state=DISABLED)
        self.btnOK.config(state=DISABLED)
        self.btnpass.config(state=DISABLED)
        self.txtbox.delete(0, END)

    def enable(self):
        self.txtbox.config(state=NORMAL)
        self.btnOK.config(state=NORMAL)
        self.btnpass.config(state=NORMAL)
        self.txtbox.delete(0, END)
        self.txtbox.focus()

    def enable_next(self):
        index = playerlist.index(self)

        if index != len(playerlist)-1:
            index = index + 1
        else:
            index = 0

        player = playerlist[index]
        player.txtbox.config(state=NORMAL)
        player.txtbox.delete(0, END)
        player.txtbox.focus()
        player.btnOK.config(state=NORMAL)
        player.btnpass.config(state=NORMAL)

    def reset(self):
        self.txtscore.config(text='0')
        self.txtbox.delete(0, END)

    def get_score(self):
        return int(self.count)

    def set_score(self):
        self.count = int(self.txtscore.cget('text')) + 1
        self.txtscore.config(text=str(self.count))

    def enter(self, event=None):

        if not self.txtbox.get():
            show_error()
            self.txtbox.delete(0, END)
            return

        if not dic.check(self.txtbox.get()):
            show_error_english()
            return

        if wordlist and self.txtbox.get()[0] != wordlist[-1][-1]:
            show_error()
            return

        if self.txtbox.get() in wordlist:
            show_exist_error()
        else:
            wordlist.append(self.txtbox.get())
            self.disable()
            self.enable_next()
            self.set_score()
            show_desc()

    def pass_it(self):
        self.disable()
        self.enable_next()
        show_desc()


def on_closing_window():
    """This function is called when window is called"""
    print('Window closed')
    root.quit()
    pass


def create_window():
    global root

    root = Tk()
    w = 400
    h = 300

    ws = root.winfo_screenwidth()
    hs = root.winfo_screenheight()

    x = (ws / 2) - w / 2
    y = (hs / 2) - h / 2

    root.geometry("%dx%d+%d+%d" % (w, h, x, y))

    root.title("Word Chain Game v1.1")

    root.protocol("WM_DELETE_WINDOW", on_closing_window)
    return root


def show():
    string = ''
    for word in wordlist:
        if word != wordlist[0]:
            string = string + '--'
        string = string + word

    lbl_desc.config(text=string, fg="blue")
    #print(wordlist, sep=',')


def show_desc():
    lbl_desc.config(text=desc, fg='grey')


def show_exist_error():
    lbl_desc.config(text=existerror, fg='red')


def show_error():
    lbl_desc.config(text=error, fg='red')


def show_error_english():
    lbl_desc.config(text=english_error, fg='red')


def disable_all():
    for player in playerlist:
        player.disable()


def reset_all():
    for player in playerlist:
        player.reset()
    wordlist.clear()


def end_game():
    disable_all()
    btn_start.config(text='Start')
    if len(wordlist) == 0:
        return

    score_list = []
    for player in playerlist:
        score_list.append(player.get_score())

    m = max(score_list)
    max_score_pos_list = [i for i, j in enumerate(score_list) if j == m]
    if len(max_score_pos_list) > 1:
        set_desc_label("It's a TIE!")
    else:
        name = playerlist[max_score_pos_list[0]].get_name()
        set_desc_label("%s is the WINNER!" % name)

    print(max_score_pos_list)


def start():
    disable_all()
    reset_all()
    show_desc()
    playerlist[0].enable()
    btn_start.config(text='Reset')


def set_desc_label(msg):
    lbl_desc.config(text=msg, fg='purple1')
    pass


def add_player(name):
    playerlist.append(Player(name))


def create_buttons():
    global btn_start

    row = Frame(root)
    btn_quit = Button(row, text='Quit', width=5, fg="black", command=root.quit)
    btn_end = Button(row, text='End Game', width=10, fg="black", command=end_game)
    btn_show = Button(row, text='History', width=10, fg="black", command=show)
    btn_start = Button(row, text='Start', width=5, fg="black", command=start)
    row.pack(side=TOP, padx=5, pady=5)
    btn_quit.pack(side=RIGHT)
    btn_end.pack(side=RIGHT)
    btn_start.pack(side=LEFT)
    btn_show.pack(side=LEFT)


def create_desc_label():
    global lbl_desc

    row = Frame(root)
    lbl_desc = Label(row, text=desc, fg="grey", width=100, height=40, wraplength=300, justify=LEFT)
    lbl_desc.config(font=('Helvetica', '15', 'bold'))
    row.pack(side=TOP, padx=5)
    lbl_desc.pack(side=LEFT)


def create_copyright_label():
    row = Frame(root)
    lbl_top = Label(row, text=copyright, fg='blue', width=40, justify=CENTER)
    row.pack(side=TOP, padx=5, pady=5)
    lbl_top.pack(side=LEFT)


def main():

    create_window()

    create_copyright_label()

    add_player("Zaahida")
    add_player('Khubaib')
    #add_player('Aamil')

    disable_all()

    create_buttons()

    create_desc_label()


if __name__ == '__main__':
    main()
    mainloop()

