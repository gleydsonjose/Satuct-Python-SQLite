from tkinter import *
from os import path
import sqlite3
from windows.currency_converter import CurrencyConverter
from windows.alert import Alert
from windows.instructions import Instructions


class MainProgram:
    def __init__(self):

        # Creating a connection with sqlite
        self.connection = sqlite3.connect('db/items.db')
        self.cursor = self.connection.cursor()

        # Capturing database file size
        self.sizebd = path.getsize('db/items.db')

        # Creating widgets for main program window
        self.create_window_and_widgets_mp()

    # If id list scrolls, all lists will scroll together in vertical
    def yscroll_id_list(self, *args):
        if self.id_list.yview() != self.i_list.yview() and self.id_list.yview() != self.op_list.yview()\
                and self.id_list.yview() != self.np_list.yview():
            self.i_list.yview_moveto(args[0])
            self.op_list.yview_moveto(args[0])
            self.np_list.yview_moveto(args[0])
            self.scrollbar.set(*args)

    # If item list scrolls, all lists will scroll together in vertical
    def yscroll_i_list(self, *args):
        if self.i_list.yview() != self.id_list.yview() and self.i_list.yview() != self.op_list.yview()\
                and self.i_list.yview() != self.np_list.yview():
            self.id_list.yview_moveto(args[0])
            self.op_list.yview_moveto(args[0])
            self.np_list.yview_moveto(args[0])
            self.scrollbar.set(*args)

    # If old price list scrolls, all lists will scroll together in vertical
    def yscroll_op_list(self, *args):
        if self.op_list.yview() != self.id_list.yview() and self.op_list.yview() != self.i_list.yview()\
                and self.op_list.yview() != self.np_list.yview():
            self.id_list.yview_moveto(args[0])
            self.i_list.yview_moveto(args[0])
            self.np_list.yview_moveto(args[0])
            self.scrollbar.set(*args)

    # If new price list scrolls, all lists will scroll together in vertical
    def yscroll_np_list(self, *args):
        if self.np_list.yview() != self.id_list.yview() and self.np_list.yview() != self.i_list.yview()\
                and self.np_list.yview() != self.op_list.yview():
            self.id_list.yview_moveto(args[0])
            self.i_list.yview_moveto(args[0])
            self.op_list.yview_moveto(args[0])
            self.scrollbar.set(*args)

    # Scrolling all lists together in vertical
    def yscroll_all_lists(self, *args):
        self.id_list.yview(*args)
        self.i_list.yview(*args)
        self.op_list.yview(*args)
        self.np_list.yview(*args)

    def delete_item(self):
        # Deleting item by id
        for i in self.id_list.get(ANCHOR):
            # Success alert
            n = Alert()
            n.alert('Item deleted successfully', '#2b97dc', 57, 40, 93, 85, '252x147+410+320')

            # Deleting
            sql = f'DELETE FROM Items WHERE id = {i}'
            self.cursor.execute(sql)
            self.connection.commit()

        # Alert by trying to delete using another list
        if self.i_list.curselection() or self.op_list.curselection() or self.np_list.curselection():
            n = Alert()
            n.alert('For delete an item, use ID list', '#2b97dc', 40, 40, 88, 85, '240x147+410+320')

    def updatelist(self):
        # Clearing the lists
        self.id_list.delete(0, END)
        self.i_list.delete(0, END)
        self.op_list.delete(0, END)
        self.np_list.delete(0, END)

        # Checking if database file size is bigger than 0
        if self.sizebd > 0:

            try:
                # Selecting id column to appear in id_list
                sql = 'SELECT id FROM Items'
                self.cursor.execute(sql)
                ids = self.cursor.fetchall()
                for i in ids:
                    self.id_list.insert(END, i)
            except:
                # Error alert
                n = Alert()
                n.alert('ERROR ID List: There was a problem while attempting to\n'
                         ' acess the id column', '#ff0000', 26, 35, 144, 90, '353x150+355+320')

            try:
                # Selecting item column to appear in item_list
                sql = 'SELECT item FROM Items'
                self.cursor.execute(sql)
                item = self.cursor.fetchall()
                for it in item:
                    for i in it:
                        self.i_list.insert(END, i)
            except:
                # Error alert
                n = Alert()
                n.alert('ERROR Items List: There was a problem while attempting to\n'
                         ' acess the item column', '#ff0000', 27, 35, 153, 90, '372x150+346+320')

            try:
                # Selecting oldprices column to appear in oldprice_list
                sql = 'SELECT oldprice FROM Items'
                self.cursor.execute(sql)
                oldprices = self.cursor.fetchall()
                for op in oldprices:
                    for o in op:
                        self.op_list.insert(END, o)
            except:
                # Error alert
                n = Alert()
                n.alert('ERROR Old Price List: There was a problem while attempting to\n'
                         ' acess the oldprice column', '#ff0000', 26, 35, 163, 90, '390x150+328+320')

            try:
                # Selecting newprices column to appear in newprice_list
                sql = 'SELECT newprice FROM Items'
                self.cursor.execute(sql)
                newprice = self.cursor.fetchall()
                for np in newprice:
                    for n in np:
                        self.np_list.insert(END, n)
            except:
                # Error alert
                n = Alert()
                n.alert('ERROR New Price List: There was a problem while attempting to\n'
                         ' acess the newprice column', '#ff0000', 26, 35, 166, 90, '395x150+328+320')
        else:
            # Error alert
            n = Alert()
            n.alert('ERROR Database: The DB has not yet been created, type information\n'
                     ' in the text fields, and click Calculate to create a DB, then close the\n'
                     ' program and reopen', '#ff0000', 27, 32, 177, 105, '417x168+315+320')

    def calculation(self):
        # Calculation variables
        global value, perc, symbol, old_price, new_price
        price = self.price.get()
        percentage = self.percentage.get()
        item = self.item.get().strip()

        # Checking if text fields don't are empty
        if len(price) > 0 and len(percentage) > 0 and len(item) > 0:

            try:
                # Capturing item value
                value = float(price.replace(',', '.').strip())
            except:
                # Error alert
                n = Alert()
                n.alert('ERROR Price: Enter a valid value', '#ff0000', 41, 38, 96, 86, '256x150+410+320')

            try:
                # Capturing percentage value
                perc = int(percentage.strip())
            except:
                # Error alert
                n = Alert()
                n.alert('ERROR Percentage: Enter an integer value', '#ff0000', 37, 38, 118, 86, '300x150+410+320')

            # Currency
            if self.c_var.get() in 'Real':
                symbol = 'R$'
            elif self.c_var.get() in 'Dollar':
                symbol = 'US$'
            elif self.c_var.get() in 'Euro':
                symbol = '€'

            # Increase and discount
            if self.inc_dis.get() == 1:
                increase = value + (value * perc / 100)
                old_price = f'{symbol}{value:.2f}'
                new_price = f'{symbol}{increase:.2f}'

            elif self.inc_dis.get() == 2:
                discount = value - (value * perc / 100)
                old_price = f'{symbol}{value:.2f}'
                new_price = f'{symbol}{discount:.2f}'

            try:
                # Inserting data in Items table
                sql = f"INSERT INTO Items (item, oldprice, newprice) VALUES('{item}','{old_price}','{new_price}')"
                self.cursor.execute(sql)
                self.connection.commit()

                # Success alert
                n = Alert()
                n.alert('Item successfully added', '#2b97dc', 58, 40, 93, 85, '250x147+410+320')
            except:
                # Creating a new table
                sql = 'CREATE TABLE IF NOT EXISTS Items (id INTEGER PRIMARY KEY ' \
                      'AUTOINCREMENT, item VARCHAR(200), oldprice VARCHAR(200), newprice VARCHAR(200))'
                self.cursor.execute(sql)

                # Success alert
                n = Alert()
                n.alert('Database created successfully! Close the program and reopen', '#2b97dc',
                         26, 32, 160, 80, '383x140+320+320')

        else:
            # Error alert
            n = Alert()
            n.alert('ERROR: Empty text field', '#ff0000', 59, 40, 93, 85, '250x150+410+320')

        # Cleaning text fields
        self.item.delete(0, END)
        self.price.delete(0, END)
        self.percentage.delete(0, END)

    def create_window_and_widgets_mp(self):
        # Main window
        window = Tk()

        # Program title
        program_title = Label(window, text='SATUCT', font=('Impact', 13), bg='#4f4f4f', fg='#2b97dc', width=90,
                              height=3)
        program_title.place(x=0, y=0)

        # Title image.
        title_image = PhotoImage(file='images\\logo.png')
        bg_image = Label(window, image=title_image, bg='#4f4f4f')
        bg_image.image = title_image
        bg_image.place(x=279, y=4)

        # Item name
        item_name = Label(window, text='Item name:', bg='#e8e8e8', fg='#4f4f4f')
        item_name.place(x=10, y=120)
        self.item = Entry(window, width=20, borderwidth=1, relief='groove')
        self.item.place(x=13, y=143)

        # Price
        price_name = Label(window, text='Price:', bg='#e8e8e8', fg='#4f4f4f')
        price_name.place(x=10, y=168)
        self.price = Entry(window, width=20, borderwidth=1, relief='groove')
        self.price.place(x=13, y=189)

        # Percentage
        percentage_name = Label(window, text='Percentage:', bg='#e8e8e8', fg='#4f4f4f')
        percentage_name.place(x=10, y=216)
        self.percentage = Entry(window, width=20, borderwidth=1, relief='groove')
        self.percentage.place(x=13, y=237)

        # Currency
        c_name = Label(window, text='Currency:', bg='#e8e8e8', fg='#4f4f4f')
        c_name.place(x=10, y=264)
        c_list = ['Real', 'Dollar', 'Euro']
        self.c_var = StringVar(window)
        self.c_var.set(c_list[0])
        c_option = OptionMenu(window, self.c_var, *c_list)
        c_option.config(borderwidth=1, relief='flat', bg='#4f4f4f', activebackground='#616161', fg='#e8e8e8',
                        activeforeground='#e8e8e8')
        c_option.place(x=12, y=285)

        # Increase and discount
        self.inc_dis = IntVar(window)
        self.inc_dis.set(1)
        inc_rb = Radiobutton(window, text='Increase', value=1, variable=self.inc_dis)
        inc_rb.config(bg='#e8e8e8', activebackground='#e8e8e8', fg='#4f4f4f', activeforeground='#4f4f4f')
        inc_rb.place(x=10, y=325)
        dis_rb = Radiobutton(window, text='Discount', value=2, variable=self.inc_dis)
        dis_rb.config(bg='#e8e8e8', activebackground='#e8e8e8', fg='#4f4f4f', activeforeground='#4f4f4f')
        dis_rb.place(x=10, y=350)

        # Currency converter button
        cc_btn = Button(window, text='Currency Converter', command=CurrencyConverter)
        cc_btn.config(bg='#4f4f4f', activebackground='#616161', fg='#e8e8e8', activeforeground='#e8e8e8',
                      borderwidth=1, relief='flat', width=17, font=('arial', 9))
        cc_btn.place(x=436, y=83)

        # Instructions button
        self.i_btn = Button(window, text='Instructions', command=Instructions)
        self.i_btn.config(bg='#4f4f4f', activebackground='#616161', fg='#e8e8e8', activeforeground='#e8e8e8',
                     borderwidth=1, relief='flat', width=11, font=('arial', 9))
        self.i_btn.place(x=577, y=83)

        # Calculate button
        calc_btn = Button(window, text='Calculate', command=self.calculation)
        calc_btn.config(bg='#4f4f4f', activebackground='#616161', fg='#e8e8e8', activeforeground='#e8e8e8',
                        borderwidth=1, relief='flat', width=10, font=('arial', 9))
        calc_btn.place(x=15, y=390)

        # Delete button
        del_btn = Button(window, text='Delete', command=self.delete_item)
        del_btn.config(bg='#4f4f4f', activebackground='#616161', fg='#e8e8e8', activeforeground='#e8e8e8',
                       borderwidth=1, relief='flat', width=10, font=('arial', 9))
        del_btn.place(x=15, y=425)

        # Update button
        upd_btn = Button(window, text='Update', command=self.updatelist)
        upd_btn.config(bg='#4f4f4f', activebackground='#616161', fg='#e8e8e8', activeforeground='#e8e8e8',
                       borderwidth=1, relief='flat', width=10, font=('arial', 9))
        upd_btn.place(x=15, y=460)

        # Frame for scrollbar
        scrollbar_frame = Frame(window)
        scrollbar_frame.place(x=646, y=121)

        # Scrollbar for lists
        self.scrollbar = Scrollbar(scrollbar_frame, orient='vertical', command=self.yscroll_all_lists)
        self.scrollbar.grid(ipady=155)

        # ID list
        id_title_list = Label(window, text='ID', bg='#4f4f4f', fg='#e8e8e8', width=6, borderwidth=2,
                              relief='flat', font=('arial', 9))
        id_title_list.place(x=170, y=121)
        self.id_list = Listbox(window, selectmode=SINGLE, bg='#4f4f4f', fg='#e8e8e8', borderwidth=2,
                               relief='flat', width=7, height=21, activestyle='none', highlightthickness=0,
                               yscrollcommand=self.yscroll_id_list)
        self.id_list.place(x=170, y=142)

        # Item list
        i_title_list = Label(window, text='Item', bg='#4f4f4f', fg='#e8e8e8', width=21, borderwidth=2,
                             relief='flat', font=('arial', 9))
        i_title_list.place(x=218, y=121)
        self.i_list = Listbox(window, selectmode=SINGLE, borderwidth=2, relief='flat', width=26, height=21,
                              activestyle='none', highlightthickness=0, yscrollcommand=self.yscroll_i_list)
        self.i_list.place(x=215, y=142)

        # Old price list
        op_title_list = Label(window, text='Old Price', bg='#4f4f4f', fg='#e8e8e8', width=19, borderwidth=2,
                              relief='flat', font=('arial', 9))
        op_title_list.place(x=371, y=121)
        self.op_list = Listbox(window, selectmode=SINGLE, borderwidth=2, relief='flat', width=22, height=21,
                               activestyle='none', highlightthickness=0, yscrollcommand=self.yscroll_op_list)
        self.op_list.place(x=374, y=142)

        # New price list
        np_title_list = Label(window, text='New Price', bg='#4f4f4f', fg='#e8e8e8', width=19, borderwidth=2,
                              relief='flat', font=('arial', 9))
        np_title_list.place(x=507, y=121)
        self.np_list = Listbox(window, selectmode=SINGLE, borderwidth=2, relief='flat', width=22, height=21,
                               activestyle='none', highlightthickness=0, yscrollcommand=self.yscroll_np_list)
        self.np_list.place(x=509, y=142)

        # Main window settings
        window.resizable(False, False)
        icon = PhotoImage(file='images\logo.png')
        window.tk.call('wm', 'iconphoto', window._w, icon)
        window.title('SATUCT - Calculations')
        window['bg'] = '#e8e8e8'
        window.geometry('676x500+200+150')
        window.mainloop()


if __name__ == '__main__':
    MainProgram()
