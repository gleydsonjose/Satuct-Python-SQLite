from tkinter import *


class Instructions:
    def __init__(self):
        self.instructions()

    def instructions(self):
        # Instructions window
        instructions_window = Toplevel()

        # Information 1
        instructions_info1 = Label(instructions_window,
                                   text='1- When the program starts for first time, type something in the text fields and\n'
                                        '     click Calculate to create a database on your computer, close the program\n'
                                        'and open again', bg='#e8e8e8', fg='#4f4f4f')
        instructions_info1.place(x=15, y=14)

        # Information 2
        instructions_info2 = Label(instructions_window,
                                   text='2- From the moment the program starts, click the Update button to show the\n'
                                        'data in the lists', bg='#e8e8e8', fg='#4f4f4f')
        instructions_info2.place(x=15, y=70)

        # Information 3
        instructions_info3 = Label(instructions_window,
                                   text='3- When deleting an item from the list, choose by ID and then click the button\n'
                                        'Delete', bg='#e8e8e8', fg='#4f4f4f')
        instructions_info3.place(x=15, y=112)

        # Information 4
        instructions_info4 = Label(instructions_window,
                                   text='4- Whenever you delete or add an item, click the Update button',
                                   bg='#e8e8e8', fg='#4f4f4f')
        instructions_info4.place(x=15, y=153)

        # Instructions window settings
        instructions_icon = PhotoImage(file='images\logo.png')
        instructions_window.resizable(False, False)
        instructions_window.tk.call('wm', 'iconphoto', instructions_window._w, instructions_icon)
        instructions_window.title('SATUCT - Instructions')
        instructions_window['bg'] = '#e8e8e8'
        instructions_window.geometry('450x191')