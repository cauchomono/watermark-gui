from tkinter import *
from PIL import ImageTk, Image, ImageGrab
from tkinter.messagebox import showinfo
from tkinter import filedialog

class Photo_controller():

    def __init__(self,):
        self.photo_id = 0
        self.collection = ('test_img/1.jpg', "test_img/2.gif", "test_img/3.jpg", "test_img/4.jpg")


    def prepared_image(self):
            image_to_display = self.collection[self.photo_id]
            print(image_to_display)
            image = Image.open(image_to_display)  # allows other image formats
            resized_image = image.resize((720, 480))  # Resizes the image
            img = ImageTk.PhotoImage(resized_image)
            return img



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