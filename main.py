from window import Main_Window

from tkinter.messagebox import showinfo
from PIL import ImageTk,Image



def display_image(collection , image_number):
    image_to_display = collection[image_number]
    print(image_to_display)
    image = Image.open(image_to_display)  # allows other image formats
    resized_image = image.resize((720, 480))  # Resizes the image
    img = ImageTk.PhotoImage(resized_image)
    return img





# window.bind('<Motion>', motion)



#Upper Buttons

#
#
#
#
# #images tuples
# image_number = 0
# collection=('test_img/1.jpg',"test_img/2.gif","test_img/3.jpg","test_img/4.jpg")
# collection_size = len(collection)
#
#
# #mid Frame(Image Canvas)

#
#
# #Initial image
# image_dis = display_image(collection,image_number)
# image_to_user = canvas.create_image(300, 300, image=image_dis)




main_window = Main_Window()
