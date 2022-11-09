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

background_img = PhotoImage(file = f"Admin_Kerdes_Valaszt_Background.png")
background = canvas.create_image(
    540.0, 303.5,
    image=background_img)

img0 = PhotoImage(file = f"Admin_Kerdes_Valaszt_Vissza.png")
b0 = Button(
    image = img0,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b0.place(
    x = 930, y = 544,
    width = 128,
    height = 50)

img1 = PhotoImage(file = f"Admin_Kerdes_Valaszt_Szerkeszt.png")
b1 = Button(
    image = img1,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b1.place(
    x = 55, y = 277,
    width = 150,
    height = 36)

img2 = PhotoImage(file = f"Admin_Kerdes_Valaszt_Szerkeszt2.png")
b2 = Button(
    image = img2,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b2.place(
    x = 879, y = 389,
    width = 150,
    height = 36)

img3 = PhotoImage(file = f"Admin_Kerdes_Valaszt_Szerkeszt3.png")
b3 = Button(
    image = img3,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b3.place(
    x = 879, y = 277,
    width = 150,
    height = 36)

img4 = PhotoImage(file = f"Admin_Kerdes_Valaszt_Szerkeszt4.png")
b4 = Button(
    image = img4,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b4.place(
    x = 55, y = 389,
    width = 150,
    height = 36)

window.resizable(False, False)
window.mainloop()
