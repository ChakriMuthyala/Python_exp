from Tkinter import *
from PIL import Image, ImageTk

class CameraHandler(Frame):
    def __init__(self, master, frame_look={}, **look):
        args = dict(relief=SUNKEN, border=1)
        args.update(frame_look)
        Frame.__init__(self, master, **args)

        # args = {'relief': FLAT}
        args.update(look)
        self.img = Image.open("2.jpg")
        self.pic = ImageTk.PhotoImage(self.img)
        self.pic_button = Button(self, text='View Camera', command= self.get_pic)
        self.pic_button.pack(side='top')
        self.label = Label(self, width=400, height=250, image=self.pic)
        self.label.pack(side='bottom')

    def get_pic(self):
        print 'hello'