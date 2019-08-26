from tkinter import *
from windows.alert import Alert


class CurrencyConverter:
    def __init__(self):
        self.create_widgets_cc()

    # This function will make conversion
    def calculate_currency(self):
        choose_c = self.choose_c_var.get()
        c_conversion = self.c_conversion_var.get()

        try:
            value = float(self.c_value.get().replace(',', '.').strip())

            # If choose currency is equal conversion currency
            if choose_c == c_conversion:
                # Error alert
                n = Alert()
                n.alert('Choose different currencies, not equal', '#ff0000', 28, 40, 100, 85, '266x150+410+320')

            # Real to dollar
            elif choose_c in 'Real' and c_conversion in 'Dollar':
                conversion_value = value / 3.89
                self.current_c_value['text'] = f'R${value:.2f}'
                self.final_c_value['text'] = f'US${conversion_value:.2f}'

            # Real to euro
            elif choose_c in 'Real' and c_conversion in 'Euro':
                conversion_value = value / 4.33
                self.current_c_value['text'] = f'R${value:.2f}'
                self.final_c_value['text'] = f'€{conversion_value:.2f}'

            # Dollar to real
            elif choose_c in 'Dollar' and c_conversion in 'Real':
                conversion_value = value / 0.26
                self.current_c_value['text'] = f'US${value:.2f}'
                self.final_c_value['text'] = f'R${conversion_value:.2f}'

            # Dollar to euro
            elif choose_c in 'Dollar' and c_conversion in 'Euro':
                conversion_value = value / 1.11
                self.current_c_value['text'] = f'US${value:.2f}'
                self.final_c_value['text'] = f'€{conversion_value:.2f}'

            # Euro to real
            elif choose_c in 'Euro' and c_conversion in 'Real':
                conversion_value = value / 0.23
                self.current_c_value['text'] = f'€{value:.2f}'
                self.final_c_value['text'] = f'R${conversion_value:.2f}'

            # Euro to dollar
            elif choose_c in 'Euro' and c_conversion in 'Dollar':
                conversion_value = value / 0.90
                self.current_c_value['text'] = f'€{value:.2f}'
                self.final_c_value['text'] = f'US${conversion_value:.2f}'

        except:
            # Error alert
            n = Alert()
            n.alert('Enter a valid value', '#ff0000', 74, 40, 93, 85, '250x150+410+320')

    # Change flag when your choose a currency
    def choose_flag_change(self, choose_c_list):
        if choose_c_list in 'Real':
            self.choose_c_img['file'] = 'images\\BR.png'
        elif choose_c_list in 'Dollar':
            self.choose_c_img['file'] = 'images\\US.png'
        elif choose_c_list in 'Euro':
            self.choose_c_img['file'] = 'images\\EU.png'

    # Change flag when your choose a currency
    def converter_flag_change(self, c_conversion_list):
        if c_conversion_list in 'Real':
            self.c_conversion_img['file'] = 'images\\BR.png'
        elif c_conversion_list in 'Dollar':
            self.c_conversion_img['file'] = 'images\\US.png'
        elif c_conversion_list in 'Euro':
            self.c_conversion_img['file'] = 'images\\EU.png'

    def create_widgets_cc(self):
        # Currency converter window
        cc_window = Toplevel()

        # Background choose currency image and options
        self.bg_black = Label(cc_window, text='')
        self.bg_black.config(bg='#4f4f4f', height=13, width=21)
        self.bg_black.place(x=0, y=0)

        # Choose currency image
        self.choose_c_img = PhotoImage(file='images\\BR.png')
        choose_c = Label(cc_window, bg='#4f4f4f', image=self.choose_c_img)
        choose_c.image = self.choose_c_img
        choose_c.place(x=11, y=18)

        # Choose currency options
        self.choose_c_list = ['Real', 'Dollar', 'Euro']
        self.choose_c_var = StringVar(cc_window)
        self.choose_c_var.set(self.choose_c_list[0])
        choose_currency_option = OptionMenu(cc_window, self.choose_c_var, *self.choose_c_list,
                                            command=self.choose_flag_change)
        choose_currency_option.config(borderwidth=1, relief='flat', bg='#616161', activebackground='#7a7a7a',
                                      fg='#e8e8e8', activeforeground='#e8e8e8', highlightthickness=0)
        choose_currency_option.place(x=69, y=20)

        # Currency value
        c_value_name = Label(cc_window, text='Value:')
        c_value_name.config(bg='#4f4f4f', fg='#e8e8e8')
        c_value_name.place(x=10, y=53)
        self.c_value = Entry(cc_window, width=20)
        self.c_value.config(borderwidth=1, relief='groove')
        self.c_value.place(x=13, y=74)

        # Currency conversion image
        self.c_conversion_img = PhotoImage(file='images\\US.png')
        c_conversion_bg_img = Label(cc_window, bg='#4f4f4f', image=self.c_conversion_img)
        c_conversion_bg_img.image = self.c_conversion_img
        c_conversion_bg_img.place(x=11, y=105)

        # Currency conversion options
        self.c_conversion_list = ['Real', 'Dollar', 'Euro']
        self.c_conversion_var = StringVar(cc_window)
        self.c_conversion_var.set(self.c_conversion_list[1])
        c_conversion_option = OptionMenu(cc_window, self.c_conversion_var, *self.c_conversion_list,
                                         command=self.converter_flag_change)
        c_conversion_option.config(borderwidth=1, relief='flat', bg='#616161', activebackground='#7a7a7a',
                                   fg='#e8e8e8', activeforeground='#e8e8e8', highlightthickness=0)
        c_conversion_option.place(x=69, y=107)

        # Conversion calculate button
        c_conversion_btn = Button(cc_window, text='Convert', command=self.calculate_currency)
        c_conversion_btn.config(bg='#616161', activebackground='#7a7a7a', fg='#e8e8e8', activeforeground='#e8e8e8',
                                borderwidth=1, relief='flat', width=8)
        c_conversion_btn.place(x=42, y=155)

        # Current currency
        current_c_name = Label(cc_window, text='Current value:')
        current_c_name.config(bg='#e8e8e8', fg='#4f4f4f')
        current_c_name.place(x=170, y=14)
        self.current_c_value = Label(cc_window, text='R$0')
        self.current_c_value.config(bg='#e8e8e8', fg='#4f4f4f')
        self.current_c_value.place(x=170, y=40)

        # Final currency
        final_c_name = Label(cc_window, text='Final value:')
        final_c_name.config(bg='#e8e8e8', fg='#4f4f4f')
        final_c_name.place(x=170, y=101)
        self.final_c_value = Label(cc_window, text='US$0')
        self.final_c_value.config(bg='#e8e8e8', fg='#4f4f4f')
        self.final_c_value.place(x=170, y=127)

        # Currency converter window settings
        cc_window.resizable(True, False)
        cc_icon = PhotoImage(file='images\\logo.png')
        cc_window.tk.call('wm', 'iconphoto', cc_window._w, cc_icon)
        cc_window.title('SATUCT - Currency Converter')
        cc_window['bg'] = '#e8e8e8'
        cc_window.geometry('400x200')
