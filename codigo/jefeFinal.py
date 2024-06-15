import pygame
from entidades import EntidadJuego
from proyectil import Proyectil


class JefeFinal(EntidadJuego):
    # Inicializamos la entidad con su textura, posición, velocidad y vida
    # También inicializamos la lista de proyectiles y el tiempo del último disparo

    def __init__(self, textura, sonido_disparo):
        self.imagen = textura
        self.rect = self.imagen.get_rect()
        self.rect.centerx = 400
        self.rect.y = 50
        self.velocidad_x = 5
        self.vivo = True
        self.sonido_disparo = sonido_disparo
        self.proyectiles = []
        self.tiempo_ultimo_disparo = 0
        self.intervalo_disparo = 100  # Dispara cada 2 segundos
        self.vida = 500  # Agregar el atributo vida

    def mover(self):
        # Movemos la entidad de izquierda a derecha en la pantalla
        # Si llega a un borde, cambiamos la dirección de la velocidad
        self.rect.x += self.velocidad_x
        if self.rect.right >= 800 or self.rect.left <= 0:
            self.velocidad_x = -self.velocidad_x

    def disparar(self):
        tiempo_actual = pygame.time.get_ticks()

        # Si ha pasado suficiente tiempo desde el último disparo, creamos un nuevo proyectil
        if tiempo_actual - self.tiempo_ultimo_disparo >= self.intervalo_disparo:
            proyectil = Proyectil(self.rect.centerx, self.rect.bottom, 'texturas/proyectil1.png', 7)
            self.proyectiles.append(proyectil)
            self.sonido_disparo.play()
            self.tiempo_ultimo_disparo = tiempo_actual

    def actualizar_proyectiles(self):
        for proyectil in self.proyectiles:
            proyectil.mover()
            if proyectil.rect.top > 600:
                self.proyectiles.remove(proyectil)

    def dibujar(self, pantalla):
        # Dibujamos la entidad y todos sus proyectiles en la pantalla
        pantalla.blit(self.imagen, self.rect)
        for proyectil in self.proyectiles:
            proyectil.dibujar(pantalla)

    def dibujar_barra_vida(self, pantalla):
        largo_barra = 100
        alto_barra = 10
        vida_restante = (self.vida / 100) * largo_barra
        borde_barra = pygame.Rect(self.rect.x, self.rect.y - 20, largo_barra, alto_barra)
        barra_vida = pygame.Rect(self.rect.x, self.rect.y - 20, vida_restante, alto_barra)
        pygame.draw.rect(pantalla, (255, 0, 0), barra_vida)
        pygame.draw.rect(pantalla, (255, 255, 255), borde_barra, 2)

    def recibir_dano(self, cantidad):
        # Reducimos la vida de la entidad en la cantidad especificada
        self.vida -= cantidad
        if self.vida < 0:
            self.vida = 0