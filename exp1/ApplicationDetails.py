from Tkinter import *
import ttk
import xlrd
from xlrd import *

#import PrescibedValues
import time
import datetime
import openpyxl


def add_one_month(t):
    """Return a `datetime.date` or `datetime.datetime` (as given) that is
    one month earlier.

    Note that the resultant day of the month might change if the following
    month has fewer days:

       #>>> add_one_month(datetime.date(2010, 1, 31))
        datetime.date(2010, 2, 28)
    """
    import datetime
    one_day = datetime.timedelta(days=1)
    one_month_later = t + one_day
    while one_month_later.month == t.month:  # advance to start of next month
        one_month_later += one_day
    target_month = one_month_later.month
    while one_month_later.day < t.day:  # advance to appropriate day
        one_month_later += one_day
        if one_month_later.month != target_month:  # gone too far
            one_month_later -= one_day
            break

    return one_month_later
dw = time.strftime('%Y %m %d')
dw = dw.split()
dw = map(int, dw)
#dw = tuple(dw)

lk = add_one_month(datetime.date(dw[0], dw[1], dw[2]))
for i in range(5):
    lk = add_one_month(lk)


class ApplicationDetails(Frame):
    def __init__(self, master, pet_msg, cng_msg, Mfg, valid, frame_look={}, **look):
        args = dict(border=1)
        args.update(frame_look)
        Frame.__init__(self, master, **args)

        #############EXCEL



        # args = {'relief': FLAT}
        args.update(look)

        self.t1 = pet_msg[0]
        self.t2 = pet_msg[1]
        self.f1 = cng_msg[0]
        self.f2 = cng_msg[1]
        self.Mfg = Mfg
        self.valid = valid
        xl = xlrd.open_workbook('AD.xls')
        shet = xl.sheets()[0]
        self.rows = shet.nrows
        self.c1 = shet.col(0)
        self.c2 = shet.col(1)
        self.c3 = shet.col(2)
        self.cat_options = ['2W','3W','4W']
        self.mnyr_options = ['Jan', 'Feb','Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
        self.f_options = ['PETROL', 'CNG']
        self.ct_options = ['YES', 'NO']
        self.eng_options = ['2S','4S']
        # values=self.make_options

        self.options = [1, 2, 3]
        self.pucc_label = Label(self, text='PUCC No :', **args)
        self.pucc_label.grid(row=0, column=0, sticky=W, pady=7)
        self.pucc_entry = Entry(self)
        self.pucc_entry.grid(row=0, column=1, sticky=W, padx=5)

        self.v_label = Label(self, text='Vehicle No :', **args)
        self.v_label.grid(row=1, column=0, sticky=W, pady=7)
        self.v_entry = Entry(self)
        self.v_entry.grid(row=1, column=1, sticky=W, padx=5)

        # self.cat_options = self.wheel#['2W', '3W', '4W']
        self.cat_label = Label(self, text='Category :', **args)
        self.cat_label.grid(row=2, column=0, sticky=W, pady=7)
        self.cat_combo = ttk.Combobox(self, values=self.cat_options)
        self.cat_combo.grid(row=2, column=1, sticky=W, padx=5)
        self.cat_combo.bind('<<ComboboxSelected>>', self.add_make)
        self.cat_combo.bind('<Return>', self.add_make)

        # self.make_options = []

        value = StringVar()

        self.make_label = Label(self, text='Make :', **args)
        self.make_label.grid(row=3, column=0, sticky=W, pady=7)
        self.make_combo = ttk.Combobox(self)
        self.make_combo.grid(row=3, column=1, sticky=W, padx=5)
        self.make_combo.bind('<<ComboboxSelected>>', self.add_model)
        self.make_combo.bind('<Return>', self.add_model)

        self.make_button = Button(self, text='Add', command = self.Xcel)
        self.make_button.grid(row=3, column=2, sticky=W, padx=5)




        self.mod_label = Label(self, text='Model :', **args)
        self.mod_label.grid(row=4, column=0, sticky=W, pady=7)
        self.mod_combo = ttk.Combobox(self)
        self.mod_combo.grid(row=4, column=1, sticky=W, padx=5)

        self.eng_label = Label(self, text='Eng Stroke:', **args)
        self.eng_label.grid(row=5, column=0, sticky=W, pady=7)
        self.eng_combo = ttk.Combobox(self, width=10, values=self.eng_options)
        self.eng_combo.grid(row=5, column=1, sticky=W, padx=5)

        self.mnyr_label = Label(self, text='Month/Year :', **args)
        self.mnyr_label.grid(row=6, column=0, sticky=W, pady=7)
        self.mnyr_combo = ttk.Combobox(self, width=8, values=self.mnyr_options)
        self.mnyr_combo.grid(row=6, column=1, sticky=W, padx=5)
        self.mnyr_entry = Entry(self, width=10)
        self.mnyr_entry.grid(row=6, column=1, sticky=E)

        self.f_label = Label(self, text='Fuel:', **args)
        self.f_label.grid(row=7, column=0, sticky=W, pady=7)
        self.f_combo = ttk.Combobox(self, width=10, values=self.f_options)
        self.f_combo.grid(row=7, column=1, sticky=W, padx=5)

        self.ct_label = Label(self, text='Catalyst :', **args)
        self.ct_label.grid(row=8, column=0, sticky=W, pady=7)
        self.ct_combo = ttk.Combobox(self, width=10, values=self.ct_options)
        self.ct_combo.grid(row=8, column=1, sticky=W, padx=5)
        self.ct_combo.bind('<<ComboboxSelected>>', self.next_class)
        self.ct_combo.bind('<Return>', self.next_class)


    def next_class(self,k):
        #if self.mnyr_combo.get()=='' + ' ' + self.mnyr_entry.get()
        #self.t1.set('yu')

        if self.cat_combo.get()=='2W' or self.cat_combo.get()=='3W':
            if int(self.mnyr_entry.get())<2000 and (self.mnyr_combo.get() in ('Jan', 'Feb','Mar') ):
                self.Mfg.set(self.cat_combo.get()+' Mfg On/Before\n 31st Mar 2000')
                co = 4.5
                hc = 9000
            else:
                self.Mfg.set(self.cat_combo.get() + ' Mfg After\n 31st Mar 2000')
                co = 3.5
                hc = 6000
        else:
            self.Mfg.set('Others')
            co = 3.5
            hc = 6000
        if self.f_combo.get()=='PETROL':
            self.t1.set(co)
            self.t2.set(hc)
            self.f1.set('')
            self.f2.set('')
        else:
            self.f1.set(co)
            self.f2.set(hc)
            self.t1.set('')
            self.t2.set('')
        self.valid.set(lk)



    def add_make(self,k):
        k = self.cat_combo.get()
        #print k
        self.make_combo.set('')
        self.mod_combo.set('')
        self.make_options = []
        for i in xrange(self.rows):
            if k == str(self.c1[i].value):
                self.make_options.append(str(self.c2[i].value))
        self.make_options = list(set(self.make_options))
        self.make_options.sort();
        self.make_combo['values'] = self.make_options

    def add_model(self,k):
        k = self.make_combo.get()
        #print k
        self.mod_combo.set('')
        self.mod_options = []
        for i in xrange(self.rows):
            if k == str(self.c2[i].value):
                self.mod_options.append(str(self.c3[i].value))
        self.mod_options = list(set(self.mod_options))
        self.mod_options.sort();
        self.mod_combo['values'] = self.mod_options

    def xl_make(self,k):
        k = self.xl_cat_combo.get()
        #print k
        self.xl_make_combo.set('')
        self.xl_mod_combo.set('')
        self.xl_make_options = []
        for i in xrange(self.rows):
            if k == str(self.c1[i].value):
                self.xl_make_options.append(str(self.c2[i].value))
        self.xl_make_options = list(set(self.xl_make_options))
        self.xl_make_options.sort();
        self.xl_make_combo['values'] = self.xl_make_options

    def xl_model(self,k):
        k = self.xl_make_combo.get()
        #print k
        self.xl_mod_combo.set('')
        self.xl_mod_options = []
        for i in xrange(self.rows):
            if k == str(self.c2[i].value):
                self.xl_mod_options.append(str(self.c3[i].value))
        self.xl_mod_options = list(set(self.xl_mod_options))
        self.xl_mod_options.sort();
        self.xl_mod_combo['values'] = self.xl_mod_options

    def Xcel_operation(self):
        v1 = self.xl_cat_combo.get()
        v2 = self.xl_make_combo.get()
        v3 = self.xl_mod_combo.get()
        #print v1, v2, v3

    def Xcel(self):
        self.Add = Toplevel()
        self.Add.wm_title('Add/Edit List')

        self.xl_cat_label = Label(self.Add, text='Category :')
        self.xl_cat_label.grid(row=2, column=0, sticky=W, pady=7)
        self.xl_cat_combo = ttk.Combobox(self.Add, values=self.cat_options)
        self.xl_cat_combo.grid(row=2, column=1, sticky=W, padx=5)
        self.xl_cat_combo.bind('<<ComboboxSelected>>', self.xl_make)
        self.xl_cat_combo.bind('<Return>', self.xl_make)

        self.xl_make_label = Label(self.Add, text='Make :')
        self.xl_make_label.grid(row=3, column=0, sticky=W, pady=7)
        self.xl_make_combo = ttk.Combobox(self.Add)
        self.xl_make_combo.grid(row=3, column=1, sticky=W, padx=5)
        self.xl_make_combo.bind('<<ComboboxSelected>>', self.xl_model)
        self.xl_make_combo.bind('<Return>', self.xl_model)

        self.xl_mod_label = Label(self.Add, text='Model :')
        self.xl_mod_label.grid(row=4, column=0, sticky=W, pady=7)
        self.xl_mod_combo = ttk.Combobox(self.Add)
        self.xl_mod_combo.grid(row=4, column=1, sticky=W, padx=5)

        self.xl_make_button = Button(self.Add, text='Add', command = self.Xcel_operation)
        self.xl_make_button.grid(row=4, column=2, sticky=W, padx=5)



    def get(self):
        self.result = [self.pucc_entry.get(), self.v_entry.get(), self.cat_combo.get(), self.make_combo.get(),
                       self.mod_combo.get(), self.eng_combo.get(), self.mnyr_combo.get()+' '+ self.mnyr_entry.get(),
                       self.ct_combo.get(),self.f_combo.get(),]
        return self.result
