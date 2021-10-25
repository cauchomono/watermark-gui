from tkinter import *
from tkinter import ttk
from photo_controller import Photo_controller

class Main_Window():

    def __init__(self,):

        self.window = Tk()
        self.controller = Photo_controller()

        self.size = self.window.geometry("1280x720")
        self.title = self.window.title("Simple Watermark Software")

        self.above_controls()
        self.image_frame()

        self.image_to_canvas = self.controller.prepared_image()

        self.canvas_image = self.canvas.create_image(300, 300, image=self.image_to_canvas)

        # self.canvas.itemconfig(self.canvas_image, image=image_to_canvas)
        self.below_controls()

        self.window.mainloop()


    def above_controls(self):
        self.controls = ttk.Frame(self.window, padding=10)
        self.controls.grid(row=0, column=0)  # General Grid
        ttk.Button(self.controls, text="Upload",command = self.controller.upload_images).grid(row=0, column=1)
        ttk.Button(self.controls, text="Download").grid(row=0, column=2)

    def below_controls(self):
        self.controls = ttk.Frame(self.window, padding=10)
        self.controls.grid(row=2, column=2, columnspan=2)  # General Grid
        ttk.Button(self.controls, text="Prev", command = self.prev_image).grid(row=0,column=5)
        ttk.Button(self.controls, text="Next", command = self.next_image).grid(row=0,column=6)

    def image_frame(self):
        self.canvas = Canvas(self.window, width=720, height=480)
        self.canvas.grid(row=1, column=2, columnspan=3)  # General Grid

    def next_image(self):
        if self.controller.photo_id < len(self.controller.collection) - 1 :
            self.controller.photo_id += 1
            self.image_to_canvas = self.controller.prepared_image()
            self.canvas.itemconfig(self.canvas_image, image=self.image_to_canvas)

    def prev_image(self):
        if self.controller.photo_id != 0:
            self.controller.photo_id -= 1
            self.image_to_canvas = self.controller.prepared_image()
            self.canvas.itemconfig(self.canvas_image, image=self.image_to_canvas)

