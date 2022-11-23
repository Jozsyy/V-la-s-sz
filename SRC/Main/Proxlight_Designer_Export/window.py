from tkinter import *

import array as arr



def btn_clicked():
    print("Button Clicked")

def Admin_Kerdes_Kivalaszt():
       def selfDestroy():
           Admin_Kerdes_Kivalaszt_Szerkeszt_Button1.destroy()
           Admin_Kerdes_Kivalaszt_Szerkeszt_Button2.destroy()
           Admin_Kerdes_Kivalaszt_Szerkeszt_Button3.destroy()
           Admin_Kerdes_Kivalaszt_Szerkeszt_Button4.destroy()
           Admin_Kerdes_Kivalaszt_Vissza_Button.destroy()
           kategoria1_Label.destroy();

       background_img = PhotoImage(file=f"Admin_Kerdes_Kivalaszt_Background.png")
       background = canvas.create_image(
            540.0, 303.5,
            image=background_img)
       global kategoria1_Label
       kategoria1_Label = Label(window,text = "Tudományos",background="#201F93",fg="#FFFFFF",font=("Josefin Sans",20)).place(x = 274,y = 241)

       img0 = PhotoImage(file=f"Admin_Kerdes_Kivalaszt_Vissza.png")
       Admin_Kerdes_Kivalaszt_Vissza_Button = Button(
            image=img0,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: [selfDestroy(),Admin_Bejelentkezes()],
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
            command=lambda :[selfDestroy(),admin_kerdes_szerkeszt()],
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
            command=lambda :[selfDestroy(),admin_kerdes_szerkeszt()],
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
            command=lambda :[selfDestroy(),admin_kerdes_szerkeszt()],
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
            command=lambda :[selfDestroy(),admin_kerdes_szerkeszt()],
            relief="flat")

       Admin_Kerdes_Kivalaszt_Szerkeszt_Button4.place(
            x=55, y=389,
            width=150,
            height=36)






       window.resizable(False, False)
       window.mainloop()

