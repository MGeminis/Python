import time
import sys
import os
import pygame

MUSIC_PATH = r"C:\Python\Song\NoSalesDeMiMente.mp3" # ruta de cancion
MUSIC_START = 58.8 # segundos de inicio de la cancion

lyrics = [
    ("  MGéminis", 0.1, 0, "", 0, 0),
    ("", 0, 0, "", 0, 1),
    ("  Esa boquita de miel ", 0.058, 0, "", 0, 0.23),
    ("  y como combina el sabor con su piel, ", 0.058, 0, "", 0, 0.17),
    ("  Es que no existe nadie como tú, ", 0.05, 0.04, "mi mujer,", 0.05, 0.18),
    ("  Sigo buscando a otra", 0.045, 0, "", 0, 0),
    ("  Pero no hay como usted, ", 0.05, 0.01, "mami no es de embuste", 0.05, 0.1),
    ("  Y enseguida te vas", 0.06, 0, "", 0, 0.4),
    ("  Me dices que tú sabes, ", 0.045, 0.055, "pero no sabes nada", 0.055, 0.28),
    ("  Dime por qué te fuiste, ", 0.04, 0.05, "solo di la verdad", 0.06, 0.3),
    ("  Sigo buscándote ", 0.05, 0.02, "y no he podido encontrar", 0.05, 0.09),
    ("  Quien podrá reemplazarte ", 0.06, 0.02, "a ti", 0.06, 0.24),
    ("  Tú me enseñaste cómo amar  ", 0.085, 0.67, "y ahora que te vas", 0.09, 1.28),
    ("  No me enseñaste cómo estar ", 0.09, 0.09, "sin ti", 0.11, 0.55),
    ("  Tú me enseñastes cómo amar ", 0.085, 0.67, "y ahora que te vas", 0.1, 1.27),
    ("  No me enseñastes cómo estar ", 0.09, 0.09, "sin ti", 0.11, 6)
]

colors = [
    "\033[35m","\033[32m","\033[33m","\033[34m","\033[37m","\033[36m","\033[32m",
    "\033[91m","\033[95m","\033[93m","\033[33m","\033[91m","\033[34m","\033[97m",
    "\033[32m","\033[38;5;208m"
]

in_parenthesis = False
def animate_text(text, delay, color):
    global in_parenthesis
    i = 0

    while i < len(text):
        char = text[i]

        if char == "(":
            in_parenthesis = True
            sys.stdout.write(f"\033[2m{color}{char}\033[0m")
        elif char == ")":
            sys.stdout.write(f"\033[2m{color}{char}\033[0m")
            in_parenthesis = False
        elif in_parenthesis:
            sys.stdout.write(f"\033[2m{color}{char}\033[0m")
        else:
            sys.stdout.write(f"{color}{char}\033[0m")

        sys.stdout.flush()
        time.sleep(delay)
        i += 1

def play_music():
    if not os.path.exists(MUSIC_PATH):
        print("No se encontró el archivo de música")
        return

    pygame.mixer.init()
    pygame.mixer.music.load(MUSIC_PATH)
    pygame.mixer.music.play(start=MUSIC_START)

def sing_song():
    sys.stdout.write("\033[?25l")
    sys.stdout.flush()

    try:
        play_music()

        for i, line in enumerate(lyrics):
            parte1, speed1, wait, parte2, speed2, next_delay = line
            color = colors[i % len(colors)]

            animate_text(parte1, speed1, color)
            time.sleep(wait)
            animate_text(parte2, speed2, color)
            print()

            time.sleep(next_delay)

    finally:
        sys.stdout.flush()


if __name__ == "__main__":
    sing_song()


