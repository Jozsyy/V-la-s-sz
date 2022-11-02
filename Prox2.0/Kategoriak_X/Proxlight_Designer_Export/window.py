from tkinter import *


def btn_clicked():
    print("Button Clicked")


window = Tk()

window.geometry("1080x607")
window.configure(bg = "#ffffff")
canvas = Canvas(
    window,
    bg = "#ffffff",
    height = 607,
    width = 1080,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
canvas.place(x = 0, y = 0)

background_img = PhotoImage(file = f"Kategoriak_Background.png")
background = canvas.create_image(
    540.0, 303.5,
    image=background_img)

img0 = PhotoImage(file = f"Kategoriak_Vissza.png")
b0 = Button(
    image = img0,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b0.place(
    x = 894, y = 543,
    width = 178,
    height = 50)

img1 = PhotoImage(file = f"Kategoriak_Szerkeszt.png")
b1 = Button(
    image = img1,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b1.place(
    x = 894, y = 368,
    width = 142,
    height = 37)

img2 = PhotoImage(file = f"Kategoriak_Inditas.png")
b2 = Button(
    image = img2,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b2.place(
    x = 426, y = 429,
    width = 228,
    height = 96)

window.resizable(False, False)
window.mainloop()
