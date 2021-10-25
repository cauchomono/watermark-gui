from tkinter import *
from tkinter import ttk, filedialog

class Main_Window:

    def __init__(self):
        self.window = Tk()
        self.size = self.window.geometry("1280x720")
        self.title = self.window.title("Simple Watermark Software")
        self.above_controls()
        self.image_frame()
        self.below_controls()
        self.window.mainloop()


    def above_controls(self):
        self.controls = ttk.Frame(self.window, padding=10)
        self.controls.grid(row=0, column=0)  # General Grid
        ttk.Button(self.controls, text="Upload").grid(row=0, column=1)
        ttk.Button(self.controls, text="Download").grid(row=0, column=2)

    def below_controls(self):
        self.controls = ttk.Frame(self.window, padding=10)
        self.controls.grid(row=2, column=2, columnspan=2)  # General Grid
        ttk.Button(self.controls, text="Prev").grid(row=0,column=5)
        ttk.Button(self.controls, text="Next").grid(row=0,column=6)

    def image_frame(self):
        self.canvas = Canvas(self.window, width=720, height=480)
        self.canvas.grid(row=1, column=2, columnspan=3)  # General Grid

