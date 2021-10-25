
def motion(event):
    x, y = event.x, event.y
    print('{}, {}'.format(x, y))





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