import pygame
import random
from entidades import EntidadJuego


class Enemigo(EntidadJuego):
    """
        Inicializa la instancia de Enemigo con una textura de imagen y puntos de vida.

        :param textura: Superficie de Pygame que contiene la imagen del enemigo.
        :param vida: Puntos de vida del enemigo.
        """
    def __init__(self, textura, vida):
        self.imagen = textura
        self.rect = self.imagen.get_rect()
        self.rect.x = random.randint(0, 736)
        self.rect.y = random.randint(50, 150)
        self.velocidad_x = 1
        self.velocidad_y = 1
        self.vida = vida

    def mover(self, jugador_rect):
        """
        Mueve al enemigo hacia la posición del jugador.

        :param jugador_rect: Rectángulo del jugador (representa su posición y dimensiones).
        """

        # Mueve hacia la posición del jugador en el eje x
        if self.rect.x < jugador_rect.x:
            self.rect.x += self.velocidad_x
        elif self.rect.x > jugador_rect.x:
            self.rect.x -= self.velocidad_x

        # Mueve hacia la posición del jugador en el eje y
        if self.rect.y < jugador_rect.y:
            self.rect.y += self.velocidad_y
        elif self.rect.y > jugador_rect.y:
            self.rect.y -= self.velocidad_y

    def recibir_dano(self, dano):
        """
        Reduce los puntos de vida del enemigo por una cantidad específica.

        :param dano: Cantidad de puntos de vida a reducir.
        :return: True si el enemigo ha sido derrotado (vida <= 0), False en caso contrario.
        """
        self.vida -= dano
        if self.vida <= 0:
            return True
        return False

    def dibujar(self, pantalla):
        """
        Dibuja al enemigo en la pantalla.

        :param pantalla: Superficie de Pygame donde se dibuja el enemigo.
        """
        pantalla.blit(self.imagen, self.rect)