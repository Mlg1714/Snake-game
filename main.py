import random
import pygame
import os
import sys
from Slider import Slider

import Buttons

pygame.init()
pygame.mixer.init()

screen_info = pygame.display.Info()
bildschirm = pygame.display.set_mode((screen_info.current_w, screen_info.current_h), pygame.FULLSCREEN)
Game = pygame.Surface((screen_info.current_w, screen_info.current_h))
Game_Over = pygame.Surface((screen_info.current_w, screen_info.current_h))
Settings = pygame.Surface((screen_info.current_w, screen_info.current_h))
pygame.display.set_caption("Snakegame")

# Icons finden
ordner = getattr(sys, "_MEIPASS", os.path.dirname(os.path.abspath(__file__)))
Bilder_ordner = os.path.join(ordner, "Bilder_ordner")
Sounds_ordner = os.path.join(ordner, "Sounds")
Musik_ordner = os.path.join(ordner, "Musik")


# Bilder laden
beenden_button_pic = pygame.image.load(os.path.join(Bilder_ordner, "beenden.png")).convert_alpha()
einstellungen_button_pic = pygame.image.load(os.path.join(Bilder_ordner, "einstellungen.png")).convert_alpha()
start_button_pic = pygame.image.load(os.path.join(Bilder_ordner, "start.png")).convert_alpha()
zurück = pygame.image.load(os.path.join(Bilder_ordner, "zurueck.png")).convert_alpha()
neues_spiel = pygame.image.load(os.path.join(Bilder_ordner, "neues_spiel.png")).convert_alpha()
Speaker_pic = pygame.image.load(os.path.join(Bilder_ordner, "speaker.png")).convert_alpha()
Mute_pic = pygame.image.load(os.path.join(Bilder_ordner, "mute.png")).convert_alpha()
Ein_pic = pygame.image.load(os.path.join(Bilder_ordner, "einfach.png")).convert_alpha()
Fort_Pic = pygame.image.load(os.path.join(Bilder_ordner, "fortgeschritten.png")).convert_alpha()
Schw_Pic = pygame.image.load(os.path.join(Bilder_ordner, "schwer.png")).convert_alpha()
Wei_pic = pygame.image.load(os.path.join(Bilder_ordner, "weiter.png")).convert_alpha()

# Sounds
essen = pygame.mixer.Sound(os.path.join(Sounds_ordner, "essen.wav"))
gameover = pygame.mixer.Sound(os.path.join(Sounds_ordner, "gameover.wav"))
start = pygame.mixer.Sound(os.path.join(Sounds_ordner, "start.wav"))

mitte_x = screen_info.current_w // 2
mitte_y = screen_info.current_h // 2

# Musik randomizer
musik_datei = os.listdir(Musik_ordner)
Musik_ende = pygame.USEREVENT + 1
pygame.mixer.music.set_endevent(Musik_ende)

letzter_song = None
def next_song():
    global letzter_song
    auswahl = [song for song in musik_datei if song != letzter_song]
    neuer_song = random.choice(auswahl)
    letzter_song = neuer_song
    pygame.mixer.music.load(os.path.join(Musik_ordner, neuer_song))
    pygame.mixer.music.play()
next_song()

# Lautstärke
essen.set_volume(0.45)
gameover.set_volume(0.75)
start.set_volume(0.75)
pygame.mixer.music.set_volume(0.1125)
Mute_Status = False

def sound_abspielen(sound):
    if not Mute_Status:
        sound.play()
lautstärke_slider = Slider(
    x= mitte_x - 650,           
    y= 185,           
    breite= 1300,      
    hoehe= 30,        
    min_wert= 0,
    max_wert= 100,
    startwert= 100     
)

# Mitte des Bildschirms berechnen
button_width = start_button_pic.get_width() * 1.5
button_height = start_button_pic.get_height() * 1.5
button_x = screen_info.current_w // 2 - button_width // 2
button_y = screen_info.current_h // 2 - button_height // 2

