from tkinter import *
from tkinter.filedialog import asksaveasfilename

from PIL import ImageTk, Image,ImageDraw, ImageFont
from tkinter.messagebox import showinfo
from tkinter import filedialog



class Photo_controller():

    def __init__(self,):
        self.photo_id = 0
        self.collection = ('test_img/principal.jpg','test_img/principal.jpg')





    def prepared_image(self):
            image_to_display = self.collection[self.photo_id]
            print(image_to_display)
            self.image = Image.open(image_to_display)  # allows other image formats
            resized_image = self.image.resize((720, 480))  # Resizes the image
            self.img = ImageTk.PhotoImage(resized_image)
            return self.img



    def upload_images(self):

        filetypes = [
            ("image", ".jpeg"),
            ("image", ".png"),
            ("image", ".jpg"),
        ]

        filenames = filedialog.askopenfilenames(
            title='Open files',
            initialdir='/',
            filetypes=filetypes)
        if len(filenames) == 0:
            showinfo(title='Selected Files', message="No selected any file")
        else:
            showinfo(title='Selected Files', message=filenames)
            if len(filenames) == 1:
                self.collection = (filenames[0],filenames[0])
            else:
                self.collection = filenames
            return self.prepared_image()



    def download_images(self):

        file = asksaveasfilename(defaultextension=f".jpg", filetypes=[("All Files", "*.*"), ("PNG file", "*.png"), ("jpg file", "*.jpg")])
        if file:
            self.image.save(file)


    def motion (self,event):
        self.x,self.y = event.x, event.y



