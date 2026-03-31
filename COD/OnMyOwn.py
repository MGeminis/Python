import time
import sys
import os
import pygame

MUSIC_PATH = r"C:\Python\Song\OnMyOwn.mp3" # ruta de cancion
MUSIC_START = 23 # segundos de inicio de la cancion

lyrics = [
    ("", 0, 0, "", 0, 0),
    ("  There's gotta be another way out ", 0.07, 0, "", 0, 0.23),
    ("  I've been stuck in a cage with my doubt ", 0.058, 0, "", 0, 0.28),
    ("  I've tried ", 0.05, 0.09, "forever getting out on my own", 0.1, 2.06),
    ("  But every time I do this my way", 0.06, 0, "", 0, 0.37),
    ("  I get caught in the lies of the enemy ", 0.06, 0.01, "", 0.05, 0.33),
    ("  I lay my troubles down", 0.08, 0, "", 0, 0.07),
    ("  I'm ready for you now", 0.082, 0, "", 0, 0.45),
    ("  Break me out", 0.07, 0, "", 0, 0.75),
    ("  Come and find me in the dark now", 0.049, 0, "", 0, 0.3),
    ("  Every day by myself I'm breaking down", 0.067, 0, "", 0, 0.75),
    ("  I don't wanna fight alone ", 0.08, 0.03, "anymore", 0.14, 0.49),
    ("  Break me out", 0.07, 0, "", 0, 0.75),
    ("  From the prison of my own pride", 0.049, 0, "", 0, 0.33),
    ("  My God, I need a hope I can't deny", 0.067, 0, "", 0, 0.03),
    ("  In the end ", 0.09, 0.06, "I'm realizing", 0.11, 0.39),
    ("  I was never meant to fight ", 0.049, 0.09, "on my own", 0.08, 0.6),
    ("", 0, 9, "", 0, 7),
]

colors = [
    "\033[35m","\033[32m","\033[33m","\033[34m","\033[37m","\033[36m","\033[32m",
    "\033[91m","\033[95m","\033[93m","\033[33m","\033[91m","\033[34m","\033[97m",
    "\033[32m","\033[38;5;208m","\033[36m"
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


