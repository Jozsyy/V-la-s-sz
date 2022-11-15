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
felhasznalo1 = {"Felhasznalo_ID": "00000","Vezeteknev": "Miklo", "Keresztnev": "Jozsef-Peter", "Jelszo":"valassz123",
       "Email":"miklo.jozsef@yahoo.com", "Pontszam":"0"}
database.child("Felhasznalok").child("Admin1").set(felhasznalo1)

#Kategoriak tabla
kategoria1 = {"Kategoria_ID": "1", "Nev":"Tudomanyos"}
kategoria2 = {"Kategoria_ID": "2", "Nev":"Sport"}
database.child("Kategoriak").child("Kategoria1").set(kategoria1)
database.child("Kategoriak").child("Kategoria2").set(kategoria2)

#Kerdesek tabla
kerdes1 = {"Kerdes_ID": "00000000", "Kerdes":"Mennyi a PI értéke?","Kategoria_ID":"Tudomanyos", "Felhasznalo_ID":"00000"}
database.child("Kerdesek").child("Kerdes1").set(kerdes1)

#Valaszok tabla
valasz1= {"Valasz_id":"00000000","Kerdes_ID": "00000000","Jo_Valasz":"3.14159", "Rossz_Valasz1":"3.13153",
           "Rossz_Valasz2":"3.15141","Rossz_Valasz3":"2.71828"}
database.child("Valaszok").child("Valasz1").set(valasz1)