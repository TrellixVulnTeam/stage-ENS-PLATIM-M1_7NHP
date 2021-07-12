import tkinter as tk

import PIL
from PIL import Image
from PIL import ImageFilter, ImageTk, ImageDraw, ImageStat
import numpy as np

from tkinter.filedialog import *
from test import *
from PIL import Image

import cv2

def write_array_masck(p):
    tab = []

def alert():
    tk.messagebox.showinfo("alerte", "Bravo!")

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)

        self.master = master
        self.master.title("DeepLearning Segmentation")
        self.master.geometry('400x200')
        self.pack()
        self.monCanva = None
        self.creat_widget()
        self.add_menu()
    
    def creat_widget(self):
        print("creat")

    def add_menu(self):
        menubar = tk.Menu(self.master)

        menu1 = tk.Menu(menubar, tearoff=0)
        menu1.add_command(label="Ouvir image", command=self.open_img)
        # menu1.add_command(label="Editer", command=None)
        menu1.add_separator()
        menu1.add_command(label="Quitter", command=self.master.quit)
        menubar.add_cascade(label="Fichier", menu=menu1)

        menu2 = tk.Menu(menubar, tearoff=0)
        menu2.add_command(label="predition", command=self.print_prediction)
        menu2.add_command(label="test", command=self.test)
        menu2.add_command(label="Coller", command=None)
        menubar.add_cascade(label="Editer", menu=menu2)

        menu3 = tk.Menu(menubar, tearoff=0)
        menu3.add_command(label="A propos", command=None)
        menubar.add_cascade(label="Aide", menu=menu3)

        self.master.config(menu=menubar)

    def open_img(self):
        self.filepath = askopenfilename(title="Ouvrir une image",filetypes=[('png files','.png'),('tiff files','.tif')])
        print(self.filepath)
        self.im = Image.open(self.filepath)

        self.width, self.height = self.im.size
        self.photo = ImageTk.PhotoImage(self.im)
        print("self.im", self.im)

        if self.monCanva is None:
            self.monCanva = tk.Canvas(self,width = self.width+1, height = self.height+1, bg = "blue")

        self.monCanva.create_image(0, 0, image = self.photo, anchor=tk.NW)
        # self.monCanva.create_oval(1,1,width, height, fill = "red")
        self.monCanva.image = self.im
        self.monCanva.pack()

        np_im = np.array(self.im)

    
    def print_prediction(self):
        self.p = predition_img(self.filepath)

        print(self.p)
        print(len(self.p))
        print(len(self.p[0]))

        self.p = self.p.astype(np.uint8)

        tab = self.filepath.split('/')
        self.name = tab[len(tab)-1].split('.')[0]
        name_mask = self.name + "_mask.tif"
        # cv2.imwrite(name_mask, self.p)
        # self.im = Image.open(name_mask)
        # self.photoMask = ImageTk.PhotoImage(self.im)
        new_im = Image.fromarray(self.p)
        # new_im.show()
        self.create_top(new_im)

    def create_top(self, new_im):
        top = tk.Toplevel(self.master)
        top.title("masque")
        canvas = tk.Canvas(top, width = self.width+1, height = self.height+1, bg = "red")
        canvas.pack()
        # print(new_im)
        self.photoM = ImageTk.PhotoImage(new_im)
        photo2 = ImageTk.PhotoImage(self.im)

        # print(photo.height(), photo.width())
        canvas.create_image( 0,0, image = self.photoM, anchor=tk.NW)
        # canvas.image = new_im


    def test(self):
        array = np.random.randint(255, size=(400, 400),dtype=np.uint8)
        image = Image.fromarray(array)

        print(self.name + "_mask.tif")

if __name__ == "__main__":
    root = tk.Tk()
    a = Application(master = root)
    root.mainloop()

