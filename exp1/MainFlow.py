#20BA24#20BA24
from Tkinter import *
import ttk
import time
from General import *
from ApplicationDetails import *
#from PrescibedValues import *
#from Validity import *
from CameraHandler import *
#from MfgType import *

#print required modules
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw


def hello():
    print "hello!"

def menu_bar(): #menu bar configuration ........more to edit
    menubar = Menu(root)

    # create a pulldown menu, and add it to the menu bar
    filemenu = Menu(menubar, tearoff=0)
    filemenu.add_command(label="Open", command=hello)
    filemenu.add_command(label="Save", command=hello)
    filemenu.add_separator()
    filemenu.add_command(label="Exit", command=root.quit)
    menubar.add_cascade(label="File", menu=filemenu)

    # create more pulldown menus
    editmenu = Menu(menubar, tearoff=0)
    editmenu.add_command(label="View Backup", command=hello)
    editmenu.add_command(label="preferences", command=hello)
    editmenu.add_command(label="Change Password", command=hello)
    menubar.add_cascade(label="View", menu=editmenu)

    helpmenu = Menu(menubar, tearoff=0)
    helpmenu.add_command(label="About", command=hello)
    menubar.add_cascade(label="Help", menu=helpmenu)

    # display the menu
    root.config(menu=menubar)

def root_config():   #root configuration
    root.title("Petrol")
    root.minsize(1000, 600)  # width, height




if __name__ == '__main__':

    def show_contents():
        der = frame2_class.get()
        print  'datafromhere:', der
        print 'len:', len(der)

#        mn, yr = der[6].split(' ')
#        if mn=='2W' or mn == '3W':
#            if int(yr) < 2000 and (mn == 'Jan' or mn == 'Feb' or mn == 'May'):
#                veh_type = mn + ' Mfg On/Before 31st Mar 2000'
#                co = 4.5
#                hc = 9000
#            else:
#                veh_type = mn + ' Mfg After 31st Mar 2000'
#                co = 3.5
#                hc = 6000
#        else:
#            co = 3.5
#            hc = 6000
#        if der[8] == 'PETROL':
#            t1.set(co)
#            t4.set(hc)
#        else:
#            f1.set(co)
#            f4.set(hc)


        img = Image.open("Form.jpg")
        draw = ImageDraw.Draw(img)
        font1 = ImageFont.truetype("cmb10.ttf", 40)
        cordinates = [(680, 464),(680,556),(1344, 472),(1344,656),(1344,732),(1344,568),(680,656),(1944,464)]                                #coordinates order wise of der variable (x,y)
        for i in range(8):
            draw.text(cordinates[i], der[i], (0, 0, 0), font=font1)
        draw.text((1944, 572), time.strftime('%b %d %Y'), (0, 0, 0), font=font1)
        draw.text((1944, 656), time.strftime('%H:%M:%S'), (0, 0, 0), font=font1)
        img.save('sample-out.jpg')




    #font_style = ("calibri", 15)
    root = Tk()
    root_config()
    menu_bar()
    #print 'jahnavi'
    frame1 = LabelFrame(root, text='General', bd=2, relief=GROOVE )
    frame1.place(x=10,y=10)
    frame1_class = General(frame1)
    frame1_class.pack(fill=X)


#********************************************************************************
    frame3 = LabelFrame(root, text = '6M Validity', bd=2, relief=GROOVE)
    frame3.place(x=320, y=130)
    #frame3_class = Validity(frame3)
    #frame3_class.pack(fill=X)
    valid_label = Label(frame3, text='Valid Upto :', height=2, width=8)
    valid_label.grid(row=0, column=0, sticky=W, pady=7)
    valid = StringVar()
    valid_entry = Entry(frame3, textvariable = valid)
    valid_entry.grid(row=0, column=1, sticky=W, padx=20, pady=20)

#**************************************************************************************

    frame6 = LabelFrame(root, text='Mfg Type', bd=2, relief=GROOVE)
    frame6.place(x=320, y=10)
    # frame6_class = MfgType(frame6)
    # frame6_class.pack(fill=X)
    Mfg = StringVar()
    Mfg_entry = Label(frame6, textvariable=Mfg, font = ('Helvitica', 10),width=30)
    Mfg_entry.grid(padx=20, pady=30)

