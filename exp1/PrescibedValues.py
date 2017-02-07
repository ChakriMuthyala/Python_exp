from Tkinter import *
#import ApplicationDetails
import ttk

class PrescribedValues(Frame):
    def __init__(self, master, frame_look={}, **look):
        args = dict(border=1)
        args.update(frame_look)
        Frame.__init__(self, master, **args)

        # args = {'relief': FLAT}
        args.update(look)

        font = ('Helvetica', 13)

        self.naive1 = Label(self, text='', width=10, **args)
        self.naive1.grid(row=0, column=0, sticky=W, pady=7)

        self.pre_label_co = Label(self, text="Prescribed value\n CO", font=font, bg='white', **args)
        self.pre_label_co.grid(row=0, column=1, sticky=W, pady=7)

        self.mes_label_co = Label(self, text="Measured level\n CO", bg='white', width=18, font=font, **args)
        self.mes_label_co.grid(row=0, column=2, sticky=W, pady=7)

        self.pre_label_hc = Label(self, text="Prescibed value\n HC", bg='white', font=font, **args)
        self.pre_label_hc.grid(row=0, column=3, sticky=W, pady=7)

        self.mes_label_hc = Label(self, text="Measured value\n HC", bg='white', font=font, **args)
        self.mes_label_hc.grid(row=0, column=4, sticky=W, pady=7)

        self.before_adj = Label(self, text='Before\n Adjustments', **args)
        self.before_adj.grid(row=1, column=2, sticky=W, padx=5)

        self.after_adj = Label(self, text='After\n Adjustments', **args)
        self.after_adj.grid(row=1, column=2, sticky=E, padx=5)

        self.t_pet_label = Label(self, text='PETROL', width=10, font=('Helvetica', 15), **args)
        self.t_pet_label.grid(row=2, column=0, sticky=W)

        self.t_entry_1 = Entry(self, width=10)
        self.t_entry_1.grid(row=2, column=1, sticky=W)

        self.t_entry_2 = Entry(self, width=10)
        self.t_entry_2.grid(row=2, column=2, sticky=W, padx=8)

        self.t_entry_3 = Entry(self, width=10)
        self.t_entry_3.grid(row=2, column=2, sticky=E, padx=8)

        self.t_entry_4 = Entry(self, width=10)
        self.t_entry_4.grid(row=2, column=3, sticky=W, padx=8)

        self.t_entry_5 = Entry(self, width=10)
        self.t_entry_5.grid(row=2, column=4, sticky=W, padx=8)

        self.f_pet_label = Label(self, text='CNG/LPG', width=10, font=('Helvetica', 15), **args)
        self.f_pet_label.grid(row=3, column=0, sticky=W)

        self.f_entry_1 = Entry(self, width=10)
        self.f_entry_1.grid(row=3, column=1, sticky=W)

        self.f_entry_2 = Entry(self, width=10)
        self.f_entry_2.grid(row=3, column=2, sticky=W, padx=8)

        self.f_entry_3 = Entry(self, width=10)
        self.f_entry_3.grid(row=3, column=2, sticky=E, padx=8)

        self.f_entry_4 = Entry(self, width=10)
        self.f_entry_4.grid(row=3, column=3, sticky=W, padx=8)

        self.f_entry_5 = Entry(self, width=10)
        self.f_entry_5.grid(row=3, column=4, sticky=W, padx=8)

   # print(frame2_class.ct_combo.get())






