import time
import sys
import os
import pygame

MUSIC_PATH = r"C:\Python\Song\DesconexiónEmocional.mp3" # ruta de cancion
MUSIC_START = 134.7 # segundos de inicio de la cancion

# letras - velocidad de escritura - tiempo de espera - letras - velocidad de escritura
lyrics = [
    ("  MGéminis", 0.1, 0, "", 0),                                  #1
    ("", 0, 0, "", 0),                                              #2
    ("  Tengo miedo de ", 0.1, 0.2, "continuar", 0.17),                #3 
    ("  Si paro no sé ", 0.1, 0.2, "qué sucederá", 0.2),        #4
    ("  Todo podría ", 0.11, 0.3, "terminar", 0.2),                 #5
    ("  ¡Una ", 0.1, 0.2, "oportunidad!", 0.23),                #6
    ("  No hay nadie que entienda ", 0.09, 0.22, "más que yo", 0.15),#7
    ("  Que estoy cansado, ", 0.11, 0.5, "desvelado", 0.24),       #8 
    ("  Sintiendo que todo ", 0.12, 0.23, "se acabó", 0.19),     #9
    ("  Pero eso es solo el ", 0.12, 0.2, "principio", 0.13),#10
    ("  (No hay nadie que entienda ", 0.09, 0.17, "más que yo)", 0.15),      #11              
    ("  (Que estoy cansado, ", 0.11, 0.5, "desvelado)", 0.24),              #12      
    ("", 0, 0, "", 0),                                              #13
]

# tiempo retardado entre cada fila
delays = [0,     #1   
          1,     #2 
          1.09,  #3 
          3,  #4 
          4.1,  #5 
          4.7,  #6 
          7.7,  #7 
          8.7,  #8 
          9,  #9 
          10.015,  #10
          11.36,  #11
          12.05,  #12
          18]  #13

colors = [
    "\033[35m","\033[32m","\033[33m","\033[34m","\033[37m","\033[36m","\033[32m",
    "\033[91m","\033[95m","\033[93m","\033[94m"
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

        for i in range(len(lyrics)):
            parte1, speed1, wait, parte2, speed2 = lyrics[i]
            color = colors[i % len(colors)]

            time.sleep(delays[i] - (delays[i-1] if i > 0 else 0))

            animate_text(parte1, speed1, color)
            time.sleep(wait)
            animate_text(parte2, speed2, color)
            print()
            
    finally:
        sys.stdout.flush()

if __name__ == "__main__":
    sing_song()


