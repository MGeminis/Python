import time
import sys
import os
os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "hide"
import pygame

MUSIC_PATH = r"C:\Python\Song\EnamoradoTuyo.mp3" # ruta de cancion
MUSIC_START = 160 # segundos de inicio de la cancion

lyrics = [
    ("", 0, 0, "", 0),
    ("  Y si te parece ", 0.09, 0.3, "que yo estoy enamorado tuyo", 0.1),
    ("  Eso es un invento, intuyo, ", 0.082, 0.2, "no des crédito a murmullos", 0.084),
    ("  Porque casi nunca llamo ", 0.09, 0.3, "para decir que te amo", 0.1),
    ("  Y más de una vez lo hice ", 0.085, 0.3, "a un número equivocado", 0.092),
    ("  Casi nunca nadie dice ", 0.098, 0.35, "que yo estoy enamorado tuyo", 0.105),
    ("  No te vistas, ", 0.035, 0.2, "no te hagás la nunca vista", 0.09),
    ("  Tengo en vista cantarte un ", 0.08, 0.9, "hasta la vista", 0.08),
    ("  No te vistas, ", 0.04, 0.2, "no te hagás la nunca vista", 0.09),
    ("  Tengo lista una canción ", 0.07, 0.1, "que dice:", 0.08),
    ("  HASTA LA VISTA, ", 0.1, 0.4, "SEÑORITA", 0.28)
]

line_delays = [
    0,
    0, 
    0.3,
    0.15,
    0.2,
    0.23,
    4.42,
    1.73,
    0.7,
    1.75,
    0.37,
    10
]

colors = [
    "\033[35m","\033[33m","\033[32m","\033[34m","\033[37m","\033[36m","\033[38;5;208m",
    "\033[91m","\033[95m","\033[93m","\033[33m"
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
    os.system("cls")
    sys.stdout.write("\033[?25l")
    sys.stdout.flush()

    try:
        play_music()

        for i, line in enumerate(lyrics):
            parte1, speed1, wait, parte2, speed2 = line
            color = colors[i % len(colors)]
        
            animate_text(parte1, speed1, color)
            time.sleep(wait)
            animate_text(parte2, speed2, color)
            print()
        
            if i < len(line_delays):
                time.sleep(line_delays[i])

    finally:
        sys.stdout.flush()

if __name__ == "__main__":
    sing_song()
