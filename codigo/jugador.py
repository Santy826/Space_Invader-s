import pygame
from entidades import EntidadJuego
from proyectil import Proyectil


class Jugador(EntidadJuego):
    def __init__(self, textura, sonido_disparo):
        self.imagen = textura
        self.rect = self.imagen.get_rect()
        self.rect.centerx = 400 # Posición horizontal inicial del jugador
        self.rect.bottom = 570  # Posición vertical inicial del jugador
        self.velocidad = 10 # Velocidad de movimiento del jugador
        self.sonido_disparo = sonido_disparo    # Sonido de disparo
        self.proyectiles = []   # Lista de proyectiles disparados por el jugador
        self.vida = 250  # Vida inicial del jugador

    def mover(self):
        """
        Mueve al jugador a la izquierda o a la derecha según la tecla presionada.
        """
        teclas = pygame.key.get_pressed()
        if teclas[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= self.velocidad
        if teclas[pygame.K_RIGHT] and self.rect.right < 800:
            self.rect.x += self.velocidad

    def disparar(self):
        """
        Crea un nuevo proyectil y lo añade a la lista de proyectiles del jugador.
        Reproduce el sonido de disparo.
        """
        proyectil = Proyectil(self.rect.centerx, self.rect.top, 'texturas/proyectil1.png', velocidad=-5)
        self.proyectiles.append(proyectil)
        self.sonido_disparo.play()

    def actualizar_proyectiles(self, enemigos, juego):
        """
        Actualiza la posición de los proyectiles y verifica colisiones con enemigos.
        Elimina proyectiles fuera de la pantalla y enemigos alcanzados.
        """
        for proyectil in self.proyectiles:
            proyectil.mover()
            if proyectil.rect.bottom < 0:
                self.proyectiles.remove(proyectil)
            else:
                for enemigo in enemigos:
                    if proyectil.rect.colliderect(enemigo.rect):
                        if enemigo.recibir_dano(1):
                            enemigos.remove(enemigo)
                        self.proyectiles.remove(proyectil)
                        break

    def dibujar(self, pantalla):
        """
        Dibuja al jugador y sus proyectiles en la pantalla.
        """
        pantalla.blit(self.imagen, self.rect)
        for proyectil in self.proyectiles:
            proyectil.dibujar(pantalla)

    def dibujar_barra_vida(self, pantalla):
        """
        Dibuja una barra de vida encima del jugador que refleja su vida actual.
        """
        largo_barra = 100
        alto_barra = 10
        vida_restante = (self.vida / 100) * largo_barra
        borde_barra = pygame.Rect(self.rect.x, self.rect.y - 20, largo_barra, alto_barra)
        barra_vida = pygame.Rect(self.rect.x, self.rect.y - 20, vida_restante, alto_barra)
        pygame.draw.rect(pantalla, (0, 255, 0), barra_vida)
        pygame.draw.rect(pantalla, (255, 255, 255), borde_barra, 2)

    def recibir_dano(self, cantidad):
        """
        Reduce la vida del jugador en la cantidad especificada. La vida no puede ser negativa.
        """
        self.vida -= cantidad
        if self.vida < 0:
            self.vida = 0