from tkinter import *
from tkinter import Label
import tkinter as tk
import array as arr
import pyrebase

#Pythonkod osszekotese az adatbazissal
config={
      "apiKey": "AIzaSyCVvp08oEuPrBFxEavuYOu7Nd9Hi1bo3Cw",
      "authDomain": "valassz-715f5.firebaseapp.com",
      "databaseURL": "https://valassz-715f5-default-rtdb.asia-southeast1.firebasedatabase.app",
      "projectId": "valassz-715f5",
      "storageBucket": "valassz-715f5.appspot.com",
      "messagingSenderId": "1078959352066",
      "appId": "1:1078959352066:web:e435a66a59064b2e4efa1b",
      "measurementId": "G-ZWK4BL98PZ",
      "databaseURL": "https://valassz-715f5-default-rtdb.asia-southeast1.firebasedatabase.app/"
}

firebase = pyrebase.initialize_app(config)
database = firebase.database()



def btn_clicked():
    print("Button Clicked")

def Admin_Kerdes_Kivalaszt():
       def selfDestroy():
           Admin_Kerdes_Kivalaszt_Szerkeszt_Button1.destroy()
           Admin_Kerdes_Kivalaszt_Szerkeszt_Button2.destroy()
           Admin_Kerdes_Kivalaszt_Szerkeszt_Button3.destroy()
           Admin_Kerdes_Kivalaszt_Szerkeszt_Button4.destroy()
           Admin_Kerdes_Kivalaszt_Vissza_Button.destroy()


       background_img = PhotoImage(file=f"Admin_Kerdes_Kivalaszt_Background.png")
       background = canvas.create_image(
            540.0, 303.5,
            image=background_img)


       #kategoria1_Label = Label(window,text = "Tudományos",background="#201F93",fg="#FFFFFF",font=("Josefin Sans",20)).place(x = 274,y = 241)



       img0 = PhotoImage(file=f"Admin_Kerdes_Kivalaszt_Vissza.png")
       Admin_Kerdes_Kivalaszt_Vissza_Button = Button(
            image=img0,
            borderwidth=0,
            highlightthickness=0,
            activebackground="#08082C",
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
            activebackground="#08082C",
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
            activebackground="#08082C",
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
            activebackground="#08082C",
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
            activebackground="#08082C",
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
        activebackground="#08082C",
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
        activebackground="#08082C",
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
        font=("Josefin Sans", 18),
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
        font=("Josefin Sans", 18),
        bd=0,
        bg="#d9d9d9",
        highlightthickness=0,
        show='*')

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




    background_img = PhotoImage(file=f"background.png")

    background = canvas.create_image(
        540.0, 303.5,
        image=background_img)

    img0 = PhotoImage(file = f"img0.png")  ##bejelentkezes button.
    Bejelentkezes_Button = Button(
            image = img0,
            borderwidth = 0,
            highlightthickness = 0,
            activebackground="#08082C",
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
            activebackground="#08082C",
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
            activebackground="#08082C",
            command =  lambda: [selfDestroy(),Admin_Bejelentkezes()],
            relief = "flat")

    Admin_Button.place(
            x = 9, y = 8,
            width = 71,
            height = 63)

    window.resizable(False, False)
    window.mainloop()

