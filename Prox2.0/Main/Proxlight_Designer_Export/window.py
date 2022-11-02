from tkinter import *




def btn_clicked():
    print("Button Clicked")

##Ez mindeniknel kozos
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


def Main_Menu():##Main_menu
    background_img = PhotoImage(file = f"background.png")
    background = canvas.create_image(
        540.0, 303.5,
        image=background_img)

    img0 = PhotoImage(file = f"img0.png")  ##bejelentkezes button.
    b0 = Button(
        image = img0,
        borderwidth = 0,
        highlightthickness = 0,
        command = btn_clicked,
        relief = "flat")

    b0.place(
        x = 398, y = 253,
        width = 284,
        height = 102)

    img1 = PhotoImage(file = f"img1.png")
    b1 = Button(
        image = img1,
        borderwidth = 0,
        highlightthickness = 0,
        command = btn_clicked,
        relief = "flat")

    b1.place(
        x = 398, y = 411,
        width = 284,
        height = 100)

    img2 = PhotoImage(file = f"img2.png")
    b2 = Button(
        image = img2,
        borderwidth = 0,
        highlightthickness = 0,
        command = Admin_Bejelentkezes,
        relief = "flat")

    b2.place(
        x = 9, y = 8,
        width = 71,
        height = 63)

    window.resizable(False, False)
    window.mainloop()
def Admin_Bejelentkezes():
    background_img = PhotoImage(file=f"Admin_background.png")
    background = canvas.create_image(
        540.0, 303.5,
        image=background_img)

    img0 = PhotoImage(file=f"Belep_Admin.png")
    b0 = Button(
        image=img0,
        borderwidth=0,
        highlightthickness=0,
        command=Admin_Kerdes_Kivalaszt,
        relief="flat")

    b0.place(
        x=444, y=508,
        width=191,
        height=65)

    img1 = PhotoImage(file=f"Vissza_Admin.png")
    b1 = Button(
        image=img1,
        borderwidth=0,
        highlightthickness=0,
        command= Main_Menu,
        relief="flat")

    b1.place(
        x=680, y=516,
        width=178,
        height=50)

    entry0_img = PhotoImage(file=f"img_textBox_Admin (2).png")
    entry0_bg = canvas.create_image(
        539.5, 306.0,
        image=entry0_img)

    entry0 = Entry(
        bd=0,
        bg="#d9d9d9",
        highlightthickness=0)

    entry0.place(
        x=399, y=282,
        width=281,
        height=46)

    entry1_img = PhotoImage(file=f"img_textBox_Admin.png")
    entry1_bg = canvas.create_image(
        539.5, 456.0,
        image=entry1_img)

    entry1 = Entry(
        bd=0,
        bg="#d9d9d9",
        highlightthickness=0)

    entry1.place(
        x=399, y=432,
        width=281,
        height=46)

    window.resizable(False, False)
    window.mainloop()
def Admin_Kerdes_Kivalaszt():
    background_img = PhotoImage(file=f"Admin_Kerdes_Kivalaszt_Background.png")
    background = canvas.create_image(
        540.0, 303.5,
        image=background_img)

    img0 = PhotoImage(file=f"Admin_Kerdes_Kivalaszt_Vissza.png")
    b0 = Button(
        image=img0,
        borderwidth=0,
        highlightthickness=0,
        command=Admin_Bejelentkezes,
        relief="flat")

    b0.place(
        x=930, y=544,
        width=128,
        height=50)

    img1 = PhotoImage(file=f"Admin_Kerdes_Kivalaszt_Szerkeszt.png")
    b1 = Button(
        image=img1,
        borderwidth=0,
        highlightthickness=0,
        command=btn_clicked,
        relief="flat")

    b1.place(
        x=55, y=277,
        width=150,
        height=36)

    img2 = PhotoImage(file=f"Admin_Kerdes_Kivalaszt_Szerkeszt.png")
    b2 = Button(
        image=img2,
        borderwidth=0,
        highlightthickness=0,
        command=btn_clicked,
        relief="flat")

    b2.place(
        x=879, y=389,
        width=150,
        height=36)

    img3 = PhotoImage(file=f"Admin_Kerdes_Kivalaszt_Szerkeszt.png")
    b3 = Button(
        image=img3,
        borderwidth=0,
        highlightthickness=0,
        command=btn_clicked,
        relief="flat")

    b3.place(
        x=879, y=277,
        width=150,
        height=36)

    img4 = PhotoImage(file=f"Admin_Kerdes_Kivalaszt_Szerkeszt.png")
    b4 = Button(
        image=img4,
        borderwidth=0,
        highlightthickness=0,
        command=btn_clicked,
        relief="flat")

    b4.place(
        x=55, y=389,
        width=150,
        height=36)

    window.resizable(False, False)
    window.mainloop()


Main_Menu()


