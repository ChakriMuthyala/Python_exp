from Tkinter import *
import ttk

class MfgType(Frame):
    def __init__(self, master, frame_look={}, **look):
        args = dict(border=1)
        args.update(frame_look)
        Frame.__init__(self, master, **args)

        # args = {'relief': FLAT}
        args.update(look)

        self.valid_entry = Entry(self, width=30)
        self.valid_entry.grid(padx=20, pady=30)