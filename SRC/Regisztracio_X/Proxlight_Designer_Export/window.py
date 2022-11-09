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

background_img = PhotoImage(file = f"Regisztracio_Background.png")
background = canvas.create_image(
    540.0, 303.5,
    image=background_img)

img0 = PhotoImage(file = f"Regisztracio_Regisztralas.png")
b0 = Button(
    image = img0,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b0.place(
    x = 771, y = 377,
    width = 238,
    height = 60)

img1 = PhotoImage(file = f"Regisztracio_Vissza.png")
b1 = Button(
    image = img1,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b1.place(
    x = 801, y = 466,
    width = 178,
    height = 50)

entry0_img = PhotoImage(file = f"Regisztracio_TextBox.png")
entry0_bg = canvas.create_image(
    341.0, 221.5,
    image = entry0_img)

entry0 = Entry(
    bd = 0,
    bg = "#ffffff",
    highlightthickness = 0)

entry0.place(
    x = 207, y = 201,
    width = 268,
    height = 39)

entry1_img = PhotoImage(file = f"Regisztracio_TextBox2.png")
entry1_bg = canvas.create_image(
    935.5, 315.5,
    image = entry1_img)

entry1 = Entry(
    bd = 0,
    bg = "#ffffff",
    highlightthickness = 0)

entry1.place(
    x = 847, y = 295,
    width = 177,
    height = 39)

entry2_img = PhotoImage(file = f"Regisztracio_TextBox3.png")
entry2_bg = canvas.create_image(
    341.0, 303.5,
    image = entry2_img)

entry2 = Entry(
    bd = 0,
    bg = "#ffffff",
    highlightthickness = 0)

entry2.place(
    x = 207, y = 283,
    width = 268,
    height = 39)

entry3_img = PhotoImage(file = f"Regisztracio_TextBox4.png")
entry3_bg = canvas.create_image(
    376.0, 393.5,
    image = entry3_img)

entry3 = Entry(
    bd = 0,
    bg = "#ffffff",
    highlightthickness = 0)

entry3.place(
    x = 277, y = 373,
    width = 198,
    height = 39)

entry4_img = PhotoImage(file = f"Regisztracio_TextBox5.png")
entry4_bg = canvas.create_image(
    821.0, 220.5,
    image = entry4_img)

entry4 = Entry(
    bd = 0,
    bg = "#ffffff",
    highlightthickness = 0)

entry4.place(
    x = 685, y = 200,
    width = 272,
    height = 39)

entry5_img = PhotoImage(file = f"Regisztracio_TextBox6.png")
entry5_bg = canvas.create_image(
    289.0, 493.5,
    image = entry5_img)

entry5 = Entry(
    bd = 0,
    bg = "#ffffff",
    highlightthickness = 0)

entry5.place(
    x = 155, y = 473,
    width = 268,
    height = 39)

window.resizable(False, False)
window.mainloop()
