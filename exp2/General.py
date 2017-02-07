from Tkinter import *
import ttk
import time


class General(Frame):
    def __init__(self, master, frame_look={}, **look):
        args = dict( border=1)
        args.update(frame_look)
        Frame.__init__(self, master, **args)

        # args = {'relief': FLAT}
        args.update(look)

        self.dt = StringVar()
        self.tm = StringVar()
        self.time1 = ''

        self.sl_label = Label(self, text='Serial No :', **args)
        self.sl_label.grid(row=0, column=0, sticky=W, pady=7)
        self.sl_entry = Entry(self)
        self.sl_entry.grid(row=0, column=1, sticky=W, padx=5)
        self.id_label = Label(self, text='I.D. :', **args)
        self.id_label.grid(row=1, column=0, sticky=W, pady=7)
        self.id_entry = Entry(self)
        self.id_entry.grid(row=1, column=1, sticky=W, padx=5)
        self.time_label = Label(self, text='Time :', **args)
        self.time_label.grid(row=2, column=0, sticky=W, pady=7)
        self.time_entry = Entry(self, textvariable= self.tm)
        self.time_entry.grid(row=2, column=1, sticky=W, padx=5)
        self.date_label = Label(self, text='Date :', **args)
        self.date_label.grid(row=3, column=0, sticky=W, pady=7)
        self.date_entry = Entry(self, textvariable = self.dt)
        self.date_entry.grid(row=3, column=1, sticky=W, padx=5)
        self.date_update()

    def date_update(self):
        self.time2 = time.strftime('%H:%M:%S')
        # if time string has changed, update it
        if self.time2 != self.time1:
            time1 = self.time2
            self.dt.set(self.time2)
            self.tm.set(self.time2)
        # calls itself every 200 milliseconds
        # to update the time display as needed
        # could use >200 ms, but display gets jerky
        self.date_entry.after(200, self.date_update)
