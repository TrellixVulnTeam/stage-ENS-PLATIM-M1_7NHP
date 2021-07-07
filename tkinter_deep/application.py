import tkinter as tk

import PIL
from PIL import Image
from PIL import ImageFilter, ImageTk, ImageDraw, ImageStat
import numpy as np

from tkinter.filedialog import *
from test import *
from PIL import Image

import cv2


def alert():
    tk.messagebox.showinfo("alerte", "Bravo!")

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)

        self.master = master
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
        # self.im.show()
        # self.im.show()
        # p = predition_img(self.filepath)
        # print(type(p))
        width, height = self.im.size
        self.photo = ImageTk.PhotoImage(self.im)
        print("self.im", self.im)

        # print(type(photo))

        print(width, height)
        if self.monCanva is None:
            self.monCanva = tk.Canvas(self,width = width+1, height = height+1)
            # , bg = "blue")

        self.monCanva.create_image(0, 0, image = self.photo)
        # self.monCanva.create_oval(1,1,width, height, fill = "red")
        self.monCanva.image = self.im
        self.monCanva.pack()
    
    def print_prediction(self):
        p = predition_img(self.filepath)
        print(type(p))
        print(p)
        cv2.imwrite(f"test_moii.png", p)

        # pil_image=Image.fromarray(p)
        # pil_image.show()
    
    def test(self):
        array = np.random.randint(255, size=(400, 400),dtype=np.uint8)
        image = Image.fromarray(array)
        # image.show()
        print(array)

if __name__ == "__main__":
    root = tk.Tk()
    a = Application(master = root)
    root.mainloop()

