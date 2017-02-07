from Tkinter import *
import ttk
import string

class ApplicationDetails(Frame):
    def __init__(self, master, frame_look={}, **look):
        args = dict(border=1)
        args.update(frame_look)
        Frame.__init__(self, master, **args)

        # args = {'relief': FLAT}
        args.update(look)
        self.options = [1,2,3]
        self.var = StringVar()
        self.v_label = Label(self, text='Vehicle No :', **args)
        self.v_label.grid(row=0, column=0, sticky=W, pady=7)
        self.v_entry = Entry(self, textvariable = self.var)
        self.v_entry.grid(row=0, column=1, sticky=W, padx=5)
        self.v_entry.bind('<Enter>', self.cap)

        self.reg_label = Label(self, text='Year of Regn :', **args)
        self.reg_label.grid(row=1, column=0, sticky=W, pady=7)
        self.reg_entry = Entry(self, **args)
        self.reg_entry.grid(row=1, column=1, sticky=W, padx=5)

        self.odo_label = Label(self, text='Odometer Reading :', **args)
        self.odo_label.grid(row=2, column=0, sticky=W, pady=7)
        self.odo_entry = Entry(self, **args)
        self.odo_entry.grid(row=2, column=1, sticky=W, padx=5)

        self.vtype_label = Label(self, text='Vehicle Type :', **args)
        self.vtype_label.grid(row=3, column=0, sticky=W, pady=7)
        self.combo = ttk.Combobox(self, values=self.options)
        self.combo.grid(row=3, column=1, sticky=W, padx=5)

        self.engtype_label = Label(self, text='Engine Type :', **args)
        self.engtype_label.grid(row=4, column=0, sticky=W, pady=7)
        self.eng_combo = ttk.Combobox(self, values=self.options)
        self.eng_combo.grid(row=4, column=1, sticky=W, padx=5)

        self.make_label = Label(self, text='Make :', **args)
        self.make_label.grid(row=5, column=0, sticky=W, pady=7)
        self.make_combo = ttk.Combobox(self, values=self.options)
        self.make_combo.grid(row=5, column=1, sticky=W, padx=5)
        self.make_button = Button(self, text='Add', command = self.add_make)
        self.make_button.grid(row=5, column=2, sticky=W, padx=5)

        #self.cap()

        self.mod_label = Label(self, text='Model :', **args)
        self.mod_label.grid(row=6, column=0, sticky=W, pady=7)
        self.mod_combo = ttk.Combobox(self, values=self.options)
        self.mod_combo.grid(row=6, column=1, sticky=W, padx=5)
        self.mod_button = Button(self, text='Add', command = self.add_make)
        self.mod_button.grid(row=6, column=2, sticky=W, padx=5)

        self.extra = Button(self, text='DELL', command = self.gen_params)
        self.extra.grid(row=7, column=0, sticky=W, pady=7)

        #self.result = [self.v_entry.get(), self.reg_entry.get(), self.odo_entry.get(), self.combo.get(),self.eng_combo.get(), self.mod_combo.get()]





    def add_make(self):
        print 'add make'

    def gen_params(self, **args):
        self.idle_label = Label(self, text = 'Idle RPM :', **args)
        self.idle_label.grid(row=8, column=0, sticky=W, pady=7)
        self.idle_entry = Entry(self)
        self.idle_entry.grid(row=8, column=1, sticky=W, padx=5)

        self.max_label = Label(self, text = 'Max RPM :', **args)
        self.max_label.grid(row=9, column=0, sticky=W, pady=7)
        self.max_entry = Entry(self)
        self.max_entry.grid(row=9, column=1, sticky=W, padx=5)

        self.k_label = Label(self, text='K(%) :', **args)
        self.k_label.grid(row=10, column=0, sticky=W, pady=7)
        self.k_entry = Entry(self)
        self.k_entry.grid(row=10, column=1, sticky=W, padx=5)


        self.extra = Button(self, text='XPPX', command=self.del_params)
        self.extra.grid(row=7, column=0, sticky=W, pady=7)




    def del_params(self):
        self.idle_label.destroy()
        self.idle_entry.destroy()
        self.max_label.destroy()
        self.max_entry.destroy()
        self.k_entry.destroy()
        self.k_label.destroy()

        self.extra = Button(self, text='DELL', command=self.gen_params)
        self.extra.grid(row=7, column=0, sticky=W, pady=7)

    def get_details(self):
        self.result = [self.v_entry.get(), self.reg_entry.get(), self.odo_entry.get(), self.combo.get(),
                       self.eng_combo.get(), self.make_combo.get(), self.mod_combo.get()]
        return self.result

    def get_params(self):
        self.param_result = [self.idle_entry.get(), self.max_entry.get(), self.k_entry.get()]
        return self.param_result

    def cap(self):
        self.var.set(self.var.get().upper())



