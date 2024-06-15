import pygame
from entidades import EntidadJuego


# Definimos la clase Proyectil que hereda de EntidadJuego
class Proyectil(EntidadJuego):
    # El método __init__ se llama cuando se crea una nueva instancia de Proyectil
    def __init__(self, x, y, imagen, velocidad):
        # Cargamos la imagen del proyectil
        self.imagen = pygame.image.load(imagen)
        # Obtenemos el rectángulo delimitador de la imagen
        self.rect = self.imagen.get_rect()
        # Posicionamos el rectángulo en las coordenadas (x, y) proporcionadas
        self.rect.centerx = x
        self.rect.top = y
        # Establecemos la velocidad del proyectil
        self.velocidad = velocidad

    # Definimos el método mover que actualiza la posición del proyectil
    def mover(self):
        # Incrementamos la coordenada y del rectángulo en la velocidad del proyectil
        self.rect.y += self.velocidad

    # Definimos el método dibujar que dibuja el proyectil en la pantalla
    def dibujar(self, pantalla):
        # Dibujamos la imagen del proyectil en la pantalla en la posición del rectángulo
        pantalla.blit(self.imagen, self.rect)