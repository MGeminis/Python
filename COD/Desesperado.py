import time
import sys
import os
import pygame

MUSIC_PATH = r"C:\Python\Song\Desesperado.mp3" # ruta de cancion
MUSIC_START = 121.5 # segundos de inicio de la cancion

# letras - velocidad de escritura - tiempo de espera - letras - velocidad de escritura
lyrics = [
    ("  MGéminis", 0.1, 0, "", 0),                                          #1
    ("", 0, 0, "", 0),                                                      #2
    ("  Por eso voy a tomar", 0.09, 0, "", 0),                              #3  
    ("  Para sacar de mi cabeza, ", 0.08, 0.05, "que aún te amo", 0.08),    #4
    ("  Pues tengo ganas de buscarte en cualquier lado", 0.07, 0, "", 0),   #5        
    ("  Estoy desesperado por tenerte a mi lado, ", 0.11, 2, "yeah", 0.1),  #6          
    ("  Por eso voy a tomar ", 0.1, 0.8, "(por eso voy a tomar)", 0.04),    #7             
    ("  Para sacar de mi cabeza, ", 0.08, 0.05, "que aún te extraño", 0.08),#8           
    ("  Pues tengo ganas de buscarte en cualquier lado ", 0.07, 0, "", 0),  #9         
    ("  Estoy desesperado ", 0.09, 0.7, "por tenerte a mi lado", 0.1),      #10 
    ("", 0, 0, "", 0),                                                      #11                  
]

# tiempo retardado entre cada fila
delays = [0,    #1  
          1,    #2 
          1.09, #3  
          2.99, #4  
          4.69, #5  
          4.99, #6  
          5.44, #7  
          5.69, #8  
          6.99, #9  
          7.19, #10
          14,] #11

# colores de las letras por fila
colors = [
    "\033[35m","\033[32m","\033[33m","\033[34m","\033[37m","\033[36m","\033[32m",
    "\033[91m","\033[95m","\033[93m","\033[94m"
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


