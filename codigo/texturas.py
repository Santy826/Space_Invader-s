import pygame


def cargar_texturas():
    texturas = {
        'fondo': pygame.image.load('texturas/cielo.png'),
        'portada': pygame.image.load('texturas/menu.png'),
        'jugador': pygame.image.load('texturas/nave.png'),
        'enemigo1': pygame.image.load('texturas/enemigo4.png'),
        'enemigo2': pygame.image.load('texturas/enemigo2.png'),
        'enemigo3': pygame.image.load('texturas/enemigo3.png'),
        'enemigo4': pygame.image.load('texturas/ayuda1.png'),
        'enemigo5': pygame.image.load('texturas/ayuda2.png'),
        'jefeFinal': pygame.image.load('texturas/jefeFinal.png')
    }
    return texturas