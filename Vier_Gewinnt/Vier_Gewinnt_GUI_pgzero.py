import pgzrun
from Vier_Gewinnt_Klasse import viergewinntklasse
import time

Vier_Gewinnt = viergewinntklasse()
HEIGHT = 600
WIDTH = 600


xposition = 30
yposition = 30
Spielerliste = []
LabelListe = []
Array = [["w" for x in range(7)] for y in range(6)]
# Leeres Spielfeld generieren
for x in range(7):
    yposition = -30
    xposition = xposition +5
    for y in range(6):
        yposition = yposition +65
        Spieler = Actor("spieler_weiß")
        Spieler.x = xposition
        Spieler.y = yposition
        Spielerliste.append(Spieler)
    xposition = xposition + 60

def draw():
    global Vier_Gewinnt
    global LabelListe

    # Hintergrund
    screen.fill("green")
    # Spielsteine zeichnen (Grün, Gelb, Weiß)
    for Spieler in Spielerliste:
        Spieler.draw()
    # Label zeichen
    for Label in LabelListe:
        screen.draw.text(Label.gettext(), (Label.getxposition(), Label.getypsition()), color="white")

    # Überprüfung ob das Spiel stattgefunden hat
    if Vier_Gewinnt.getSpielbeendet() == True:
        time.sleep(5)
        Vier_Gewinnt = viergewinntklasse()
        __Spielfeldgenerieren()
        for label in LabelListe:
            if str(label.gettext()) == "Spieler Gelb hat gewonnen.":
                LabelListe.remove(label)



# Methode fügt Daten (Text,xPosition,yPosition) für ein Label als Array in ein Array
def labelsetzen(text,xposition,yposition):
    Label = labelklasse(text,xposition,yposition)
    LabelListe.append(Label)





def on_mouse_down(pos):
    global Vier_Gewinnt

    # Spalte des Zuges ermitteln
    xmouse = pos[0]
    spalte = 100
    if xmouse >= 2.5 and xmouse <= 67.4:
        spalte = 0
    elif xmouse >= 67.5 and xmouse <= 132.4:
        spalte = 1
    elif xmouse >= 132.5 and xmouse <= 197.4:
        spalte = 2
    elif xmouse >= 197.5 and xmouse <= 262.4:
        spalte = 3
    elif xmouse >= 152.5 and xmouse <= 327.4:
        spalte = 4
    elif xmouse >= 217.5 and xmouse <= 392.4:
        spalte = 5
    elif xmouse >= 272.5 and xmouse <= 457.4:
        spalte = 6
    if spalte != 100:
        Vier_Gewinnt.setSpielzug(spalte)
        Vier_Gewinnt.ausführen()
        # Spielfeld erstellen
        __Spielfeldgenerieren()
    # Label setzen wenn einer gewonnen hat
    if Vier_Gewinnt.getErgebnis() == "ge":
        labelsetzen("Spieler Gelb hat gewonnen.",10,500)
    elif Vier_Gewinnt.getErgebnis() == "gr":
        labelsetzen("Spieler Grün hat gewonnen.",10,500)
    elif Vier_Gewinnt.getErgebnis() == "un":
        labelsetzen("Unentschieden",10,500)
    draw()

def __Spielfeldgenerieren():
    global Array
    Array = Vier_Gewinnt.getArray()
    xposition = 30
    yposition = 30
    for x in range(7):
        yposition = -30
        xposition = xposition +5
        for y in range(6):
            yposition = yposition +65
            if Array[y][x] == "w":
                Spieler = Actor("spieler_weiß")
            elif Array[y][x] == "ge":
                Spieler = Actor("spieler_gelb")
            elif Array[y][x] == "gr":
                Spieler = Actor("spieler_gruen")
            Spieler.x = xposition
            Spieler.y = yposition
            Spielerliste.append(Spieler)
        xposition = xposition + 60

    
class labelklasse:
    def __init__(self,text,xposition,yposition):
        self.__text = text
        self.__xposition = xposition
        self.__yposition = yposition

    def gettext(self):
        return self.__text

    def getxposition(self):
        return self.__xposition

    def getypsition(self):
        return self.__yposition





pgzrun.go()
