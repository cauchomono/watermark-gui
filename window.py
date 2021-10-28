
from tkinter import ttk

from tkinter import *
from tkinter.filedialog import asksaveasfilename

from PIL import ImageTk, Image,ImageDraw, ImageFont
from tkinter.messagebox import showinfo
from tkinter import filedialog


class Main_Window():

    def __init__(self,):

        self.window = Tk()

        self.photo_id = 0
        self.collection = ('test_img/principal.jpg', 'test_img/principal.jpg')

        self.size = self.window.geometry("1280x720")
        self.title = self.window.title("Simple Watermark Software")

        self.above_controls()
        self.image_frame()
        self.image = self.open_image()
        self.image_to_canvas = self.prepared_image()



        self.canvas_image = self.canvas.create_image(300, 250, image=self.image_to_canvas)
        self.canvas.bind("<Motion>", self.motion)
        self.below_controls()

        self.window.mainloop()


    def above_controls(self):
        self.controls = ttk.Frame(self.window, padding=10)
        self.controls.grid(row=0, column=0)  # General Grid
        ttk.Button(self.controls, text="Upload",command = self.upload_images).grid(row=0, column=1)
        ttk.Button(self.controls, text="Download",command=self.download_images).grid(row=0, column=2)
        ttk.Button(self.controls, text="Watermark Text", command = self.text_options).grid(row=0, column=3)

    def below_controls(self):
        self.controls = ttk.Frame(self.window, padding=10)
        self.controls.grid(row=2, column=2, columnspan=2)  # General Grid
        ttk.Button(self.controls, text="Prev", command = self.prev_image).grid(row=0,column=5)
        ttk.Button(self.controls, text="Next", command = self.next_image).grid(row=0,column=6)
        ttk.Button(self.controls, text="Update", command=self.reset).grid(row=0, column=7)

    def image_frame(self):
        self.canvas = Canvas(self.window, width=720, height=480)
        self.canvas.grid(row=1, column=2, columnspan=3)  # General Grid
        self.canvas.bind("<Button-3>", func=self.clickPasteText)

    def next_image(self):
        if self.photo_id < len(self.collection) - 1 :
            self.photo_id += 1
            self.image = self.open_image()
            self.image_to_canvas = self.prepared_image()
            self.canvas.itemconfig(self.canvas_image, image=self.image_to_canvas)

    def prev_image(self):
        if self.photo_id != 0:
            self.photo_id -= 1
            self.image = self.open_image()
            self.image_to_canvas = self.prepared_image()
            self.canvas.itemconfig(self.canvas_image, image=self.image_to_canvas)


    def clickPasteText(self, event):

        self.watermark = ImageDraw.Draw(self.image)
        text = self.get_text_watermark()

        font = ImageFont.truetype('arial.ttf', 36)

        self.watermark.text((self.x, self.y), text, font=font)
        self.update()


    def text_options(self):
        self.newWindow = Toplevel(self.window)
        self.newWindow.title("Options")
        self.newWindow.geometry("320x320")
        Label(self.newWindow,text="Text").pack()
        self.watermark_entry = Entry(self.newWindow, )
        self.watermark_entry.pack()
        Button(self.newWindow, command=self.get_text_watermark, text="Accept").pack()
        instructions  = "1.Write your text in the message box\n" \
                        "2.Click in Accept  button\n" \
                        "3.Right click in the place where you want your watermark\n" \
                        "5.In the watermark app, click in download\n" \
                        "for the other photos repeat from 3 step. " \

        Label(self.newWindow, text=instructions).pack()


    def get_text_watermark(self):

        return self.watermark_entry.get()

    def open_image(self):
        image_to_display = self.collection[self.photo_id]
        print(image_to_display)
        self.image = Image.open(image_to_display)  # allows other image formats
        return self.image

    def prepared_image(self):

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
            self.reset()




    def download_images(self):
        file = asksaveasfilename(defaultextension=f".jpg", filetypes=[("All Files", "*.*"), ("PNG file", "*.png"), ("jpg file", "*.jpg")])
        if file:
            self.image.save(file)


    def motion (self,event):
        self.x,self.y = event.x, event.y

    def update(self):
        self.image_to_canvas = self.prepared_image()
        self.canvas.itemconfig(self.canvas_image, image=self.image_to_canvas)

    def reset(self):
        self.open_image()
        self.prepared_image()
        self.update()


