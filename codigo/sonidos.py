import pygame


def cargar_sonidos():
    sonidos = {
        'disparo': pygame.mixer.Sound('sonidos/disparo.wav'),
        'colision': pygame.mixer.Sound('sonidos/colision.wav'),
        'principal': pygame.mixer.Sound('sonidos/soundTrack.mp3')
    }
    return sonidos