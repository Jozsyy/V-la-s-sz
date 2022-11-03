from tkinter import *

def btn_clicked():
    print("Button Clicked")


def Admin_Bejelentkezes():

    def Admin_Kerdes_Kivalaszt():
        Belep_Admin_button.destroy()
        Vissza_Admin_button.destroy()
        FelhasznaloNev_Entry.destroy()
        Jelszo_Entry.destroy()

        def destAdmin_Kerd_Szerk():
            Admin_Kerdes_Kivalaszt_Szerkeszt_Button1.destroy()
            Admin_Kerdes_Kivalaszt_Szerkeszt_Button2.destroy()
            Admin_Kerdes_Kivalaszt_Szerkeszt_Button3.destroy()
            Admin_Kerdes_Kivalaszt_Szerkeszt_Button4.destroy()
            Admin_Kerdes_Kivalaszt_Vissza_Button.destroy()

        background_img = PhotoImage(file=f"Admin_Kerdes_Kivalaszt_Background.png")
        background = canvas.create_image(
            540.0, 303.5,
            image=background_img)

        img0 = PhotoImage(file=f"Admin_Kerdes_Kivalaszt_Vissza.png")
        Admin_Kerdes_Kivalaszt_Vissza_Button = Button(
            image=img0,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: [destAdmin_Kerd_Szerk(),Admin_Bejelentkezes()],
            relief="flat")

        Admin_Kerdes_Kivalaszt_Vissza_Button.place(
            x=930, y=544,
            width=128,
            height=50)

        img1 = PhotoImage(file=f"Admin_Kerdes_Kivalaszt_Szerkeszt.png")
        Admin_Kerdes_Kivalaszt_Szerkeszt_Button1 = Button(
            image=img1,
            borderwidth=0,
            highlightthickness=0,
            command=btn_clicked,
            relief="flat")

        Admin_Kerdes_Kivalaszt_Szerkeszt_Button1.place(
            x=55, y=277,
            width=150,
            height=36)

        img2 = PhotoImage(file=f"Admin_Kerdes_Kivalaszt_Szerkeszt.png")
        Admin_Kerdes_Kivalaszt_Szerkeszt_Button2 = Button(
            image=img2,
            borderwidth=0,
            highlightthickness=0,
            command=btn_clicked,
            relief="flat")

        Admin_Kerdes_Kivalaszt_Szerkeszt_Button2.place(
            x=879, y=389,
            width=150,
            height=36)

        img3 = PhotoImage(file=f"Admin_Kerdes_Kivalaszt_Szerkeszt.png")
        Admin_Kerdes_Kivalaszt_Szerkeszt_Button3 = Button(
            image=img3,
            borderwidth=0,
            highlightthickness=0,
            command=btn_clicked,
            relief="flat")

        Admin_Kerdes_Kivalaszt_Szerkeszt_Button3.place(
            x=879, y=277,
            width=150,
            height=36)

        img4 = PhotoImage(file=f"Admin_Kerdes_Kivalaszt_Szerkeszt.png")
        Admin_Kerdes_Kivalaszt_Szerkeszt_Button4 = Button(
            image=img4,
            borderwidth=0,
            highlightthickness=0,
            command=btn_clicked,
            relief="flat")

        Admin_Kerdes_Kivalaszt_Szerkeszt_Button4.place(
            x=55, y=389,
            width=150,
            height=36)






        window.resizable(False, False)
        window.mainloop()

    Bejelentkezes_Button.destroy()
    Regisztracio_button.destroy()
    Admin_Button.destroy()



    background_img = PhotoImage(file=f"Admin_background.png")
    background = canvas.create_image(
        540.0, 303.5,
        image=background_img)

    img0 = PhotoImage(file=f"Belep_Admin.png")
    Belep_Admin_button = Button(
        image=img0,
        borderwidth=0,
        highlightthickness=0,
        command=Admin_Kerdes_Kivalaszt,
        relief="flat")

    Belep_Admin_button.place(
        x=444, y=508,
        width=191,
        height=65)

    img1 = PhotoImage(file=f"Vissza_Admin.png")
    Vissza_Admin_button = Button(
        image=img1,
        borderwidth=0,
        highlightthickness=0,
        command= btn_clicked,
        relief="flat")

    Vissza_Admin_button.place(
        x=680, y=516,
        width=178,
        height=50)

    FelhasznaloNev_Entry_img = PhotoImage(file=f"img_textBox_Admin (2).png")
    FelhasznaloNev_Entry_bg = canvas.create_image(
        539.5, 306.0,
        image=FelhasznaloNev_Entry_img)

    FelhasznaloNev_Entry = Entry(
        bd=0,
        bg="#d9d9d9",
        highlightthickness=0)

    FelhasznaloNev_Entry.place(
        x=399, y=282,
        width=281,
        height=46)

    Jelszo_Entry_img = PhotoImage(file=f"img_textBox_Admin.png")
    Jelszo_Entry_bg = canvas.create_image(
        539.5, 456.0,
        image=Jelszo_Entry_img)

    Jelszo_Entry = Entry(
        bd=0,
        bg="#d9d9d9",
        highlightthickness=0)

    Jelszo_Entry.place(
        x=399, y=432,
        width=281,
        height=46)

    window.resizable(False, False)
    window.mainloop()

#-------------------------------------------------

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



background_img = PhotoImage(file = f"background.png")
background = canvas.create_image(
        540.0, 303.5,
        image=background_img)

img0 = PhotoImage(file = f"img0.png")  ##bejelentkezes button.
Bejelentkezes_Button = Button(
        image = img0,
        borderwidth = 0,
        highlightthickness = 0,
        command = btn_clicked,
        relief = "flat")

Bejelentkezes_Button.place(
        x = 398, y = 253,
        width = 284,
        height = 102)

img1 = PhotoImage(file = f"img1.png")
Regisztracio_button = Button(
        image = img1,
        borderwidth = 0,
        highlightthickness = 0,
        command = btn_clicked,
        relief = "flat")

Regisztracio_button.place(
        x = 398, y = 411,
        width = 284,
        height = 100)

img2 = PhotoImage(file = f"img2.png")
Admin_Button = Button(
        image = img2,
        borderwidth = 0,
        highlightthickness = 0,
        command = Admin_Bejelentkezes,
        relief = "flat")

Admin_Button.place(
        x = 9, y = 8,
        width = 71,
        height = 63)

window.resizable(False, False)
window.mainloop()





