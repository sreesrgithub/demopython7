from tkinter import *
import pyqrcode

from PIL import ImageTk, Image

root = Tk()


def generate():
    link_name = name_entry.get()
    link = link_entry.get()
    file_name = link_name + ".png"
    url= pyqrcode.create(link)
    url.png(file_name,scale=6)
    image= ImageTk.PhotoImage(Image.open(file_name))
    image_label = Label(image=image)
    image_label.image= image
    canvas.create_window(200,400,window=image_label)


canvas = Canvas(root, width=400, height=600)
canvas.pack()
app_label = Label(root, text="QR Code Generator", fg="Black", font='Georgia 20 bold underline')
canvas.create_window(200, 50, window=app_label)
name_entry = Entry(root)
canvas.create_window(200, 100, window=name_entry)
link_entry = Entry(root)
canvas.create_window(200, 160, window=link_entry)
name_label = Label(root, text="Link name", fg="black", font="TimesNewRoman")
canvas.create_window(200, 130, window=name_label)
link_label = Label(root, text="Link", fg="black", font="TimesNewRoman")
canvas.create_window(200, 190, window=link_label)
button = Button(text="Generate QR Code",command = generate)
canvas.create_window(200, 230, window=button)

root.mainloop()
