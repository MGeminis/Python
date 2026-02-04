import time
import sys
import os
import pygame

MUSIC_PATH = r"C:\Python\Song\ColorRosa.mp3" # ruta de cancion
MUSIC_START = 131.5 # segundos de inicio de la cancion 

# letras - velocidad de escritura - tiempo de espera - letras - velocidad de escritura
lyrics = [
    ("  MGéminis ", 0.1, 0, "", 0),                                            #1
    ("", 0, 0, "", 0),                                                         #2
    ("  Amé tu forma de reír ", 0.12, 0.35, "cuando yo te conocí", 0.11),      #3       
    ("  y tu manera de llorar ", 0.1, 0.5, "cuando algo iba mal", 0.11),       #4        
    ("  Tambien amé tu sonreír ", 0.1, 0.5, "cuando eras muy feliz", 0.1),     #5          
    ("  y tu manera de ocultar ", 0.1, 0.2, "las ganas hoy de llorar", 0.1),   #6             
    ("  Sé que nada ya diré ", 0.1, 0.6, "es muy fácil de entender", 0.09),    #7           
    ("  mi manera de pensar ", 0.095, 0.5, "no me deja razonar", 0.12),        #8         
    ("  Si pudiera algo hacer, ", 0.09, 0.25, "haría algo por tu bien", 0.11), #9                 
    ("  solo te deseo abrazar", 0.09, 0, "", 0),                               #10                        
    ("  ¡JAMAS TE PODRÉ OLVIDAR! ", 0.095, 0, "", 0),                          #11                     
    ("  no puedo aceptar que no estarás junto a mi lado ", 0.09, 0, "", 0),    #12              
    ("  mi corazón dejó de palpitar, ", 0.1, 0.15, "se rompió...", 0.09),      #13             
    ("  mi amor... ", 0.1, 1.38, "se fue...", 0.12),                            #14
    ("", 0, 5, "", 0),                                                         #15
]

# tiempo retardado entre cada fila
delays = [0,    #1  
          1,    #2 
          1,    #3  
          1.25, #4  
          1.35, #5  
          1.55, #6  
          1.92, #7  
          2.3, #8  
          2.7,  #9  
          3,    #10 
          3.2, #11 
          3.47, #12 
          4.02,  #13 
          4.42, #14 
          4.98 ]   #15

# colores de las letras por fila
colors = [
    "\033[35m","\033[32m","\033[33m","\033[34m","\033[99m","\033[36m","\033[32m",
    "\033[91m","\033[92m","\033[93m","\033[94m","\033[95m","\033[96m","\033[97m"
]

def animate_text(text, delay, color):
    for char in text:
        sys.stdout.write(f"{color}{char}\033[0m")
        sys.stdout.flush()
        time.sleep(delay)

def play_music():
    if not os.path.exists(MUSIC_PATH):
        print("❌ No se encontró el archivo de música")
        return

    pygame.mixer.init()
    pygame.mixer.music.load(MUSIC_PATH)
    pygame.mixer.music.play(start=MUSIC_START)

def sing_song():
    play_music()

    for i in range(len(lyrics)):
        parte1, speed1, wait, parte2, speed2 = lyrics[i]
        color = colors[i % len(colors)]

        time.sleep(delays[i] - (delays[i-1] if i > 0 else 0))

        animate_text(parte1, speed1, color)
        time.sleep(wait)
        animate_text(parte2, speed2, color)
        print()

if __name__ == "__main__":
    sing_song()


