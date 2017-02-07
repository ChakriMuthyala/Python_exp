from Tkinter import *
import threading
import vidcap
from PIL import Image, ImageFont, ImageTk, ImageDraw, ImageFont
import time
import multiprocessing

class CameraHandler(Frame):

    def __init__(self, master, frame_look={}, **look):
        args = dict( border=1)
        args.update(frame_look)
        Frame.__init__(self, master, **args)
        # args = {'relief': FLAT}

        args.update(look)

        self.thread = None
        self.stopEvent = None
        self.dev = vidcap.new_Dev(0, 0)
        self.panel = None


#        self.img0 = Image.open("2.jpg")
#        self.img = self.img0.resize((400,270), Image.ANTIALIAS)
#        self.pic = ImageTk.PhotoImage(self.img)
#        #self.label = Label(self, width=400, height=270, image=self.pic)
       # self.label.pack(side='bottom')
        self.pic_button = Button(self, text='View Camera', command= self.onClose)
        self.pic_button.pack(side='top', pady=5)
        #self.getBuffer()

        self.stopEvent = threading.Event()
        self.thread = threading.Thread(target=self.videoLoop, args=())
        self.thread.start()
        #self.thread = multiprocessing.Process(target= self.videoLoop, args = ())
        #self.thread.start()



    def videoLoop(self):
        try:
            while not self.stopEvent.is_set():
                buffer, width, height = self.dev.getbuffer()
                self.im = Image.frombytes('RGB', (width, height), buffer, 'raw', 'BGR', 0, -1)
                image = self.im.resize((650, 440), Image.ANTIALIAS)  # standard sizes
                image = ImageTk.PhotoImage(image)
                if self.panel is None:
                    self.panel = Label(self, width = 400, height = 270, image = image)
                    self.panel.pack(side='bottom')
                    self.panel.image = image
                    self.panel.bind('<Button-1>', self.onClose)

                else:
                    self.panel.configure(image=image)
                    #self.panel.image = image

                #self.label['image'] = self.pic
                #time.sleep(0.03)

        except RuntimeError, e:
            print("[INFO] caught a RuntimeError")
    def getBuffer(self):
            """Returns a string containing the raw pixel data.

        You probably don't want to use this function, but rather getImage() or
        saveSnapshot()."""


            return self.dev.getbuffer()

    def get_pic(self):
        k = 1




    def onClose(self):
        self.stopEvent.set()
        print 'goose'