# Buttons erstellen
start_button = Buttons.Button(button_x, 300, start_button_pic, 1.5)
einstellungen_button = Buttons.Button(button_x, 500 ,einstellungen_button_pic, 1.5)
beenden_button = Buttons.Button(button_x, 700,beenden_button_pic, 1.5)
neues_spiel_button = Buttons.Button(640 - button_width // 2, 660, neues_spiel, 1.5)
zurück_button = Buttons.Button(1280 - button_width // 2, 660, zurück, 1.5)
speaker_button = Buttons.Button(1500, 70, Speaker_pic, 0.125)
mute_button = Buttons.Button(1500, 70, Mute_pic, 0.125)
Einfach_button = Buttons.Button(button_x, 300, Ein_pic, 1.5)
Fortgeschritten_button = Buttons.Button(button_x, 500, Fort_Pic, 1.5)
Schwer_button = Buttons.Button(button_x, 700, Schw_Pic, 1.5)
Weiter_button = Buttons.Button(640 - button_width // 2, 660, Wei_pic, 1.5)
zurück_button_settings = Buttons.Button(button_x, 900, zurück, 1.5)

# Farbe
blau = (30, 30, 150) #Blau
rot =  (255, 0, 0, 255) # Rot
hell = (120, 168, 60) #Helleresgrün
dunkel = (112, 156, 54) # Dunkelgrün
weiß = (255, 255, 255)  # Weiß
Schwarz = (0, 0, 0, 255)

kleiner_font = pygame.font.SysFont("arialblack", 30)
font = pygame.font.SysFont("arialblack", 80)  # Schriftart und Größe
def draw_text(text, font, farbe, x, y):
    text_surface = font.render(text, True, farbe)  
    bildschirm.blit(text_surface, (x, y))

mitte_x = screen_info.current_w // 2
mitte_y = screen_info.current_h // 2

text_surface_Mu = font.render("Music", 60, (weiß))
text_rect_Mu = text_surface_Mu.get_rect(center=(mitte_x, 130))

text_surface_Pa = font.render("Pause", True, (weiß))
text_rect_Pa = text_surface_Pa.get_rect(center=(mitte_x, 100))

text_surface_ST = font.render("Snakegame", True, (weiß))
text_rect_ST = text_surface_ST.get_rect(center=(mitte_x, 100))

text_surface_GM = font.render("Game Modes", True, (weiß))
text_rect_GM = text_surface_GM.get_rect(center=(mitte_x, 100))

# Gameover text
text_surface_GO = font.render("Game Over", True, (rot))
text_rect_GO = text_surface_GO.get_rect(center=(mitte_x, 90))

# Spielzustände
main_menu = "main"
Pause = True
Spiel = True

# Spielfeld
zellgroesse = 40
spielfeld_breite = 800
spielfeld_hoehe = 800
feld_x = (screen_info.current_w - spielfeld_breite) // 2
feld_y = (screen_info.current_h - spielfeld_hoehe) // 2

mitte_spalte = (spielfeld_breite // zellgroesse) // 2
mitte_zeile = (spielfeld_hoehe // zellgroesse) // 2

# Movement
Richtung = "Stop"
letzte_bewegungsrichtung = "Rechts"
bewegungs_zaehler = 0
bewegungs_verzoegern = 7
kopf_x = feld_x + mitte_spalte * zellgroesse
kopf_y = feld_y + mitte_zeile * zellgroesse

# Start pos der Schlange
start_x = feld_x + mitte_spalte * zellgroesse
start_y = feld_y + mitte_zeile * zellgroesse

# Alle 3 segmente
schlange = [
    (start_x, start_y),
    (start_x - zellgroesse, start_y),
    (start_x - zellgroesse * 2, start_y)]
soll_wachsen = False

# Fruchtrandomizer
def neue_frucht_position():
    while True:
        spalte = random.randint(0, (spielfeld_breite // zellgroesse) - 1)
        zeile = random.randint(0, (spielfeld_hoehe // zellgroesse) - 1)
        pos_x = feld_x + spalte * zellgroesse
        pos_y = feld_y + zeile * zellgroesse
        if (pos_x, pos_y) not in schlange:
            return pos_x, pos_y
frucht_x, frucht_y = neue_frucht_position()

highscore = 0
frucht_score = 0

# Hauptschleife
while Spiel:

    events = pygame.event.get()
    # Hintergrundfarbe Main Menü
    bildschirm.fill((Schwarz))

    # Menüs
    if main_menu == "main": 
        bildschirm.blit(text_surface_ST, text_rect_ST)
        if start_button.draw(bildschirm, events):
            sound_abspielen(start)
            main_menu = "Game_Modes"
            frucht_x, frucht_y = neue_frucht_position()
            schlange = [
                (start_x, start_y),
                (start_x - zellgroesse, start_y),
                (start_x - zellgroesse * 2, start_y)]
            frucht_score = 0
            Richtung = "Stop"
            letzte_bewegungsrichtung = Richtung
        if einstellungen_button.draw(bildschirm, events):
            main_menu = "settings"
        if beenden_button.draw(bildschirm, events):
            Spiel = False

    elif main_menu == "settings":
        pygame.draw.line(bildschirm, weiß, (mitte_x - 650, 200), (mitte_x + 650, 200), 10)
        pygame.draw.circle(bildschirm, weiß, (int(lautstärke_slider.griff_x), 200), 15)
        bildschirm.blit(text_surface_Mu, text_rect_Mu)
        draw_text(f"{lautstärke_slider.get_value()}%", kleiner_font, weiß, mitte_x + 680, 185)
        if zurück_button_settings.draw(bildschirm, events):
            main_menu = "main"
 
    elif main_menu == "Game_Modes":
        bildschirm.blit(text_surface_GM, text_rect_GM)
        if Einfach_button.draw(bildschirm, events):
            bewegungs_verzoegern = 8
            main_menu = "game"
        if Fortgeschritten_button.draw(bildschirm, events):
            bewegungs_verzoegern = 6
            main_menu = "game"
        if Schwer_button.draw(bildschirm, events):
            bewegungs_verzoegern = 4
            main_menu = "game"

    elif main_menu == "Pause":
        bildschirm.blit(text_surface_Pa, text_rect_Pa)
        Richtung = "Stop"
        if zurück_button.draw(bildschirm, events):
            main_menu = "main"
        if Weiter_button.draw(bildschirm, events):
            main_menu = "game"
        
    elif main_menu == "Game_Over":
        if frucht_score > highscore:
            highscore = frucht_score
        draw_text(str(highscore), font, weiß, mitte_x, 500)
        bildschirm.blit(text_surface_GO, text_rect_GO)
        if neues_spiel_button.draw(bildschirm, events):
            sound_abspielen(start)
            main_menu = "game"
            frucht_x, frucht_y = neue_frucht_position()
            schlange = [
                (start_x, start_y),
                (start_x - zellgroesse, start_y),
                (start_x - zellgroesse * 2, start_y)]
            frucht_score = 0
            Richtung = "Stop"
            letzte_bewegungsrichtung = Richtung
        if zurück_button.draw(bildschirm, events):
            main_menu = "main"

    elif main_menu == "game":
        
        # Hintergrundfarbe Game
        Game.fill(blau)

        # Mute Button
        if Mute_Status == False:
            if speaker_button.draw(Game, events):
                Mute_Status = True
                pygame.mixer.music.pause()
        elif Mute_Status == True:
            if mute_button.draw(Game, events):
                Mute_Status = False
                pygame.mixer.music.unpause()
        bildschirm.blit(Game, (0, 0))

        # Spiefeld
        for spalte in range(spielfeld_breite // zellgroesse):
            for zeile in range(spielfeld_hoehe // zellgroesse):
                pos_x = feld_x + spalte * zellgroesse
                pos_y = feld_y + zeile * zellgroesse
        
                if (spalte + zeile) % 2 == 0:
                    farbe = hell
                else:
                    farbe = dunkel

                pygame.draw.rect(Game, farbe, (pos_x, pos_y, zellgroesse, zellgroesse))

        # Player
        for segment in schlange:
            pygame.draw.rect(Game, (255, 255, 255), (int(segment[0]), int(segment[1]), 40, 40))

        # Fruchtrandomizer
        pygame.draw.circle(Game, (255, 0, 0), (int(frucht_x + zellgroesse // 2), int(frucht_y + zellgroesse // 2)), 20)
        if pygame.Rect(schlange[0][0], schlange[0][1], 40, 40).colliderect(pygame.Rect(frucht_x, frucht_y, 40, 40)):
            sound_abspielen(essen)
            frucht_x, frucht_y = neue_frucht_position()
            frucht_score = frucht_score + 1
            soll_wachsen = True

        # Geschwindigkeit der Schlange
        bewegungs_zaehler += 1
        if bewegungs_zaehler >= bewegungs_verzoegern:
            bewegungs_zaehler = 0

            # Bewegung der Schlange
            kopf_x, kopf_y = schlange[0]

            if Richtung == "Rechts":
                neuer_kopf = (kopf_x + zellgroesse, kopf_y)
            elif Richtung == "Links":
                neuer_kopf = (kopf_x - zellgroesse, kopf_y)
            elif Richtung == "Oben":
                neuer_kopf = (kopf_x, kopf_y - zellgroesse)
            elif Richtung == "Unten":
                neuer_kopf = (kopf_x, kopf_y + zellgroesse)
            else:
                neuer_kopf = (kopf_x, kopf_y)

            # Wachsen der Schlange
            if Richtung != "Stop":
                schlange.insert(0, neuer_kopf)
                if soll_wachsen:
                    soll_wachsen = False
                else:
                    schlange.pop()

                letzte_bewegungsrichtung = Richtung

            # Collition mit dem Body
            if Richtung != "Stop":
                if schlange[0] in schlange[1:]:
                    main_menu = "Game_Over"
                    sound_abspielen(gameover)
                    schlange = [
                    (start_x, start_y),
                    (start_x - zellgroesse, start_y),
                    (start_x - zellgroesse * 2, start_y)]
                    Richtung = "Stop"

        bildschirm.blit(Game, (0, 0))

        # Bildschirmgrenzen überprüfen
        kopf_x, kopf_y = schlange[0]
        if kopf_x < feld_x or kopf_x > feld_x + spielfeld_breite - 40 or kopf_y < feld_y or kopf_y > feld_y + spielfeld_hoehe - 40:
            main_menu = "Game_Over"
            sound_abspielen(gameover)
            schlange = [
            (start_x, start_y),
            (start_x - zellgroesse, start_y),
            (start_x - zellgroesse * 2, start_y)]
            Richtung = "Stop"

        draw_text(str(frucht_score),font ,weiß,930, 40)

    # Events abfragen (z.B. Fenster schließen)  
    for event in events:
        if main_menu == "settings":
            lautstärke_slider.handle_event(event)
            if lautstärke_slider.griff_x < mitte_x - 650:
                lautstärke_slider.griff_x = mitte_x - 650
            if lautstärke_slider.griff_x > mitte_x + 650:
                lautstärke_slider.griff_x = mitte_x + 650
        if event.type == Musik_ende:
            next_song()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE and main_menu == "game":
                main_menu = "Pause"
            if event.key == pygame.K_RIGHT and letzte_bewegungsrichtung != "Links":
                Richtung = "Rechts"
            if event.key == pygame.K_LEFT and letzte_bewegungsrichtung != "Rechts" and letzte_bewegungsrichtung != "Stop":
                Richtung = "Links"
            if event.key == pygame.K_UP and letzte_bewegungsrichtung != "Unten":
                Richtung = "Oben"
            if event.key == pygame.K_DOWN and letzte_bewegungsrichtung != "Oben":
                Richtung = "Unten"
        if event.type == pygame.QUIT:
            Spiel = False


    lautstärke = lautstärke_slider.get_value() / 100
    pygame.mixer.music.set_volume(lautstärke)   

    # Alles anzeigen
    pygame.display.flip()

    # FPS
    uhr = pygame.time.Clock()
    uhr.tick(60)

pygame.quit()