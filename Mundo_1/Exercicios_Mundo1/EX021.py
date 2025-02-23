import pygame

arquivo = r'C:\Users\User\Music\downloads\Agora viu que perdeu e chora - Dor de Amor - O show tem que continuar - [Quintal dos Prettos - DVD].mp3'

pygame.mixer.init()
pygame.mixer.music.load(arquivo)
pygame.mixer.music.play()

while pygame.mixer.music.get_busy():
    pygame.time.Clock().tick(10)