def Admin_Bejelentkezes():

    def selfDestroy():
        Belep_Admin_button.destroy()
        Vissza_Admin_button.destroy()
        FelhasznaloNev_Entry.destroy()
        Jelszo_Entry.destroy()


    background_img = PhotoImage(file=f"Admin_background.png")
    background = canvas.create_image(
        540.0, 303.5,
        image=background_img)

    img0 = PhotoImage(file=f"Belep_Admin.png")
    Belep_Admin_button = Button(
        image=img0,
        borderwidth=0,
        highlightthickness=0,
        command=lambda :[selfDestroy(),Admin_Kerdes_Kivalaszt()],
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
        command= lambda :[selfDestroy(),Main_Menu()],
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

def Main_Menu():
    def selfDestroy():
        Bejelentkezes_Button.destroy()
        Regisztracio_button.destroy()
        Admin_Button.destroy()

    background_img = PhotoImage(file = f"background.png")
    background = canvas.create_image(
            540.0, 303.5,
            image=background_img)

    img0 = PhotoImage(file = f"img0.png")  ##bejelentkezes button.
    Bejelentkezes_Button = Button(
            image = img0,
            borderwidth = 0,
            highlightthickness = 0,
            command = lambda: [selfDestroy(),felhasznalo_bejelentkezes()],
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
            command =  lambda: [selfDestroy(),regisztracio()],
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
            command =  lambda: [selfDestroy(),Admin_Bejelentkezes()],
            relief = "flat")

    Admin_Button.place(
            x = 9, y = 8,
            width = 71,
            height = 63)

    window.resizable(False, False)
    window.mainloop()

def admin_kerdes_szerkeszt():
    def selfDestroy():
        Admin_Kerdes_Szerkeszt_Mentes_Button.destroy()
        Admin_Kerdes_Szerkeszt_Vissza_Button.destroy()
        Kerdes_Entry.destroy()
        Valasz_1_Entry.destroy()
        Valasz_2_Entry.destroy()
        Valasz_3_Entry.destroy()
        Valasz_4_Entry.destroy()
        oneButton.destroy()
        twoButton.destroy()
        threeButton.destroy()
        fourButton.destroy()

    background_img = PhotoImage(file=f"Admin_Kerdes_Szerkeszt.png")
    background = canvas.create_image(
        540.0, 303.5,
        image=background_img)

    img0 = PhotoImage(file=f"Admin_Kerdes_Szerkeszt_Mentes.png")
    Admin_Kerdes_Szerkeszt_Mentes_Button = Button(
        image=img0,
        borderwidth=0,
        highlightthickness=0,
        command=btn_clicked,
        relief="flat")

    Admin_Kerdes_Szerkeszt_Mentes_Button.place(
        x=426, y=497,
        width=228,
        height=96)

    img1 = PhotoImage(file=f"Admin_Kerdes_Szerkeszt_Vissza.png")
    Admin_Kerdes_Szerkeszt_Vissza_Button = Button(
        image=img1,
        borderwidth=0,
        highlightthickness=0,
        command=lambda :[selfDestroy(),Admin_Kerdes_Kivalaszt()],
        relief="flat")

    Admin_Kerdes_Szerkeszt_Vissza_Button.place(
        x=894, y=543,
        width=178,
        height=50)

    entry0_img = PhotoImage(file=f"Kerdes.png")
    entry0_bg = canvas.create_image(
        533.5, 177.5,
        image=entry0_img)

    Kerdes_Entry = Entry(
        bd=0,
        bg="#659cce",
        highlightthickness=0)

    Kerdes_Entry.place(
        x=148, y=110,
        width=771,
        height=133)

    entry1_img = PhotoImage(file=f"Valasz_1.png")
    entry1_bg = canvas.create_image(
        287.5, 343.0,
        image=entry1_img)

    Valasz_1_Entry= Entry(
        bd=0,
        bg="#659cce",
        highlightthickness=0)

    Valasz_1_Entry.place(
        x=84, y=322,
        width=407,
        height=40)

    entry2_img = PhotoImage(file=f"Valasz_2.png")
    entry2_bg = canvas.create_image(
        287.5, 429.0,
        image=entry2_img)

    Valasz_2_Entry = Entry(
        bd=0,
        bg="#659cce",
        highlightthickness=0)

    Valasz_2_Entry.place(
        x=84, y=408,
        width=407,
        height=40)

    entry3_img = PhotoImage(file=f"Valasz_3.png")
    entry3_bg = canvas.create_image(
        812.5, 343.0,
        image=entry3_img)

    Valasz_3_Entry = Entry(
        bd=0,
        bg="#659cce",
        highlightthickness=0)

    Valasz_3_Entry.place(
        x=609, y=322,
        width=407,
        height=40)

    entry4_img = PhotoImage(file=f"Valasz_4.png")
    entry4_bg = canvas.create_image(
        812.5, 429.0,
        image=entry4_img)

    Valasz_4_Entry = Entry(
        bd=0,
        bg="#659cce",
        highlightthickness=0)

    Valasz_4_Entry.place(
        x=609, y=408,
        width=407,
        height=40)

    img2 = PhotoImage(file=f"1.png")
    oneButton = Button(
        image=img2,
        borderwidth=0,
        highlightthickness=0,
        command=btn_clicked,
        relief="flat")

    oneButton.place(
        x=55, y=520,
        width=54,
        height=54)

    img3 = PhotoImage(file=f"2.png")
    twoButton = Button(
        image=img3,
        borderwidth=0,
        highlightthickness=0,
        command=btn_clicked,
        relief="flat")

    twoButton.place(
        x=119, y=520,
        width=54,
        height=54)

    img4 = PhotoImage(file=f"3.png")
    threeButton = Button(
        image=img4,
        borderwidth=0,
        highlightthickness=0,
        command=btn_clicked,
        relief="flat")

    threeButton.place(
        x=183, y=520,
        width=54,
        height=54)

    img5 = PhotoImage(file=f"4.png")
    fourButton = Button(
        image=img5,
        borderwidth=0,
        highlightthickness=0,
        command=btn_clicked,
        relief="flat")

    fourButton.place(
        x=247, y=520,
        width=54,
        height=54)

    window.resizable(False, False)
    window.mainloop()

def felhasznalo_bejelentkezes():
    def selfDestroy():
        FelhasznaloNev_Bejelentkezes_Entry.destroy()
        FelhasznaloJelszo_Bejelentkezes_Entry.destroy()
        Felhasznalo_Bejelentkezes_Belepes_Button.destroy()
        Felhasznalo_Bejelentkezes_Vissza_Button.destroy()

    background_img = PhotoImage(file=f"Felhasznalo_Bejelentkezes_Background.png")
    background = canvas.create_image(
        540.0, 303.5,
        image=background_img)

    entry0_img = PhotoImage(file=f"Felhasznalo_Bejelentkezes_TextBox.png")
    entry0_bg = canvas.create_image(
        540.0, 304.0,
        image=entry0_img)

    FelhasznaloNev_Bejelentkezes_Entry = Entry(
        bd=0,
        bg="#d9d9d9",
        highlightthickness=0)

    FelhasznaloNev_Bejelentkezes_Entry.place(
        x=388, y=272,
        width=304,
        height=62)

    entry1_img = PhotoImage(file=f"Felhasznalo_Bejelentkezes_TextBox2.png")
    entry1_bg = canvas.create_image(
        540.0, 459.0,
        image=entry1_img)

    FelhasznaloJelszo_Bejelentkezes_Entry = Entry(
        bd=0,
        bg="#d9d9d9",
        highlightthickness=0)

    FelhasznaloJelszo_Bejelentkezes_Entry.place(
        x=388, y=427,
        width=304,
        height=62)

    img0 = PhotoImage(file=f"Felhasznalo_Bejelentkezes_Belepes.png")
    Felhasznalo_Bejelentkezes_Belepes_Button = Button(
        image=img0,
        borderwidth=0,
        highlightthickness=0,
        command=lambda :[selfDestroy(),jatsz()],
        relief="flat")

    Felhasznalo_Bejelentkezes_Belepes_Button.place(
        x=444, y=508,
        width=191,
        height=65)

    img1 = PhotoImage(file=f"Felhasznalo_Bejelentkezes_Vissza.png")
    Felhasznalo_Bejelentkezes_Vissza_Button = Button(
        image=img1,
        borderwidth=0,
        highlightthickness=0,
        command=lambda :[selfDestroy(),Main_Menu()],
        relief="flat")

    Felhasznalo_Bejelentkezes_Vissza_Button.place(
        x=667, y=523,
        width=178,
        height=50)

    window.resizable(False, False)
    window.mainloop()

def regisztracio():
    def selfDestroy():
        Regisztracio_Regisztralas_Button.destroy()
        Regisztracio_Vissza_Button.destroy()
        Regisztracio_Jelszo_Entry.destroy()
        Regisztracio_Keresztnev_Entry.destroy()
        Regisztracio_Email_Entry.destroy()
        Regisztracio_VezetekNev_Entry.destroy()
        Regisztracio_FelhasznaloNev_Entry.destroy()
        Regisztracio_JelszoMegegyszer_Entry.destroy()

    background_img = PhotoImage(file=f"Regisztracio_Background.png")
    background = canvas.create_image(
        540.0, 303.5,
        image=background_img)

    img0 = PhotoImage(file=f"Regisztracio_Regisztralas.png")
    Regisztracio_Regisztralas_Button = Button(
        image=img0,
        borderwidth=0,
        highlightthickness=0,
        command= lambda: [selfDestroy(),sikeresRegisztracio()],
        relief="flat")

    Regisztracio_Regisztralas_Button .place(
        x=771, y=377,
        width=238,
        height=60)

    img1 = PhotoImage(file=f"Regisztracio_Vissza.png")
    Regisztracio_Vissza_Button = Button(
        image=img1,
        borderwidth=0,
        highlightthickness=0,
        command= lambda: [selfDestroy(),Main_Menu()],
        relief="flat")

    Regisztracio_Vissza_Button.place(
        x=801, y=466,
        width=178,
        height=50)

    entry0_img = PhotoImage(file=f"Regisztracio_TextBox.png")
    entry0_bg = canvas.create_image(
        341.0, 221.5,
        image=entry0_img)

    Regisztracio_VezetekNev_Entry = Entry(
        bd=0,
        bg="#ffffff",
        highlightthickness=0)

    Regisztracio_VezetekNev_Entry.place(
        x=207, y=201,
        width=268,
        height=39)

    entry1_img = PhotoImage(file=f"Regisztracio_TextBox2.png")
    entry1_bg = canvas.create_image(
        935.5, 315.5,
        image=entry1_img)

    Regisztracio_Keresztnev_Entry = Entry(
        bd=0,
        bg="#ffffff",
        highlightthickness=0)

    Regisztracio_Keresztnev_Entry .place(
        x=847, y=295,
        width=177,
        height=39)

    entry2_img = PhotoImage(file=f"Regisztracio_TextBox3.png")
    entry2_bg = canvas.create_image(
        341.0, 303.5,
        image=entry2_img)

    Regisztracio_FelhasznaloNev_Entry = Entry(
        bd=0,
        bg="#ffffff",
        highlightthickness=0)

    Regisztracio_FelhasznaloNev_Entry.place(
        x=207, y=283,
        width=268,
        height=39)

    entry3_img = PhotoImage(file=f"Regisztracio_TextBox4.png")
    entry3_bg = canvas.create_image(
        376.0, 393.5,
        image=entry3_img)

    Regisztracio_Email_Entry = Entry(
        bd=0,
        bg="#ffffff",
        highlightthickness=0)

    Regisztracio_Email_Entry.place(
        x=277, y=373,
        width=198,
        height=39)

    entry4_img = PhotoImage(file=f"Regisztracio_TextBox5.png")
    entry4_bg = canvas.create_image(
        821.0, 220.5,
        image=entry4_img)

    Regisztracio_Jelszo_Entry = Entry(
        bd=0,
        bg="#ffffff",
        highlightthickness=0)

    Regisztracio_Jelszo_Entry.place(
        x=685, y=200,
        width=272,
        height=39)

    entry5_img = PhotoImage(file=f"Regisztracio_TextBox6.png")
    entry5_bg = canvas.create_image(
        289.0, 493.5,
        image=entry5_img)

    Regisztracio_JelszoMegegyszer_Entry = Entry(
        bd=0,
        bg="#ffffff",
        highlightthickness=0)

    Regisztracio_JelszoMegegyszer_Entry .place(
        x=155, y=473,
        width=268,
        height=39)

    window.resizable(False, False)
    window.mainloop()

def sikeresRegisztracio():
    def selfDestroy():
        SikeresRegisztracio_Bejelentkezes_Button.destroy()
        SikeresRegisztracio_EXIT_Button.destroy()


    background_img = PhotoImage(file=f"SikeresRegisztracio_Backgr.png")
    background = canvas.create_image(
        540.0, 303.5,
        image=background_img)

    img0 = PhotoImage(file=f"EXIT.png")
    SikeresRegisztracio_EXIT_Button = Button(
        image=img0,
        borderwidth=0,
        highlightthickness=0,
        command=lambda :[selfDestroy(),Main_Menu()],
        relief="flat")

    SikeresRegisztracio_EXIT_Button.place(
        x=461, y=459,
        width=157,
        height=58)

    img1 = PhotoImage(file=f"SikeresRegisztracio_Bejelentkezes_Button.png")
    SikeresRegisztracio_Bejelentkezes_Button = Button(
        image=img1,
        borderwidth=0,
        highlightthickness=0,
        command=lambda :[selfDestroy(),felhasznalo_bejelentkezes()],
        relief="flat")

    SikeresRegisztracio_Bejelentkezes_Button.place(
        x=370, y=304,
        width=340,
        height=96)

    window.resizable(False, False)
    window.mainloop()

def kerdes(): #Robi
    def selfDestroy():
        Kerdes_Vege_Button.destroy()
        Kerdes_Mehet_Button.destroy()
        Kerdes_Tovabb_Button.destroy()
        valasz1_button.destroy()
        valasz2_button.destroy()
        valasz3_button.destroy()
        valasz4_button.destroy()


    img2 = PhotoImage(file=f"Kerdes_Tovabb.png")
    Kerdes_Tovabb_Button = Button(
        image=img2,
        borderwidth=0,
        highlightthickness=0,
        command=btn_clicked,
        relief="flat")

    Kerdes_Tovabb_Button.place(
        x=587, y=506,
        width=216,
        height=79)

    background_img = PhotoImage(file=f"Kerdes_Background.png")
    background = canvas.create_image(
            540.0, 303.5,
            image=background_img)

    img0 = PhotoImage(file=f"Kerdes_Vege.png")
    Kerdes_Vege_Button= Button(
            image=img0,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: [selfDestroy(),kategoriak_kivalaszt()],
            relief="flat")

    Kerdes_Vege_Button.place(
            x=894, y=547,
            width=173,
            height=46)

    img1 = PhotoImage(file=f"Kerdes_Mehet.png")
    Kerdes_Mehet_Button = Button(
            image=img1,
            borderwidth=0,
            highlightthickness=0,
            command=btn_clicked,
            relief="flat")

    Kerdes_Mehet_Button.place(
        x=289, y=506,
        width=209,
        height=79)

    img3 = PhotoImage(file=f"valasz1.png")
    valasz1_button = Button(
        image=img3,
        borderwidth=0,
        highlightthickness=0,
        command=btn_clicked,
        relief="flat")

    valasz1_button.place(
        x=34, y=315,
        width=480,
        height=56)

    img4 = PhotoImage(file=f"valasz3.png")
    valasz3_button = Button(
        image=img4,
        borderwidth=0,
        highlightthickness=0,
        command=btn_clicked,
        relief="flat")

    valasz3_button.place(
        x=566, y=315,
        width=480,
        height=56)

    img5 = PhotoImage(file=f"valasz2.png")
    valasz2_button = Button(
        image=img5,
        borderwidth=0,
        highlightthickness=0,
        command=btn_clicked,
        relief="flat")

    valasz2_button.place(
        x=34, y=401,
        width=480,
        height=56)

    img6 = PhotoImage(file=f"valasz4.png")
    valasz4_button = Button(
        image=img6,
        borderwidth=0,
        highlightthickness=0,
        command=btn_clicked,
        relief="flat")

    valasz4_button.place(
        x=566, y=401,
        width=480,
        height=56)

    window.resizable(False, False)
    window.mainloop()

def jatsz():  #Robi
    def csinaljuk(valaszt):
        if valaszt[0] == 1:
            print("Egyes volt kivalasztva")
        elif valaszt[1] == 1:
            print("Kettes volt kivalasztva")
        elif valaszt[2] == 1:
            print("Harmas volt kivalasztva")
        elif valaszt[3] == 1:
            print("Sajat volt kivalasztva"),

    valaszt = [arr.array('i', [0, 0, 0, 0]), ]

    def egyesAktiv():
        valaszt.insert(0, 1),
        valaszt.insert(1, 0),
        valaszt.insert(2, 0),
        valaszt.insert(3, 0),
        EgyesValaszt_Button.configure(background="#1F9393", activebackground="#1F9393"),
        KettesValaszt_Button.configure(background="#201F93", activebackground="#201F93"),
        HarmasValaszt_Button.configure(background="#201F93", activebackground="#201F93"),
        SajatValaszt_Button.configure(background="#201F93", activebackground="#201F93"),

    def kettesAktiv():
        valaszt.insert(0, 0),
        valaszt.insert(1, 1),
        valaszt.insert(2, 0),
        valaszt.insert(3, 0),
        EgyesValaszt_Button.configure(background="#201F93", activebackground="#201F93"),
        KettesValaszt_Button.configure(background="#1F9393", activebackground="#1F9393"),
        HarmasValaszt_Button.configure(background="#201F93", activebackground="#201F93"),
        SajatValaszt_Button.configure(background="#201F93", activebackground="#201F93"),

    def harmasAktiv():
        valaszt.insert(0, 0),
        valaszt.insert(1, 0),
        valaszt.insert(2, 1),
        valaszt.insert(3, 0),
        EgyesValaszt_Button.configure(background="#201F93", activebackground="#201F93"),
        KettesValaszt_Button.configure(background="#201F93", activebackground="#201F93"),
        HarmasValaszt_Button.configure(background="#1F9393", activebackground="#1F9393"),
        SajatValaszt_Button.configure(background="#201F93", activebackground="#201F93"),

    def sajatAktiv():
        valaszt.insert(0, 0),
        valaszt.insert(1, 0),
        valaszt.insert(2, 0),
        valaszt.insert(3, 1),
        EgyesValaszt_Button.configure(background="#201F93", activebackground="#201F93"),
        KettesValaszt_Button.configure(background="#201F93", activebackground="#201F93"),
        HarmasValaszt_Button.configure(background="#201F93", activebackground="#201F93"),
        SajatValaszt_Button.configure(background="#1F9393", activebackground="#1F9393"),


    def selfDestroy():
        Jatsz_Kijelentkezes_Button.destroy()
        Jatsz_Kezdes_Button.destroy()

    background_img = PhotoImage(file=f"Jatsz_Background.png")
    background = canvas.create_image(
        540.0, 303.5,
        image=background_img)

    img0 = PhotoImage(file=f"Jatsz_Kijelentkezes.png")
    Jatsz_Kijelentkezes_Button = Button(
        image=img0,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: [selfDestroy(),Main_Menu()],
        relief="flat")

    Jatsz_Kijelentkezes_Button.place(
        x=461, y=448,
        width=157,
        height=58)

    img1 = PhotoImage(file=f"Jatsz_Kezdes.png")
    Jatsz_Kezdes_Button = Button(
        image=img1,
        borderwidth=0,
        highlightthickness=0,
        command= lambda: [selfDestroy(),kategoriak_kivalaszt()],
        relief="flat")

    Jatsz_Kezdes_Button.place(
        x=426, y=304,
        width=228,
        height=96)

    window.resizable(False, False)
    window.mainloop()

def kategoriak_kivalaszt():  #Robi

    def csinaljuk(valaszt):
        if valaszt[0]==1:
            print("Egyes volt kivalasztva")
        elif valaszt[1]==1:
            print("Kettes volt kivalasztva")
        elif valaszt[2]==1:
            print("Harmas volt kivalasztva")
        elif valaszt[3]==1:
            print("Sajat volt kivalasztva"),


    valaszt = [arr.array('i', [0, 0, 0, 0]), ]

    def egyesAktiv():
        valaszt.insert(0, 1),
        valaszt.insert(1, 0),
        valaszt.insert(2, 0),
        valaszt.insert(3, 0),
        EgyesValaszt_Button.configure(background="#1F9393",activebackground="#1F9393"),
        KettesValaszt_Button.configure(background="#201F93",activebackground="#201F93"),
        HarmasValaszt_Button.configure(background="#201F93",activebackground="#201F93"),
        SajatValaszt_Button.configure(background="#201F93",activebackground="#201F93"),

    def kettesAktiv():
        valaszt.insert(0, 0),
        valaszt.insert(1, 1),
        valaszt.insert(2, 0),
        valaszt.insert(3, 0),
        EgyesValaszt_Button.configure(background="#201F93", activebackground="#201F93"),
        KettesValaszt_Button.configure(background="#1F9393", activebackground="#1F9393"),
        HarmasValaszt_Button.configure(background="#201F93", activebackground="#201F93"),
        SajatValaszt_Button.configure(background="#201F93", activebackground="#201F93"),

    def harmasAktiv():
        valaszt.insert(0, 0),
        valaszt.insert(1, 0),
        valaszt.insert(2, 1),
        valaszt.insert(3, 0),
        EgyesValaszt_Button.configure(background="#201F93", activebackground="#201F93"),
        KettesValaszt_Button.configure(background="#201F93", activebackground="#201F93"),
        HarmasValaszt_Button.configure(background="#1F9393", activebackground="#1F9393"),
        SajatValaszt_Button.configure(background="#201F93", activebackground="#201F93"),

    def sajatAktiv():
        valaszt.insert(0, 0),
        valaszt.insert(1, 0),
        valaszt.insert(2, 0),
        valaszt.insert(3, 1),
        EgyesValaszt_Button.configure(background="#201F93", activebackground="#201F93"),
        KettesValaszt_Button.configure(background="#201F93", activebackground="#201F93"),
        HarmasValaszt_Button.configure(background="#201F93", activebackground="#201F93"),
        SajatValaszt_Button.configure(background="#1F9393", activebackground="#1F9393"),




    def selfDestroy():
        Kategoriak_Vissza_Button.destroy()
        Kategoriak_Szerkeszt_Button.destroy()
        Kategoriak_Inditas_Button.destroy()
        EgyesValaszt_Button.destroy()
        KettesValaszt_Button.destroy()
        HarmasValaszt_Button.destroy()
        SajatValaszt_Button.destroy()


    background_img = PhotoImage(file=f"Kategoriak_Background.png")

    background = canvas.create_image(
            540.0, 303.5,
            image=background_img)

    img0 = PhotoImage(file=f"Kategoriak_Vissza.png")
    Kategoriak_Vissza_Button = Button(
            image=img0,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: [selfDestroy(),jatsz()],
            relief="flat")

    Kategoriak_Vissza_Button.place(
            x=894, y=543,
            width=178,
            height=50)

    img1 = PhotoImage(file=f"Kategoriak_Szerkeszt.png")
    Kategoriak_Szerkeszt_Button = Button(
            image=img1,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: [selfDestroy(),felhasznalo_kerdes_szerk()],
            relief="flat")

    Kategoriak_Szerkeszt_Button.place(
            x=894, y=368,
            width=142,
            height=37)

    img2 = PhotoImage(file=f"Kategoriak_Inditas.png")
    Kategoriak_Inditas_Button = Button(
            image=img2,
            borderwidth=0,
            highlightthickness=0,

            command=lambda: [csinaljuk(valaszt),selfDestroy(),kerdes()],

            relief="flat")

    Kategoriak_Inditas_Button.place(
            x=426, y=429,
            width=228,
            height=96)

    img3 = PhotoImage(file=f"EgyesValaszt.png")
    EgyesValaszt_Button = Button(

        text="Tudományos",
        font=("Josefin Sans",20),
        bg = "#201F93",
        fg = "white",
        activebackground="#201F93",
        activeforeground="white",
        borderwidth=0,
        highlightthickness=0,
        command=lambda :[egyesAktiv()],
        relief="flat")

    EgyesValaszt_Button.place(
        x=34, y=213,
        width=480,
        height=56)

    img4 = PhotoImage(file=f"HarmasValaszt.png")
    HarmasValaszt_Button = Button(
        text="Sport",
        font=("Josefin Sans", 20),
        bg="#201F93",
        fg="white",
        activebackground="#201F93",
        activeforeground="white",
        borderwidth=0,
        highlightthickness=0,
        command=lambda :[harmasAktiv()],
        relief="flat")

    HarmasValaszt_Button.place(
        x=566, y=213,
        width=480,
        height=56)

    img5 = PhotoImage(file=f"KettesValaszt.png")
    KettesValaszt_Button = Button(
        text="Történelem",
        font=("Josefin Sans", 20),
        bg="#201F93",
        fg="white",
        activebackground="#201F93",
        activeforeground="white",
        borderwidth=0,
        highlightthickness=0,
        command=lambda :[kettesAktiv()],
        relief="flat")

    KettesValaszt_Button.place(
        x=34, y=304,
        width=480,
        height=56)

    img6 = PhotoImage(file=f"SajatValaszt.png")
    SajatValaszt_Button = Button(
        text="Saját",
        font=("Josefin Sans", 20),
        bg="#201F93",
        fg="white",
        activeforeground="white",
        activebackground="#201F93",
        borderwidth=0,
        highlightthickness=0,
        command=lambda :[sajatAktiv()],
        relief="flat")

    SajatValaszt_Button.place(
        x=566, y=304,
        width=480,
        height=56)

    window.resizable(False, False)
    window.mainloop()

def felhasznalo_kerdes_szerk(): #Robi
    def selfDestroy():
        Felhasznalo_Kerdes_Szerkesztes_Mentes_Button.destroy()
        Felhasznalo_Kerdes_Szerkesztes_Vissza_Button.destroy()
        Kerdes_Entry.destroy()
        Valasz_1_Entry.destroy()
        Valasz_2_Entry.destroy()
        Valasz_3_Entry.destroy()
        Valasz_4_Entry.destroy()
        Felhasznalo_Kerdes_Szerkesztes_Mentes_Button.destroy()
        Felhasznalo_Kerdes_Szerkesztes_Vissza_Button.destroy()
        oneButton.destroy()
        twoButton.destroy()
        threeButton.destroy()
        fourButton.destroy()


    background_img = PhotoImage(file=f"Felhasznalo_Kerdes_Szerkesztes_Background.png")
    background = canvas.create_image(
        540.0, 303.5,
        image=background_img)

    img0 = PhotoImage(file=f"Felhasznalo_Kerdes_Szerkesztes_Mentes.png")
    Felhasznalo_Kerdes_Szerkesztes_Mentes_Button = Button(
        image=img0,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: [selfDestroy(),kategoriak_kivalaszt()],
        relief="flat")

    Felhasznalo_Kerdes_Szerkesztes_Mentes_Button .place(
        x=426, y=497,
        width=228,
        height=96)

    img1 = PhotoImage(file=f"Felhasznalo_Kerdes_Szerkesztes_Vissza.png")
    Felhasznalo_Kerdes_Szerkesztes_Vissza_Button = Button(
        image=img1,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: [selfDestroy(),kategoriak_kivalaszt()],
        relief="flat")

    Felhasznalo_Kerdes_Szerkesztes_Vissza_Button.place(
        x=894, y=543,
        width=178,
        height=50)

    entry0_img = PhotoImage(file=f"Kerdes.png")
    entry0_bg = canvas.create_image(
        533.5, 177.5,
        image=entry0_img)

    Kerdes_Entry = Entry(
        bd=0,
        bg="#659cce",
        highlightthickness=0)

    Kerdes_Entry.place(
        x=148, y=110,
        width=771,
        height=133)

    entry1_img = PhotoImage(file=f"Valasz_1.png")
    entry1_bg = canvas.create_image(
        287.5, 343.0,
        image=entry1_img)

    Valasz_1_Entry = Entry(
        bd=0,
        bg="#659cce",
        highlightthickness=0)

    Valasz_1_Entry.place(
        x=84, y=322,
        width=407,
        height=40)

    entry2_img = PhotoImage(file=f"Valasz_2.png")
    entry2_bg = canvas.create_image(
        287.5, 429.0,
        image=entry2_img)

    Valasz_2_Entry = Entry(
        bd=0,
        bg="#659cce",
        highlightthickness=0)

    Valasz_2_Entry.place(
        x=84, y=408,
        width=407,
        height=40)

    entry3_img = PhotoImage(file=f"Valasz_3.png")
    entry3_bg = canvas.create_image(
        812.5, 343.0,
        image=entry3_img)

    Valasz_3_Entry = Entry(
        bd=0,
        bg="#659cce",
        highlightthickness=0)

    Valasz_3_Entry.place(
        x=609, y=322,
        width=407,
        height=40)

    entry4_img = PhotoImage(file=f"Valasz_4.png")
    entry4_bg = canvas.create_image(
        812.5, 429.0,
        image=entry4_img)

    Valasz_4_Entry = Entry(
        bd=0,
        bg="#659cce",
        highlightthickness=0)

    Valasz_4_Entry.place(
        x=609, y=408,
        width=407,
        height=40)

    img2 = PhotoImage(file=f"1.png")
    oneButton = Button(
        image=img2,
        borderwidth=0,
        highlightthickness=0,
        command=btn_clicked,
        relief="flat")

    oneButton.place(
        x=55, y=520,
        width=54,
        height=54)

    img3 = PhotoImage(file=f"2.png")
    twoButton = Button(
        image=img3,
        borderwidth=0,
        highlightthickness=0,
        command=btn_clicked,
        relief="flat")

    twoButton.place(
        x=119, y=520,
        width=54,
        height=54)

    img4 = PhotoImage(file=f"3.png")
    threeButton = Button(
        image=img4,
        borderwidth=0,
        highlightthickness=0,
        command=btn_clicked,
        relief="flat")

    threeButton.place(
        x=183, y=520,
        width=54,
        height=54)

    img5 = PhotoImage(file=f"4.png")
    fourButton = Button(
        image=img5,
        borderwidth=0,
        highlightthickness=0,
        command=btn_clicked,
        relief="flat")

    fourButton.place(
        x=247, y=520,
        width=54,
        height=54)

    window.resizable(False, False)
    window.mainloop()  #Robi



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

Main_Menu()