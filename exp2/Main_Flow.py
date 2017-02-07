
from Tkinter import *
import ttk
import time
from General import *
from ApplicationDetails import *
from TableGen import *
from CameraHandler import *


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
    editmenu.add_command(label="Cut", command=hello)
    editmenu.add_command(label="Copy", command=hello)
    editmenu.add_command(label="Paste", command=hello)
    menubar.add_cascade(label="Edit", menu=editmenu)

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
        der = frame2_class.get_details()
        param = frame2_class.get_params()
        print der
        print len(der)
        print param
        print len(param)


    #font_style = ("calibri", 15)
    root = Tk()
    root_config()
    menu_bar()

    frame1 = LabelFrame(root, text='General', bd=2, relief=GROOVE )
    frame1.place(x=10,y=10)
    frame1_class = General(frame1)
    frame1_class.pack(fill=X)

    frame2 = LabelFrame(root, text = 'Application Details', bd=2, relief=GROOVE)
    frame2.place(x=10, y=180)
    frame2_class = ApplicationDetails(frame2)
    frame2_class.pack(fill=X)

    frame3 = LabelFrame(root, text = 'Table', bd=2, relief=GROOVE)
    frame3.place(x=400, y=10)
    frame3_class = TableGen(frame3)
    frame3_class.pack(fill=X)

    frame4 = LabelFrame(root, text='Camera Handler', bd=2, relief=GROOVE)
    frame4.place(x=400, y=290)
    frame4_class = CameraHandler(frame4)
    frame4_class.pack(fill=X)


    butt = Button(root, text='get data', command=show_contents)
    butt.pack(side='bottom')

    root.bind()
    root.mainloop()
