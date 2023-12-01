import datetime
import time

# Définit les heures initiales pour l'alarme, la pause et l'heure actuelle
heure = (10, 25, 13)
alarme = (10, 25, 15)
pause = (10, 25, 17)
liste_alarme = list(alarme)
liste_heure = list(heure)
liste_pause = list(pause)

# Crée des datetimes pour les heures d'alarme et de pause
alarme_datetime = datetime.datetime.now().replace(hour=liste_alarme[0], minute=liste_alarme[1], second=liste_alarme[2])
pause_datetime = datetime.datetime.now().replace(hour=liste_pause[0], minute=liste_pause[1], second=liste_pause[2])

# Fonction pour gérer la pause
def fonction_pause(x):
    while x == pause_datetime:
        a = input("Écrivez 'unpause' pour mettre fin à la pause : ")
        if a == "unpause":
            break
        else:
            while True:
                (time.sleep(1))

# Fonction pour gérer l'alarme
def reveil(x):
    if x == alarme_datetime:
        print("ALERTE ALERTE ALERTE")

# Fonction pour formater l'heure au format AM/PM ou 24 heures
def AM_PM(heure_modifiee, x):
    if x:
        heure_modifiee_syntaxe = heure_modifiee.strftime("%I:%M:%S:%p")
    else:
        heure_modifiee_syntaxe = heure_modifiee.strftime("%H:%M:%S")
    return heure_modifiee_syntaxe

# Fonction pour afficher l'heure actuelle, gérer les alarmes et la pause
def afficher_heure(x):
    heure_modifiee = datetime.datetime.now().replace(hour=liste_heure[0], minute=liste_heure[1], second=liste_heure[2])

    while True:
        # Formate et affiche l'heure actuelle
        heure_modifiee_syntaxe = AM_PM(heure_modifiee, True)
        print(heure_modifiee_syntaxe)
        time.sleep(1)

        # Met à jour l'heure en ajoutant une seconde
        heure_modifiee = heure_modifiee.replace(second=heure_modifiee.second + 1)

        # Appelle les fonctions d'alarme et de pause
        reveil(heure_modifiee)
        fonction_pause(heure_modifiee)

# Commence à afficher l'heure avec l'heure initiale définie
afficher_heure(heure)