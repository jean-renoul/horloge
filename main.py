import datetime
import time
  
heure = (10, 25, 13)
alarme = (10, 25, 15)
pause = (10, 25, 17)
liste_alarme = list(alarme)
liste_heure = list(heure)
liste_pause = list(pause)
alarme_datetime = datetime.datetime.now().replace(hour=liste_alarme[0], minute=liste_alarme[1], second=liste_alarme[2])
pause_datetime = datetime.datetime.now().replace(hour=liste_pause[0], minute=liste_pause[1], second=liste_pause[2])

def fonction_pause(x):
    while x == pause_datetime:
            a = input ("Ecrivez 'unpause' pour mettre fin à la pause : ")
            if a == "unpause":
                break
            else:
                while True:
                    (time.sleep(1))

def reveil(x):
    if x == alarme_datetime:
        print("ALERTE ALERTE ALERTE")

def AM_PM(heure_modifiee, x):
    if x:
        heure_modifiee_syntaxe = heure_modifiee.strftime("%I:%M:%S:%p")
    else:
        heure_modifiee_syntaxe = heure_modifiee.strftime("%H:%M:%S")
    return heure_modifiee_syntaxe

def afficher_heure(x):
    heure_modifiee = datetime.datetime.now().replace(hour=liste_heure[0], minute=liste_heure[1], second=liste_heure[2])
    
    while True:
        heure_modifiee_syntaxe = AM_PM(heure_modifiee, False)
        print(heure_modifiee_syntaxe)
        time.sleep(1)
        
        heure_modifiee = heure_modifiee.replace(second=heure_modifiee.second + 1)
        reveil(heure_modifiee)
        fonction_pause(heure_modifiee)

afficher_heure(heure)