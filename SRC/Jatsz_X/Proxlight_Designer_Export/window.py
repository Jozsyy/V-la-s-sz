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

background_img = PhotoImage(file = f"Jatsz_Background.png")
background = canvas.create_image(
    540.0, 303.5,
    image=background_img)

img0 = PhotoImage(file = f"Jatsz_Kijelentkezes.png")
b0 = Button(
    image = img0,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b0.place(
    x = 461, y = 448,
    width = 157,
    height = 58)

img1 = PhotoImage(file = f"Jatsz_Kezdes.png")
b1 = Button(
    image = img1,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b1.place(
    x = 426, y = 304,
    width = 228,
    height = 96)

window.resizable(False, False)
window.mainloop()