def admin_kerdes_szerkeszt():

    valaszt = arr.array('i', [0])
    alapSzin = "#659CCE"
    kivalSzin = "#201F93"
    def gombkivalaszt(gombszam):

        EgyesValaszt_Button.configure(background=alapSzin, activebackground=alapSzin),
        KettesValaszt_Button.configure(background=alapSzin, activebackground=alapSzin),
        HarmasValaszt_Button.configure(background=alapSzin, activebackground=alapSzin),
        NegyestValaszt_Button.configure(background=alapSzin, activebackground=alapSzin),

        if gombszam == 1:
            EgyesValaszt_Button.configure(background=kivalSzin, activebackground=kivalSzin),
            valaszt[0] = 1

        elif gombszam == 2:
            KettesValaszt_Button.configure(background=kivalSzin, activebackground=kivalSzin),
            valaszt[0] = 2


        elif gombszam == 3:
            HarmasValaszt_Button.configure(background=kivalSzin, activebackground=kivalSzin),
            valaszt[0] = 3
        elif gombszam == 4:
            NegyestValaszt_Button.configure(background=kivalSzin, activebackground=kivalSzin),
            valaszt[0] = 4

        Admin_Kerdes_Szerkeszt_Mentes_Button.configure(state=NORMAL)


    def csinaljuk():
        if valaszt[0]==int(1):
            print("Egyes volt kivalasztva")
        elif valaszt[0]== int(2):
            print("Kettes volt kivalasztva")
        elif valaszt[0]==int(3):
            print("Harmas volt kivalasztva")
        elif valaszt[0]==int(4):
            print("Negyes volt kivalasztva"),

    def selfDestroy():
        Admin_Kerdes_Szerkeszt_Mentes_Button.destroy()
        Admin_Kerdes_Szerkeszt_Vissza_Button.destroy()
        Kerdes_Entry.destroy()
        Valasz_1_Entry.destroy()
        Valasz_2_Entry.destroy()
        Valasz_3_Entry.destroy()
        Valasz_4_Entry.destroy()
        EgyesValaszt_Button.destroy()
        KettesValaszt_Button.destroy()
        HarmasValaszt_Button.destroy()
        NegyestValaszt_Button.destroy()

    background_img = PhotoImage(file=f"Admin_Kerdes_Szerkeszt.png")
    background = canvas.create_image(
        540.0, 303.5,
        image=background_img)

    img0 = PhotoImage(file=f"Admin_Kerdes_Szerkeszt_Mentes.png")
    Admin_Kerdes_Szerkeszt_Mentes_Button = Button(
        image=img0,
        borderwidth=0,
        highlightthickness=0,
        activebackground=kivalSzin,
        command=lambda: [csinaljuk(),selfDestroy(),Admin_Kerdes_Kivalaszt()],
        state=DISABLED,
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
        activebackground=kivalSzin,
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
        font=15,
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
    EgyesValaszt_Button = Button(
        text="1.",
        font=("Josefin Sans", 20, "bold"),
        bg=alapSzin,
        fg="black",
        activebackground=alapSzin,
        activeforeground="black",
        borderwidth=0,
        highlightthickness=0,
        command=lambda: [gombkivalaszt(1)],
        relief="flat"
    )

    EgyesValaszt_Button.place(
        x=55, y=520,
        width=54,
        height=54)

    img3 = PhotoImage(file=f"2.png")
    KettesValaszt_Button = Button(
        text="2.",
        font=("Josefin Sans", 20, "bold"),
        bg=alapSzin,
        fg="black",
        activebackground=alapSzin,
        activeforeground="black",
        borderwidth=0,
        highlightthickness=0,
        command=lambda: [gombkivalaszt(2)],
        relief="flat")

    KettesValaszt_Button.place(
        x=119, y=520,
        width=54,
        height=54)

    img4 = PhotoImage(file=f"3.png")
    HarmasValaszt_Button = Button(
        text="3.",
        font=("Josefin Sans", 20, "bold"),
        bg=alapSzin,
        fg="black",
        activebackground=alapSzin,
        activeforeground="black",
        borderwidth=0,
        highlightthickness=0,
        command=lambda: [gombkivalaszt(3)],
        relief="flat")

    HarmasValaszt_Button.place(
        x=183, y=520,
        width=54,
        height=54)

    img5 = PhotoImage(file=f"4.png")
    NegyestValaszt_Button = Button(
        text="4.",
        font=("Josefin Sans", 20, "bold"),
        bg=alapSzin,
        fg="black",
        activebackground=alapSzin,
        activeforeground="black",
        borderwidth=0,
        highlightthickness=0,
        command=lambda: [gombkivalaszt(4)],
        relief="flat")

    NegyestValaszt_Button.place(
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


    def verification():
        #Entrykbol kimentjuk az adatokat
        felhasznalonev=FelhasznaloNev_Bejelentkezes_Entry.get()
        jelszo=FelhasznaloJelszo_Bejelentkezes_Entry.get()

        #Felhasznalonevhez tartozo kod az adatbazisbol
        jelszoo=database.child("Felhasznalok").child(felhasznalonev).child("Jelszo").get().val()

        if jelszo == str(jelszoo):
           selfDestroy()
           jatsz(felhasznalonev)
        else:
            felhasznalo_bejelentkezes()




    background_img = PhotoImage(file=f"Felhasznalo_Bejelentkezes_Background.png")


    background = canvas.create_image(
      540.0, 303.5,
      image=background_img)

    entry0_img = PhotoImage(file=f"Felhasznalo_Bejelentkezes_TextBox.png")
    entry0_bg = canvas.create_image(
        540.0, 304.0,
        image=entry0_img)

    FelhasznaloNev_Bejelentkezes_Entry = Entry(
        font=("Josefin Sans", 18),
        bd=0,
        bg="#d9d9d9",
        highlightthickness=0)

    FelhasznaloNev_Bejelentkezes_Entry.place(
        x=399, y=282,
        width=281,
        height=46)

    entry1_img = PhotoImage(file=f"Felhasznalo_Bejelentkezes_TextBox2.png")
    entry1_bg = canvas.create_image(
        540.0, 459.0,
        image=entry1_img)

    FelhasznaloJelszo_Bejelentkezes_Entry = Entry(
        font=("Josefin Sans", 18),
        bd=0,
        bg="#d9d9d9",
        highlightthickness=0,
        show='*')

    FelhasznaloJelszo_Bejelentkezes_Entry.place(
        x=399, y=432,
        width=281,
        height=46)

    img0 = PhotoImage(file=f"Felhasznalo_Bejelentkezes_Belepes.png")
    Felhasznalo_Bejelentkezes_Belepes_Button = Button(
        image=img0,
        borderwidth=0,
        highlightthickness=0,

        activebackground="#08082C",

        command = lambda: [verification(), selfDestroy()],

        relief="flat")

    Felhasznalo_Bejelentkezes_Belepes_Button.place(
        x=444, y=508,
        width=191,
        height=65)

    img1 = PhotoImage(file=f"Felhasznalo_Bejelentkezes_Vissza.png")
    Felhasznalo_Bejelentkezes_Vissza_Button = Button(
        image=img1,
        borderwidth=0,
        activebackground="#08082C",
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

    def save():
        #Az adatokat elmentjuk az adatbazisba
        vezeteknev = Regisztracio_VezetekNev_Entry.get()
        keresztnev = Regisztracio_Keresztnev_Entry.get()
        felhasznalonev = Regisztracio_FelhasznaloNev_Entry.get()
        email = Regisztracio_Email_Entry.get()
        jelszo = Regisztracio_Jelszo_Entry.get()
        jelszo2 = Regisztracio_JelszoMegegyszer_Entry.get()
        if jelszo!=jelszo2:
            #Hiba ablak
            print("A ket jelszo nem ugyanaz")

        Felhasznalok = database.child("Felhasznalok").get().val()
        id=len(Felhasznalok)+1

        #email megerosites
        auth = firebase.auth()
        auth.create_user_with_email_and_password(email,jelszo)
        user = auth.sign_in_with_email_and_password(email, jelszo)
        auth.send_email_verification(user['idToken'])

        felhasznalo = {"Felhasznalo_ID": id, "Vezeteknev": vezeteknev, "Keresztnev": keresztnev,
                        "Felhasznalonev":felhasznalonev, "Jelszo": jelszo,"Email": email, "Pontszam": "0"}
        database.child("Felhasznalok").child(felhasznalonev).set(felhasznalo)


    background_img = PhotoImage(file=f"Regisztracio_Background.png")


    background = canvas.create_image(
        540.0, 303.5,
        image=background_img)

    img0 = PhotoImage(file=f"Regisztracio_Regisztralas.png")
    Regisztracio_Regisztralas_Button = Button(
        image=img0,
        borderwidth=0,
        highlightthickness=0,
        activebackground="#08082C",
        command= lambda: [save(),selfDestroy(),sikeresRegisztracio()],
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
        activebackground="#08082C",
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
        font=("Josefin Sans",18),
        bd=0,
        bg="#ffffff",
        highlightthickness=0)

    Regisztracio_VezetekNev_Entry.place(
        x=207, y=205,
        width=268,
        height=39)

    entry1_img = PhotoImage(file=f"Regisztracio_TextBox2.png")
    entry1_bg = canvas.create_image(
        935.5, 315.5,
        image=entry1_img)

    Regisztracio_Keresztnev_Entry = Entry(
        font=("Josefin Sans", 18),
        bd=0,
        bg="#ffffff",
        highlightthickness=0)

    Regisztracio_Keresztnev_Entry.place(
        x=207, y=288,
        width=268,
        height=39)

    entry2_img = PhotoImage(file=f"Regisztracio_TextBox3.png")
    entry2_bg = canvas.create_image(
        341.0, 303.5,
        image=entry2_img)

    Regisztracio_FelhasznaloNev_Entry = Entry(
        font=("Josefin Sans", 18),
        bd=0,
        bg="#ffffff",
        highlightthickness=0)

    Regisztracio_FelhasznaloNev_Entry.place(
        x=262, y=376,
        width=198,
        height=39)

    entry3_img = PhotoImage(file=f"Regisztracio_TextBox4.png")
    entry3_bg = canvas.create_image(
        376.0, 393.5,
        image=entry3_img)

    Regisztracio_Email_Entry = Entry(
        font=("Josefin Sans", 18),
        bd=0,
        bg="#ffffff",
        highlightthickness=0)

    Regisztracio_Email_Entry.place(
        x=145, y=478,
        width=345,
        height=39)

    entry4_img = PhotoImage(file=f"Regisztracio_TextBox5.png")
    entry4_bg = canvas.create_image(
        821.0, 220.5,
        image=entry4_img)

    Regisztracio_Jelszo_Entry = Entry(
        font=("Josefin Sans", 18),
        bd=0,
        bg="#ffffff",
        highlightthickness=0,
        show='*')

    Regisztracio_Jelszo_Entry.place(
        x=670, y=205,
        width=272,
        height=39)

    entry5_img = PhotoImage(file=f"Regisztracio_TextBox6.png")
    entry5_bg = canvas.create_image(
        289.0, 493.5,
        image=entry5_img)

    Regisztracio_JelszoMegegyszer_Entry = Entry(
        font=("Josefin Sans", 18),
        bd=0,
        bg="#ffffff",
        highlightthickness=0,
        show='*')

    Regisztracio_JelszoMegegyszer_Entry.place(
        x=838, y=300,
        width=177,
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
        activebackground="#08082C",
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
        activebackground="#08082C",
        command=lambda :[selfDestroy(),felhasznalo_bejelentkezes()],
        relief="flat")

    SikeresRegisztracio_Bejelentkezes_Button.place(
        x=370, y=304,
        width=340,
        height=96)

    window.resizable(False, False)
    window.mainloop()

def kerdes(felhasznalonev): #Robi

    pontszam = database.child("Felhasznalok").child(felhasznalonev).child("Pontszam").get().val()
    valaszt = arr.array('i', [0])
    alapSzin = "#659CCE"
    kivalSzin = "#1F9393"

    def gombkivalaszt(gombszam):

        valasz1_button.configure(background=alapSzin, activebackground=alapSzin),
        valasz2_button.configure(background=alapSzin, activebackground=alapSzin),
        valasz3_button.configure(background=alapSzin, activebackground=alapSzin),
        valasz4_button.configure(background=alapSzin, activebackground=alapSzin),

        if gombszam == 1:
            valasz1_button.configure(background=kivalSzin, activebackground=kivalSzin),
            valaszt[0] = 1
        elif gombszam == 2:
            valasz2_button.configure(background=kivalSzin, activebackground=kivalSzin),
            valaszt[0] = 2
        elif gombszam == 3:
            valasz3_button.configure(background=kivalSzin, activebackground=kivalSzin),
            valaszt[0] = 3
        elif gombszam == 4:
            valasz4_button.configure(background=kivalSzin, activebackground=kivalSzin),
            valaszt[0] = 4

        Kerdes_Mehet_Button.configure(state=NORMAL),

    def csinaljuk():
        if valaszt[0] == int(1):
            print("Egyes volt kivalasztva")
        elif valaszt[0] == int(2):
            print("Kettes volt kivalasztva")
        elif valaszt[0] == int(3):
            print("Harmas volt kivalasztva")
        elif valaszt[0] == int(4):
            print("Negyes volt kivalasztva"),

    def selfDestroy():
        Kerdes_Vege_Button.destroy()
        Kerdes_Mehet_Button.destroy()
        Kerdes_Tovabb_Button.destroy()
        valasz1_button.destroy()
        valasz2_button.destroy()
        valasz3_button.destroy()
        valasz4_button.destroy()

        pontszam_label.destroy()

    pontszam_label = Label(text=pontszam, font=("Josefin Sans", 20), bg="#18115E", fg="#F39C29")
    pontszam_label.place(x = 180,y = 19)


    img2 = PhotoImage(file=f"Kerdes_Tovabb.png")
    Kerdes_Tovabb_Button = Button(
        image=img2,
        borderwidth=0,
        highlightthickness=0,
        activebackground="#08082C",
        command=lambda :[selfDestroy(),kerdes(felhasznalonev)],
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
            activebackground="#08082C",
            highlightthickness=0,
            command=lambda: [selfDestroy(),kategoriak_kivalaszt(felhasznalonev)],
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
            state=DISABLED,
            activebackground="#08082C",
            command=lambda :[csinaljuk(),selfDestroy(),kerdes(felhasznalonev)],
            relief="flat")

    Kerdes_Mehet_Button.place(
        x=289, y=506,
        width=209,
        height=79)

    img3 = PhotoImage(file=f"valasz1.png")
    valasz1_button = Button(
        text="Valasz1",
        font=("Josefin Sans", 20),
        bg=alapSzin,
        fg="black",
        activebackground=alapSzin,
        activeforeground="black",
        borderwidth=0,
        highlightthickness=0,
        command=lambda: [gombkivalaszt(1)],
        relief="flat")

    valasz1_button.place(
        x=34, y=315,
        width=480,
        height=58)

    img4 = PhotoImage(file=f"valasz3.png")
    valasz3_button = Button(
        text="Valasz3",
        font=("Josefin Sans", 20),
        bg=alapSzin,
        fg="black",
        activebackground=alapSzin,
        activeforeground="black",
        borderwidth=0,
        highlightthickness=0,
        command=lambda: [gombkivalaszt(3)],
        relief="flat")

    valasz3_button.place(
        x=566, y=315,
        width=480,
        height=58)

    img5 = PhotoImage(file=f"valasz2.png")
    valasz2_button = Button(
        text="Valasz2",
        font=("Josefin Sans", 20),
        bg=alapSzin,
        fg="black",
        activebackground=alapSzin,
        activeforeground="black",
        borderwidth=0,
        highlightthickness=0,
        command=lambda: [gombkivalaszt(2)],
        relief="flat")

    valasz2_button.place(
        x=34, y=401,
        width=480,
        height=58)





    img6 = PhotoImage(file=f"valasz4.png")
    valasz4_button = Button(
        text="Valasz4",
        font=("Josefin Sans", 20),
        bg=alapSzin,
        fg="black",
        activebackground=alapSzin,
        activeforeground="black",
        borderwidth=0,
        highlightthickness=0,
        command=lambda: [gombkivalaszt(4)],
        relief="flat"
        )

    valasz4_button.place(
        x=566, y=401,
        width=480,
        height=58)

    window.resizable(False, False)
    window.mainloop()

def jatsz(felhasznalonev):  #Robi

    pontszam = database.child("Felhasznalok").child(felhasznalonev).child("Pontszam").get().val()

    def selfDestroy():
        Jatsz_Kijelentkezes_Button.destroy()
        Jatsz_Kezdes_Button.destroy()
        pontszam_label.destroy()
        felhasznaloNev_label.destroy()

    background_img = PhotoImage(file=f"Jatsz_Background.png")
    background = canvas.create_image(
        540.0, 303.5,
        image=background_img)

    pontszam_label = Label(text=pontszam,
                   font=("Josefin Sans", 20),
                   bg="#18115E",
                   fg="#F39C29")


    pontszam_label.place(x = 190,y = 62)

    felhasznaloNev_label = Label(
                    text=felhasznalonev,
                   font=("Josefin Sans", 20),
                   bg="#18115E",
                   fg="#F39C29")
    felhasznaloNev_label.place(x = 29,y = 14)


    img0 = PhotoImage(file=f"Jatsz_Kijelentkezes.png")
    Jatsz_Kijelentkezes_Button = Button(
        image=img0,
        borderwidth=0,
        highlightthickness=0,
        activebackground="#08082C",
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
        activebackground="#08082C",
        command= lambda: [selfDestroy(),kategoriak_kivalaszt(felhasznalonev)],
        relief="flat")

    Jatsz_Kezdes_Button.place(
        x=426, y=304,
        width=228,
        height=96)

    window.resizable(False, False)
    window.mainloop()

def kategoriak_kivalaszt(felhasznalonev):  #Robi

    pontszam = database.child("Felhasznalok").child(felhasznalonev).child("Pontszam").get().val()
    valaszt = arr.array('i', [0])
    alapSzin = "#201F93"
    kivalSzin = "#1F9393"
    def gombkivalaszt(gombszam):

        EgyesValaszt_Button.configure(background=alapSzin, activebackground=alapSzin),
        KettesValaszt_Button.configure(background=alapSzin, activebackground=alapSzin),
        HarmasValaszt_Button.configure(background=alapSzin, activebackground=alapSzin),
        NegyestValaszt_Button.configure(background=alapSzin, activebackground=alapSzin),

        if gombszam == 1:
            EgyesValaszt_Button.configure(background=kivalSzin, activebackground=kivalSzin),
            valaszt[0] = 1

        elif gombszam == 2:
            KettesValaszt_Button.configure(background=kivalSzin, activebackground=kivalSzin),
            valaszt[0] = 2


        elif gombszam == 3:
            HarmasValaszt_Button.configure(background=kivalSzin, activebackground=kivalSzin),
            valaszt[0] = 3
        elif gombszam == 4:
            NegyestValaszt_Button.configure(background=kivalSzin, activebackground=kivalSzin),
            valaszt[0] = 4

    def csinaljuk():
        if valaszt[0]==int(1):
            print("Egyes volt kivalasztva")
        elif valaszt[0]== int(2):
            print("Kettes volt kivalasztva")
        elif valaszt[0]==int(3):
            print("Harmas volt kivalasztva")
        elif valaszt[0]==int(4):
            print("Negyes volt kivalasztva")



    def doingEnable():
        if valaszt[0] == int(0):
            labelError = Label(text="Válassz egy kategóriát!", bg="#0B0B31",font =15 , fg="red")
            labelError.place(x=435, y=390)
            labelError.after(1500, lambda: [labelError.destroy()])
        else:
            csinaljuk()
            selfDestroy()
            kerdes(felhasznalonev)





    def selfDestroy():
        Kategoriak_Vissza_Button.destroy()
        Kategoriak_Szerkeszt_Button.destroy()
        Kategoriak_Inditas_Button.destroy()
        EgyesValaszt_Button.destroy()
        KettesValaszt_Button.destroy()
        HarmasValaszt_Button.destroy()
        NegyestValaszt_Button.destroy()


    background_img = PhotoImage(file=f"Kategoriak_Background.png")

    background = canvas.create_image(
            540.0, 303.5,
            image=background_img)

    img0 = PhotoImage(file=f"Kategoriak_Vissza.png")
    Kategoriak_Vissza_Button = Button(
            image=img0,
            borderwidth=0,
            highlightthickness=0,
            activebackground="#08082C",
            command=lambda: [selfDestroy(),jatsz(felhasznalonev)],
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
            activebackground="#08082C",
            command=lambda: [selfDestroy(),felhasznalo_kerdes_szerk(felhasznalonev)],
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
            activebackground="#08082C",
            command=lambda: [doingEnable()],

            relief="flat")

    Kategoriak_Inditas_Button.place(
            x=426, y=429,
            width=228,
            height=96)


    EgyesValaszt_Button = Button(

        text="Tudományos",
        font=("Josefin Sans",20),
        bg = "#201F93",
        fg = "white",
        activebackground="#201F93",
        activeforeground="white",
        borderwidth=0,
        highlightthickness=0,
        command=lambda :[gombkivalaszt(1)],
        relief="flat")

    EgyesValaszt_Button.place(
        x=34, y=213,
        width=480,
        height=56)


    HarmasValaszt_Button = Button(
        text="Sport",
        font=("Josefin Sans", 20),
        bg="#201F93",
        fg="white",
        activebackground="#201F93",
        activeforeground="white",
        borderwidth=0,
        highlightthickness=0,
        command=lambda :[gombkivalaszt(3)],
        relief="flat")

    HarmasValaszt_Button.place(
        x=566, y=213,
        width=480,
        height=56)


    KettesValaszt_Button = Button(
        text="Történelem",
        font=("Josefin Sans", 20),
        bg="#201F93",
        fg="white",
        activebackground="#201F93",
        activeforeground="white",
        borderwidth=0,
        highlightthickness=0,
        command=lambda :[gombkivalaszt(2)],
        relief="flat")

    KettesValaszt_Button.place(
        x=34, y=304,
        width=480,
        height=56)


    NegyestValaszt_Button = Button(
        text="Saját",
        font=("Josefin Sans", 20),
        bg="#201F93",
        fg="white",
        activeforeground="white",
        activebackground="#201F93",
        borderwidth=0,
        highlightthickness=0,
        command=lambda :[gombkivalaszt(4)],
        relief="flat")

    NegyestValaszt_Button.place(
        x=566, y=304,
        width=480,
        height=56)

    window.resizable(False, False)
    window.mainloop()

def felhasznalo_kerdes_szerk(felhasznalonev): #Robi



    valaszt = arr.array('i', [0])
    alapSzin = "#659CCE"
    kivalSzin = "#201F93"

    def save(felhasznalonev):
        felhasznaloID = database.child("Felhasznalok").child(felhasznalonev).child("Felhasznalo_ID").get().val()
        Kerdes = Kerdes_Entry.get()
        Valasz1 = Valasz_1_Entry.get()
        Valasz2 = Valasz_2_Entry.get()
        Valasz3 = Valasz_3_Entry.get()
        Valasz4 = Valasz_4_Entry.get()

        jovalasz = jovalaszfgv()

        Kerdesek = database.child("Kerdesek").get().val()
        Kerdesid = len(Kerdesek) + 1

        Kategoria = 4 ##sajat
        SajatKerdes = {"Felhasznalo_ID": felhasznaloID, "Kategoria_ID": Kategoria, "Kerdes": Kerdes,
                        "Kerdes_ID":Kerdesid}
        database.child("Kerdesek").child("Kerdes"+str(Kerdesid).set(SajatKerdes))

        Valaszok = database.child("Valaszok").get().val()
        Valaszid = len(Valaszok) + 1


        SajatValasz = {"Felhasznalo_ID": felhasznaloID, "Kategoria_ID": Kategoria, "Kerdes": Kerdes,
                        "Kerdes_ID":Kerdesid}





    def gombkivalaszt(gombszam):

        EgyesValaszt_Button.configure(background=alapSzin, activebackground=alapSzin),
        KettesValaszt_Button.configure(background=alapSzin, activebackground=alapSzin),
        HarmasValaszt_Button.configure(background=alapSzin, activebackground=alapSzin),
        NegyestValaszt_Button.configure(background=alapSzin, activebackground=alapSzin),

        if gombszam == 1:
            EgyesValaszt_Button.configure(background=kivalSzin, activebackground=kivalSzin),
            valaszt[0] = 1

        elif gombszam == 2:
            KettesValaszt_Button.configure(background=kivalSzin, activebackground=kivalSzin),
            valaszt[0] = 2


        elif gombszam == 3:
            HarmasValaszt_Button.configure(background=kivalSzin, activebackground=kivalSzin),
            valaszt[0] = 3
        elif gombszam == 4:
            NegyestVal3aszt_Button.configure(background=kivalSzin, activebackground=kivalSzin),
            valaszt[0] = 4

        Felhasznalo_Kerdes_Szerkesztes_Mentes_Button.configure(state=NORMAL)


    def jovalaszfgv():
        if valaszt[0]==int(1):
            return Valasz_1_Entry.get()
        elif valaszt[0]== int(2):
            return Valasz_2_Entry.get()
        elif valaszt[0]==int(3):
            return Valasz_3_Entry.get()
        elif valaszt[0]==int(4):
            return Valasz_4_Entry.get(),


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
        EgyesValaszt_Button.destroy()
        KettesValaszt_Button.destroy()
        HarmasValaszt_Button.destroy()
        NegyestValaszt_Button.destroy()



    background_img = PhotoImage(file=f"Felhasznalo_Kerdes_Szerkesztes_Background.png")
    background = canvas.create_image(
        540.0, 303.5,
        image=background_img)

    img0 = PhotoImage(file=f"Felhasznalo_Kerdes_Szerkesztes_Mentes.png")
    Felhasznalo_Kerdes_Szerkesztes_Mentes_Button = Button(
        image=img0,
        borderwidth=0,
        highlightthickness=0,
        activebackground="#201F93",
        command=lambda: [save(felhasznalonev),selfDestroy(),kategoriak_kivalaszt(felhasznalonev)],
        relief="flat",
        state=DISABLED)

    Felhasznalo_Kerdes_Szerkesztes_Mentes_Button .place(
        x=426, y=497,
        width=228,
        height=96)

    img1 = PhotoImage(file=f"Felhasznalo_Kerdes_Szerkesztes_Vissza.png")
    Felhasznalo_Kerdes_Szerkesztes_Vissza_Button = Button(
        image=img1,
        borderwidth=0,
        activebackground="#201F93",
        highlightthickness=0,
        command=lambda: [selfDestroy(),kategoriak_kivalaszt(felhasznalonev)],
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
    EgyesValaszt_Button = Button(
        text="1.",
        font=("Josefin Sans", 20, "bold"),
        bg=alapSzin,
        fg="black",
        activebackground=alapSzin,
        activeforeground="black",
        borderwidth=0,
        highlightthickness=0,
        command=lambda: [gombkivalaszt(1)],
        relief="flat"
    )

    EgyesValaszt_Button.place(
        x=55, y=520,
        width=54,
        height=54)

    img3 = PhotoImage(file=f"2.png")
    KettesValaszt_Button = Button(
        text="2.",
        font=("Josefin Sans", 20, "bold"),
        bg=alapSzin,
        fg="black",
        activebackground=alapSzin,
        activeforeground="black",
        borderwidth=0,
        highlightthickness=0,
        command=lambda: [gombkivalaszt(2)],
        relief="flat")

    KettesValaszt_Button.place(
        x=119, y=520,
        width=54,
        height=54)

    img4 = PhotoImage(file=f"3.png")
    HarmasValaszt_Button = Button(
        text="3.",
        font=("Josefin Sans", 20, "bold"),
        bg=alapSzin,
        fg="black",
        activebackground=alapSzin,
        activeforeground="black",
        borderwidth=0,
        highlightthickness=0,
        command=lambda: [gombkivalaszt(3)],
        relief="flat")

    HarmasValaszt_Button.place(
        x=183, y=520,
        width=54,
        height=54)

    img5 = PhotoImage(file=f"4.png")
    NegyestValaszt_Button = Button(
        text="4.",
        font=("Josefin Sans", 20, "bold"),
        bg=alapSzin,
        fg="black",
        activebackground=alapSzin,
        activeforeground="black",
        borderwidth=0,
        highlightthickness=0,
        command=lambda: [gombkivalaszt(4)],
        relief="flat")

    NegyestValaszt_Button.place(
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