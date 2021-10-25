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
    if len(filenames) == 0:
        showinfo(title='Selected Files',message="No selected any file")
    else:
        showinfo(title='Selected Files', message=filenames)


def next_image():
    new_image = image_number + 1
    new_image_dis = display_image(collection, new_image)
    canvas.itemconfig(image_to_user,image=new_image_dis)
    return canvas

def prev_image():
    new_image = image_number - 1
    new_image_dis = display_image(collection, new_image)
    canvas.itemconfig(image_to_user, image=new_image_dis)
    return canvas