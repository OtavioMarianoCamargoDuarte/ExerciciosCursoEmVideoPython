import pygame
import time  # para a pausa

pygame.mixer.init()
pygame.init()
pygame.mixer.music.load(
    'C:/Users/prala/Desktop/EstudosPython/ExerciciosCursoEmVideo/ex021.mp3')
pygame.mixer.music.play()

# Aguarde enquanto a música estiver tocando
while pygame.mixer.music.get_busy():
    time.sleep(1)  # Mantém o programa ativo enquanto a música toca
