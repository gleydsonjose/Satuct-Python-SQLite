from tkinter import *


class Alert:
    def alert(self, text, fontcolor, alert_x, alert_y, ok_x, ok_y, geometry):
        alert_window = Toplevel()

        alert = Label(alert_window, text=text)
        alert.config(bg='#e8e8e8', fg=fontcolor)
        alert.place(x=alert_x, y=alert_y)

        # OK Button
        ok_btn = Button(alert_window, text='OK', command=alert_window.destroy)
        ok_btn.config(bg='#4f4f4f', activebackground='#616161', fg='#e8e8e8', activeforeground='#e8e8e8',
                      borderwidth=1,
                      relief='flat', width=8)
        ok_btn.place(x=ok_x, y=ok_y)

        alert_window.resizable(False, False)
        alert_icon = PhotoImage(file='images\\logo.png')
        alert_window.tk.call('wm', 'iconphoto', alert_window._w, alert_icon)
        alert_window.title('SATUCT - Alert')
        alert_window['bg'] = '#e8e8e8'
        alert_window.geometry(geometry)
