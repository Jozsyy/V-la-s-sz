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

background_img = PhotoImage(file = f"Felhasznalo_Bejelentkezes_Background.png")
background = canvas.create_image(
    540.0, 303.5,
    image=background_img)

entry0_img = PhotoImage(file = f"Felhasznalo_Bejelentkezes_TextBox.png")
entry0_bg = canvas.create_image(
    540.0, 304.0,
    image = entry0_img)

entry0 = Entry(
    bd = 0,
    bg = "#d9d9d9",
    highlightthickness = 0)

entry0.place(
    x = 388, y = 272,
    width = 304,
    height = 62)

entry1_img = PhotoImage(file = f"Felhasznalo_Bejelentkezes_TextBox2.png")
entry1_bg = canvas.create_image(
    540.0, 459.0,
    image = entry1_img)

entry1 = Entry(
    bd = 0,
    bg = "#d9d9d9",
    highlightthickness = 0)

entry1.place(
    x = 388, y = 427,
    width = 304,
    height = 62)

img0 = PhotoImage(file = f"Felhasznalo_Bejelentkezes_Belepes.png")
b0 = Button(
    image = img0,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b0.place(
    x = 444, y = 508,
    width = 191,
    height = 65)

img1 = PhotoImage(file = f"Felhasznalo_Bejelentkezes_Vissza.png")
b1 = Button(
    image = img1,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b1.place(
    x = 667, y = 523,
    width = 178,
    height = 50)

window.resizable(False, False)
window.mainloop()
