
from tkinter import *
from tkinter import ttk, filedialog
from tkinter.messagebox import showinfo


def motion(event):
    x, y = event.x, event.y
    print('{}, {}'.format(x, y))


def upload_images():
    filetypes = [
      ("image", ".jpeg"),
      ("image", ".png"),
      ("image", ".jpg"),
   ]

    filenames = filedialog.askopenfilenames(
        title='Open files',
        initialdir='/',
        filetypes=filetypes)

    showinfo(title='Selected Files',message=filenames)


window = Tk()
window.geometry("1080x800")
window.title("Simple Watermark Software")
window.bind('<Motion>', motion)

frm_controls_up = ttk.Frame(window, padding=10)
frm_controls_up.grid()
ttk.Label(frm_controls_up, text="upload your photo(s)").grid(column=0, row=0)
ttk.Button(frm_controls_up, text="Upload", command=upload_images).grid(row=0, column=1)
ttk.Button(frm_controls_up, text="Download").grid(row=0, column=2)

ttk.Button(frm_controls_up, text="Prev").grid(row=3, column=4)
ttk.Button(frm_controls_up, text="Next").grid(row=3, column=5)


frm_image = ttk.Frame(window, padding=10)

window.mainloop()