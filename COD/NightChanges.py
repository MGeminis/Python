import os
import time
import sys
import pygame

MUSIC_PATH = r"C:\Python\Song\NightChanges.mp3" # ruta de cancion
MUSIC_START = 38 # segundos de inicio de la cancion 

# letras - velocidad - tiempo - letras - velocidad - tiempo - letras - velocidad
lyrics = [
    ("  MGéminis", 0.1, 0, "", 0, 0, "", 0),                                   #1   
    ("", 0, 0, "", 0, 0, "", 0),                                               #2   
    ("  We're only getting ", 0.06, 0.2, "older, ", 0.08, 0.3, "baby", 0.2),   #3  
    ("  And I've been thinking about ", 0.06, 0.35, "it lately", 0.1, 0, "", 0),#4  
    ("  Does it ever drive you crazy", 0.09, 0.6, "", 0, 0, "", 0.1),          #5  
    ("  Just how fast the night ", 0.07, 1, "changes?", 0.09, 0, "", 0.1),     #6   
    ("  Everything that you've ever dreamed of", 0.08, 0, "", 0, 0, "", 0),    #7 
    ("  Disappearing when you wake up", 0.095, 0, "", 0, 0, "", 0),            #8 
    ("  But there's nothing to be afraid of", 0.08, 0.4, "", 0, 0, "", 0.11),  #9
    ("  Even when the night ", 0.09, 0.9, "changes", 0.09, 0, "", 0),          #10
    ("  It will never change ", 0.08, 0.9, "me and you...", 0.08, 0, "", 0),   #11
    ("", 0, 0, "", 0, 0, "", 0)                                                #12
]  

delays = [
    0,    #1  
    0,    #2  
    1.5,  #3 
    2.35, #4  
    3.2,  #5  
    3.4,  #6  
    4.35, #7  
    5.15, #8  
    6.19, #9 
    6.3,  #10  
    7.25, #11   
    11    #12
]

colors = [
    "\033[31m","\033[32m","\033[33m","\033[34m","\033[32m","\033[36m","\033[37m",
    "\033[91m","\033[92m","\033[93m","\033[94m","\033[95m",
]

def animate_text(text, delay, color):
    i = 0
    while i < len(text):
        if text[i] == "(":
            sys.stdout.write(f"\033[2m{color}{text[i]}\033[0m")
            sys.stdout.flush()
            time.sleep(delay)
            i += 1

            sys.stdout.write(f"\033[2m{color}")
            sys.stdout.flush()
            while i < len(text) and text[i] != ")":
                sys.stdout.write(text[i])
                sys.stdout.flush()
                time.sleep(delay)
                i += 1

            if i < len(text) and text[i] == ")":
                sys.stdout.write(text[i])
                sys.stdout.flush()
                time.sleep(delay)
                i += 1

            sys.stdout.write("\033[0m")
            sys.stdout.flush()
        else:
            sys.stdout.write(f"{color}{text[i]}\033[0m")
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

        for i in range(len(lyrics)):
            parte1, speed1, wait1, parte2, speed2, wait2, parte3, speed3 = lyrics[i]
            color = colors[i % len(colors)]
    
            time.sleep(delays[i] - (delays[i-1] if i > 0 else 0))
    
            animate_text(parte1, speed1, color)
            time.sleep(wait1)
            animate_text(parte2, speed2, color)
            time.sleep(wait2)
            animate_text(parte3, speed3, color)
            print()
            
    finally:
        sys.stdout.flush()


if __name__ == "__main__":
    sing_song()