#*****************************************************************************************
    frame4 = LabelFrame(root, text='Prescribed Values', bd=2, relief=GROOVE)
    frame4.place(x=320, y=333)
 #   frame4_class = PrescribedValues(frame4)
   # frame4_class.pack(fill=X)

    naive1 = Label(frame4, text='', width=10)
    naive1.grid(row=0, column=0, sticky=W, pady=7)
    font = ('Helvetica', 13)
    pre_label_co = Label(frame4, text="Prescribed value\n CO", font=font, bg='white',)
    pre_label_co.grid(row=0, column=1, sticky=W, pady=7)

    mes_label_co = Label(frame4, text="Measured level\n CO", bg='white', width=18, font=font)
    mes_label_co.grid(row=0, column=2, sticky=W, pady=7)

    pre_label_hc = Label(frame4, text="Prescibed value\n HC", bg='white', font=font)
    pre_label_hc.grid(row=0, column=3, sticky=W, pady=7)

    mes_label_hc = Label(frame4, text="Measured value\n HC", bg='white', font=font)
    mes_label_hc.grid(row=0, column=4, sticky=W, pady=7)

    before_adj = Label(frame4, text='Before\n Adjustments')
    before_adj.grid(row=1, column=2, sticky=W, padx=5)

    after_adj = Label(frame4, text='After\n Adjustments')
    after_adj.grid(row=1, column=2, sticky=E, padx=5)

    t_pet_label = Label(frame4, text='PETROL', width=10, font=('Helvetica', 15))
    t_pet_label.grid(row=2, column=0, sticky=W)

    t1 = StringVar()
    t_entry_1 = Entry(frame4, textvariable =t1, width=10)
    t_entry_1.grid(row=2, column=1, sticky=W)

    t2 = StringVar()
    t_entry_2 = Entry(frame4,textvariable = t2, width=10)
    t_entry_2.grid(row=2, column=2, sticky=W, padx=8)

    t3 = StringVar()
    t_entry_3 = Entry(frame4,textvariable = t3, width=10)
    t_entry_3.grid(row=2, column=2, sticky=E, padx=8)

    t4 = StringVar()
    t_entry_4 = Entry(frame4,textvariable = t4, width=10)
    t_entry_4.grid(row=2, column=3, sticky=W, padx=8)

    t5 = StringVar()
    t_entry_5 = Entry(frame4,textvariable = t5, width=10)
    t_entry_5.grid(row=2, column=4, sticky=W, padx=8)

    f_pet_label = Label(frame4, text='CNG/LPG', width=10, font=('Helvetica', 15))
    f_pet_label.grid(row=3, column=0, sticky=W)

    f1 = StringVar()
    f_entry_1 = Entry(frame4, textvariable = f1,width=10)
    f_entry_1.grid(row=3, column=1, sticky=W)

    f2 = StringVar()
    f_entry_2 = Entry(frame4,textvariable = f2, width=10)
    f_entry_2.grid(row=3, column=2, sticky=W, padx=8)

    f3 = StringVar()
    f_entry_3 = Entry(frame4,textvariable = f3, width=10)
    f_entry_3.grid(row=3, column=2, sticky=E, padx=8)

    f4 = StringVar()
    f_entry_4 = Entry(frame4, textvariable = f4,width=10)
    f_entry_4.grid(row=3, column=3, sticky=W, padx=8)

    f5 = StringVar()
    f_entry_5 = Entry(frame4,textvariable = f5, width=10)
    f_entry_5.grid(row=3, column=4, sticky=W, padx=8)

#*****************************************************************************
    pet_msg = [t1, t4]
    cng_msg = [f1,f4]

    frame2 = LabelFrame(root, text='Application Details', bd=2, relief=GROOVE)
    frame2.place(x=10, y=180)
    frame2_class = ApplicationDetails(frame2, pet_msg, cng_msg, Mfg, valid)
    frame2_class.pack(fill=X)

    #frame5 = LabelFrame(root, text='Camera Handler', bd=2, relief=GROOVE)
    #frame5.place(x=560, y=10)
    #frame5_class = CameraHandler(frame5)
    #frame5_class.pack(fill=X)

    frame5_class = CameraHandler(root)
    frame5_class.pack(fill=X)


    frame7 = Frame(root, bg='Green')
    frame7.place(x=400, y=530)

    butt = Button(frame7, text='  OK   ', command=show_contents)
    butt.pack(side = "left", padx = 40)
    cancel = Button(frame7, text='  cancel   ', command=root.destroy)
    cancel.pack(side='right', padx=40)


    root.bind()
    root.mainloop()
