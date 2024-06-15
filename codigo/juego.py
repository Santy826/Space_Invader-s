import pygame
from texturas import cargar_texturas
from jugador import Jugador
from enemigo import Enemigo
from jefeFinal import JefeFinal
from sonidos import cargar_sonidos

# Clase principal del juego
class Juego:
    def __init__(self):
        pygame.init()   # Inicializar pygame
        self.ancho, self.alto = 800, 600    # Dimensiones de la pantalla
        self.pantalla = pygame.display.set_mode((self.ancho, self.alto))    # Crear pantalla
        pygame.display.set_caption("Space Invader")
        self.clock = pygame.time.Clock()    # Reloj para controlar la velocidad del juego
        self.texturas = cargar_texturas()   # Cargar texturas
        self.sonidos = cargar_sonidos()     # Cargar sonidos
        self.jugador = Jugador(self.texturas['jugador'], self.sonidos['disparo'])   # Crear jugador
        self.enemigos = [Enemigo(self.texturas[f'enemigo{i}'], 3) for i in range(1, 4)]

        # Reproducir música de fondo usando el sonido cargado
        self.sonidos['principal'].play(-1)  # -1 para reproducir en bucle

       # Crear una lista de 20 enemigos utilizando las texturas disponibles
        self.enemigos = []
        for i in range(5):
            self.enemigos.append(Enemigo(self.texturas['enemigo1'], 3))
            self.enemigos.append(Enemigo(self.texturas['enemigo2'], 3))
            self.enemigos.append(Enemigo(self.texturas['enemigo3'], 3))
            self.enemigos.append(Enemigo(self.texturas['enemigo4'], 3))
            self.enemigos.append(Enemigo(self.texturas['enemigo5'], 3))

        self.jefe_final = JefeFinal(self.texturas['jefeFinal'], self.sonidos['disparo'])
        self.jefe_final.vivo = False
        self.puntaje = 0    # Puntaje inicial
        self.vidas = 200    # Vidas iniciales
        self.corriendo = True   # Variable para controlar el ciclo del juego

    def manejar_eventos(self):
        # Manejar los eventos del juego
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                self.corriendo = False
            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_SPACE:
                    self.jugador.disparar()

    def actualizar(self):
        # Actualizar el estado del juego
        self.jugador.mover()
        self.jugador.actualizar_proyectiles(self.enemigos, self)

        for enemigo in self.enemigos:
            enemigo.mover(self.jugador.rect)
        if not self.enemigos and not self.jefe_final.vivo:  
            self.jefe_final.vivo = True
        if self.jefe_final and self.jefe_final.vivo:
            self.jefe_final.mover()
            self.jefe_final.disparar()
            self.jefe_final.actualizar_proyectiles()
        self.detectar_colisiones()

    def detectar_colisiones(self):
        # Detectar colisiones entre proyectiles y enemigos
        for proyectil in self.jugador.proyectiles:
            for enemigo in self.enemigos:
                if proyectil.rect.colliderect(enemigo.rect):
                    if enemigo.recibir_dano(1):
                        self.enemigos.remove(enemigo)
                    self.jugador.proyectiles.remove(proyectil)
                    self.puntaje += 50
                    self.sonidos['colision'].play()
                    break
         # Detectar colisiones entre proyectiles y el jefe final                
        for proyectil in self.jugador.proyectiles:
            if proyectil.rect.colliderect(self.jefe_final.rect):
                self.jugador.proyectiles.remove(proyectil)
                self.jefe_final.recibir_dano(10)

        # Detectar colisiones entre proyectiles del jefe final y el jugador
        for proyectil in self.jefe_final.proyectiles:
            if proyectil.rect.colliderect(self.jugador.rect):
                self.jefe_final.proyectiles.remove(proyectil)
                self.vidas -= 50
                self.sonidos['colision'].play()
                if self.vidas <= 0:
                    self.mostrar_game_over()
                    self.corriendo = False
                break

        # Detectar colisiones entre enemigos y el jugador
        for enemigo in self.enemigos:
            if enemigo.rect.colliderect(self.jugador.rect):
                self.mostrar_game_over()
                self.corriendo = False

    def dibujar(self):
        # Dibujar todos los elementos del juego en la pantalla
        self.pantalla.blit(self.texturas['fondo'], (0, 0))
        self.jugador.dibujar(self.pantalla)
        for enemigo in self.enemigos:
            enemigo.dibujar(self.pantalla)
        if self.jefe_final and self.jefe_final.vivo:
            self.jefe_final.dibujar(self.pantalla)
            self.dibujar_barra_vida(self.jefe_final.rect.x, self.jefe_final.rect.y - 20, self.jefe_final.vida, 100, (255, 0, 0))
        self.dibujar_barra_vida(self.jugador.rect.x, self.jugador.rect.y - 20, self.jugador.vida, 130, (0, 255, 0))
        self.mostrar_puntaje()
        self.mostrar_vidas()

        pygame.display.flip()   # Actualizar pantalla

    def dibujar_barra_vida(self, x, y, vida, vida_maxima, color):
        # Dibujar la barra de vida de un personaje
        ancho_barra = 40
        alto_barra = 10
        ancho_vida = int(ancho_barra * vida / vida_maxima)
        barra_rect = pygame.Rect(x, y, ancho_barra, alto_barra)
        vida_rect = pygame.Rect(x, y, ancho_vida, alto_barra)
        pygame.draw.rect(self.pantalla, (255, 0, 0), barra_rect)
        pygame.draw.rect(self.pantalla, color, vida_rect)

    def mostrar_puntaje(self):
        # Mostrar el puntaje en la pantalla
        fuente = pygame.font.Font(None, 36)
        texto = fuente.render(f"Puntaje: {self.puntaje}", True, (255, 255, 255))
        self.pantalla.blit(texto, (10, 10))

    def mostrar_vidas(self):
        # Mostrar las vidas en la pantalla
        fuente = pygame.font.Font(None, 36)
        texto = fuente.render(f"Vidas: {self.vidas}", True, (255, 255, 255))
        self.pantalla.blit(texto, (650, 10))

    def mostrar_winner(self):
        # Mostrar el mensaje de ganador
        fuente = pygame.font.Font(None, 74)
        texto = fuente.render("Winner", True, (0, 255, 0))
        self.pantalla.blit(texto, (300, 250))
        pygame.display.flip()
        pygame.time.wait(2000)

    def mostrar_game_over(self):
        # Mostrar el mensaje de game over
        fuente = pygame.font.Font(None, 74)
        texto = fuente.render("Game Over", True, (255, 0, 0))
        self.pantalla.blit(texto, (250, 300))
        pygame.display.flip()
        pygame.time.wait(2000)

    def mostrar_portada(self):
        # Mostrar el menú principal
        menu = True
        while menu:
            self.pantalla.blit(self.texturas['portada'], (0, 0))
            fuente_menu = pygame.font.Font('Tiny5/Tiny5-Regular.ttf', 35)
            iniciar = fuente_menu.render("1. Iniciar Juego", True, (255, 255, 255))
            tutorial = fuente_menu.render("2. Cómo Jugar", True, (255, 255, 255))
            salir = fuente_menu.render("3. Salir", True, (255, 255, 255))

            self.pantalla.blit(iniciar, (300, 250))
            self.pantalla.blit(tutorial, (300, 320))
            self.pantalla.blit(salir, (300, 390))

            pygame.display.flip()

            for evento in pygame.event.get():
                # Si el evento es QUIT (cierre de la ventana)
                if evento.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                 # Si el evento es una tecla presionada
                elif evento.type == pygame.KEYDOWN:
                    # Si la tecla presionada es ESPACIO
                    if evento.key == pygame.K_SPACE:
                        # Llamamos a la función disparar
                        self.disparar()
                    # Si la tecla presionada es 1
                    if evento.key == pygame.K_1:
                        # Salimos del menú y detenemos la música principal
                        menu = False
                        self.sonidos['principal'].stop()  # Detener la música
                    elif evento.key == pygame.K_2:
                        self.mostrar_tutorial()
                    elif evento.key == pygame.K_3:
                        # Cerramos Pygame y salimos del programa
                        pygame.quit()
                        exit()

    def mostrar_tutorial(self):
        # Mostrar tutorial
        tutorial = True

        # Definimos un desplazamiento en el eje y para el texto del tutorial
        y_offset = 300

        # Mientras el tutorial esté activo
        while tutorial:
            # Dibujamos la portada en la pantalla en la posición (0,0)
            self.pantalla.blit(self.texturas['portada'], (0, 0))

            # Definimos la fuente del texto del tutorial, especificando la ruta de la fuente y el tamaño
            fuente_tutorial = pygame.font.Font('Tiny5/Tiny5-Regular.ttf', 25)

            # Definimos el texto del tutorial como una lista de strings
            texto_tutorial = [
                "1.Usa las flechas izquierda y derecha para moverte",
                "2.Presiona ESPACIO para disparar",
                "3.Evita los disparos enemigos y destruye a los enemigos",
                "4.El juego termina si los enemigos te tocan o pierdes todas tus vidas",
                
                "Presiona ESC para regresar"
            ]

            for i, linea in enumerate(texto_tutorial):
                texto = fuente_tutorial.render(linea, True, (255, 255, 255))
                # self.pantalla.blit(texto, (50, 50 + i * 50))
                self.pantalla.blit(texto, (50, i * 30 + y_offset))  
            pygame.display.flip()

            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                elif evento.type == pygame.KEYDOWN:
                    if evento.key == pygame.K_ESCAPE:
                        tutorial = False

    def ejecutar(self):
        # Mostramos la pantalla de inicio del juego
        self.mostrar_portada()

        # Mientras el juego esté corriendo
        while self.corriendo:

            # Manejamos los eventos del usuario (teclas presionadas, etc.)
            self.manejar_eventos()

            # Actualizamos el estado del juego (posición de los personajes, colisiones, etc.)
            self.actualizar()

             # Dibujamos el estado actual del juego en la pantalla
            self.dibujar()

            # Si el jugador se queda sin vidas o si algún enemigo llega al fondo de la pantalla
            if self.vidas <= 0 or any(enemigo.rect.bottom >= self.alto for enemigo in self.enemigos):
                self.mostrar_game_over()
                self.corriendo = False
            
            # Si el jefe final está vivo y su vida llega a 0
            if self.jefe_final.vivo and self.jefe_final.vida <= 0:
                # Mostramos la pantalla de "Winner"
                self.mostrar_winner()

                # Terminamos el juego
                self.corriendo = False

            # Limitamos el juego a 60 fotogramas por segundo    
            self.clock.tick(60)

        # Cuando el juego termina, cerramos Pygame    
        pygame.quit()


if __name__ == "__main__":
    # Creamos una instancia del juego
    juego = Juego()

    # Ejecutamos el juego
    juego.ejecutar()