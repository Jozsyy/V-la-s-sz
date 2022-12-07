import pyrebase

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

#Felhasznalok tabla
felhasznalo1 = {"Felhasznalo_ID": "1","Vezeteknev": "Miklo", "Keresztnev": "Jozsef-Peter", "Jelszo":"valassz123",
       "Email":"miklo.jozsef@yahoo.com", "Pontszam":"0"}
database.child("Felhasznalok").child("Admin1").set(felhasznalo1)

felhasznalo2 = {"Felhasznalo_ID": "2","Vezeteknev": "Sarkany", "Keresztnev": "Illes", "Jelszo":"valassz1234",
       "Email":"sarkany.illes@student.ms.sapientia.ro", "Pontszam":"0"}
database.child("Felhasznalok").child("Admin2").set(felhasznalo2)

felhasznalo3 = {"Felhasznalo_ID": "3","Vezeteknev": "Bartha", "Keresztnev": "Robert", "Jelszo":"valassz12345",
       "Email":"bartha.robert1@gmail.com", "Pontszam":"0"}
database.child("Felhasznalok").child("Admin3").set(felhasznalo3)


#Kategoriak tabla
kategoria1 = {"Kategoria_ID": "1", "Nev":"Tudomanyos"}
kategoria2 = {"Kategoria_ID": "2", "Nev":"Sport"}
kategoria3 = {"Kategoria_ID": "3", "Nev":"Altalanos"}
kategoria4 = {"Kategoria_ID": "4", "Nev":"Sajat"}

database.child("Kategoriak").child("Kategoria1").set(kategoria1)
database.child("Kategoriak").child("Kategoria2").set(kategoria2)
database.child("Kategoriak").child("Kategoria3").set(kategoria3)
database.child("Kategoriak").child("Kategoria4").set(kategoria4)

#Kerdesek tabla
kerdes1 = {"Kerdes_ID": "00000000", "Kerdes":"Mennyi a PI értéke?","Kategoria_ID":"Tudomanyos", "Felhasznalo_ID":"00001"}
database.child("Kerdesek").child("Kerdes1").set(kerdes1)

kerdes2 = {"Kerdes_ID": "00000002", "Kerdes":"Hany kontinens kezdodik 'A'-betuvel?","Kategoria_ID":"Tudomanyos", "Felhasznalo_ID":"00003"}
database.child("Kerdesek").child("Kerdes2").set(kerdes2)

kerdes3 = {"Kerdes_ID": "00000003", "Kerdes":"Hol elnek a pingvinek?","Kategoria_ID":"Altalanos", "Felhasznalo_ID":"00003"}
database.child("Kerdesek").child("Kerdes3").set(kerdes3)

#SPORT
kerdes4 = {"Kerdes_ID": "00000004", "Kerdes":"Melyik orszag nyerte a 2018-as VB-t?","Kategoria_ID":"Altalanos", "Felhasznalo_ID":"00003"}
database.child("Kerdesek").child("Kerdes4").set(kerdes4)

#TUDOMANYOS
kerdes5 = {"Kerdes_ID": "00000005", "Kerdes":"Mikor halt meg Albert Einstein?","Kategoria_ID":"Tudomanyos", "Felhasznalo_ID":"00003"}
database.child("Kerdesek").child("Kerdes5").set(kerdes5)

#ALTALANOS
kerdes6 = {"Kerdes_ID": "00000006", "Kerdes":"Minek a rövidítése a CD?","Kategoria_ID":"Tudomanyos", "Felhasznalo_ID":"00003"}
database.child("Kerdesek").child("Kerdes6").set(kerdes6)





#Valaszok tabla
valasz1= {"Valasz_id":"00000001","Kerdes_ID": "00000001","Jo_Valasz":"3.14159", "Rossz_Valasz1":"3.13153",
           "Rossz_Valasz2":"3.15141","Rossz_Valasz3":"2.71828"}
database.child("Valaszok").child("Valasz1").set(valasz1)

valasz2= {"Valasz_id":"00000002","Kerdes_ID": "00000002","Jo_Valasz":"3", "Rossz_Valasz1":"4",
           "Rossz_Valasz2":"5","Rossz_Valasz3":"2"}
database.child("Valaszok").child("Valasz2").set(valasz2)

valasz3= {"Valasz_id":"00000003","Kerdes_ID": "00000003","Jo_Valasz":"deli sarkon", "Rossz_Valasz1":"eszaki sarkon",
           "Rossz_Valasz2":"Afrikaban","Rossz_Valasz3":"itt"}
database.child("Valaszok").child("Valasz3").set(valasz3)

valasz4= {"Valasz_id":"00000004","Kerdes_ID": "00000004","Jo_Valasz":"Franciaorszag", "Rossz_Valasz1":"Nemetorszag",
           "Rossz_Valasz2":"Argentina","Rossz_Valasz3":"Spanyolorszag"}
database.child("Valaszok").child("Valasz4").set(valasz4)

valasz5= {"Valasz_id":"00000005","Kerdes_ID": "00000005","Jo_Valasz":"1955", "Rossz_Valasz1":"1975",
           "Rossz_Valasz2":"1969","Rossz_Valasz3":"1900"}
database.child("Valaszok").child("Valasz5").set(valasz5)

valasz6= {"Valasz_id":"00000006","Kerdes_ID": "00000006","Jo_Valasz":"Compact Disc", "Rossz_Valasz1":"Merevlemez",
           "Rossz_Valasz2":"Compact Disco","Rossz_Valasz3":"Counter Day"}
database.child("Valaszok").child("Valasz6").set(valasz6)


print(database.child("Felhasznalok").child("Admin5").get().val())