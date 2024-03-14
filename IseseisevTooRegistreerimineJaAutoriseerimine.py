from MyModul import *

kasutajad = []
paroolid = []

logPas = LoePasJaLog("autoriseerimine.txt")

while True:
    print("\n0 - Registreerimine\n1 - Sisselogimine\n2 - Kasutajanime või parooli muutmine\n3 - Parooli taastamine\n4 - Väljumine")
    valik = input("Sisestage valiku number: ")
    
    if valik == "4":
        # Salvestame autentimisandmed enne väljumist
        kirjutaFailisse("autoriseerimine.txt", [f"{kasutajad[i]}:{paroolid[i]}" for i in range(len(kasutajad))])
        break

    kasutajanimi = input("Sisestage kasutajanimi: ")

    if valik == "0":
        valik_parool = input("Kas soovite sisestada oma parooli (s) või genereerida süsteemi poolt (g)? ")
        if valik_parool.lower() == "s":
            parool = input("Sisestage parool: ")
        elif valik_parool.lower() == "g":
            parool = salasona(5)
            print("Genereeritud parool:", parool)
        registreeriKasutaja(kasutajanimi, parool, kasutajad, paroolid)
        kirjutaFailisse("autoriseerimine.txt", [f"{kasutajad[i]}:{paroolid[i]}" for i in range(len(kasutajad))])


    elif valik == "1":
        parool = input("Sisestage oma parool: ")
        sisselogimine(kasutajanimi, parool, logPas, kasutajad, paroolid)

    elif valik == "2":
        vanaParool = input("Sisestage vana parool: ")
        uusParool = input("Sisestage uus parool: ")
        muudaParool(kasutajanimi, vanaParool, uusParool, kasutajad, paroolid)  

    elif valik == "3":
        uusParool = input("Sisestage uus parool: ")
        receiver_email = input("Sisestage saaja e-posti aadress: ")
        unustatudParool(kasutajanimi, uusParool, logPas, receiver_email)
