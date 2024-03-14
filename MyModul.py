import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import random
import string


def registreeriKasutaja(kasutajanimi, parool, kasutajad, paroolid):
    """Funktsioon uue kasutaja registreerimiseks."""
    kasutajad.append(kasutajanimi)
    paroolid.append(parool)
    print("Kasutaja on edukalt registreeritud.")

def LoePasJaLog(fail:str)->any:
    """Andmete lugemine failist ja sõnastiku loomine."""
    logPas = {}  
    with open(fail, "r", encoding="utf-8") as f:
        for line in f:
            l, p = line.strip().split(":")
            logPas[l] = p
    return logPas

def salasona(pikkus: int):
    """Funktsioon genereerib juhusliku parooli."""
    return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(pikkus))

def muudaParool(kasutajanimi, vanaParool, uusParool, kasutajad, paroolid):
    """Funktsioon kasutaja parooli muutmiseks."""
    if kasutajanimi in kasutajad:
        index = kasutajad.index(kasutajanimi)
        if paroolid[index] == vanaParool:
            paroolid[index] = uusParool
            print("Parool on edukalt muudetud.")
        else:
            print("Vale vana parool.")
    else:
        print("Kasutajanime ei eksisteeri.")

def kirjutaFailisse(fail:str, jarjend):
    """Faili kirjutamine antud järjendi sisuga."""
    with open(fail, "w", encoding="utf-8") as f:
        for el in jarjend:
            f.write(el + "\n")       

def sisselogimine(kasutajanimi, parool, logPas, kasutajad, paroolid):
    """Funktsioon kontrollib kasutajanime ja parooli sisselogimisel."""
    if not kasutajanimi or not parool:
        print("Palun sisestage nii kasutajanimi kui ka parool.")
        return

    if kasutajanimi in logPas:
        if parool == logPas[kasutajanimi]:
            print("Sisselogimine õnnestus.")
        else:
            print("Vale parool.")
    else:
        print("Kasutajanime ei eksisteeri.")

def unustatudParool(kasutajanimi, uusParool, logPas, receiver_email):
    """Funktsioon saadab kasutajale e-kirja uue parooliga."""
    if kasutajanimi in logPas:
        logPas[kasutajanimi] = uusParool
        

        # Muutujad kirja saatmiseks
        smtp_server = "smtp.gmail.com"
        port = 587
        sender_email = "martinsild.mr@gmail.com"
        password = ""
        subject = "Martin SIld"
        message = "Martin Sild"
        receiver_email = ""

        # Kirja loomine
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = receiver_email  
        msg['Subject'] = "Uus parool"

        # Kirja sisu
        message = f"Teie uus parool: {uusParool}"
        msg.attach(MIMEText(message, 'plain'))

        # Kirja saatmine
        try:
            server = smtplib.SMTP(smtp_server, port)
            server.starttls()
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, msg.as_string())
            print("Kirja saatmine õnnestus.")
        except Exception as e:
            print("Viga kirja saatmisel:", str(e))
        finally:
            server.quit()

        print("Parool on edukalt muudetud. Uus parool on saadetud märgitud e-posti aadressile.")
    else:
        print("Kasutajat määratud nimega ei leitud.")
