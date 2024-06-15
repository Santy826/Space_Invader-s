import pygame


class Menu:
    def __init__(self, pantalla):
        # Inicializamos la clase con la pantalla del juego
        self.pantalla = pantalla

    def mostrar(self):
        # Dibujamos la portada en la pantalla en la posición (0,0)
        self.pantalla.blit(self.texturas['portada'], (0, 0))

        # Rellenamos la pantalla con color negro
        self.pantalla.fill((0, 0, 0))

        # Actualizamos la pantalla
        pygame.display.flip()

        # Esperamos a que el usuario presione la tecla ENTER para salir del menú
        esperando = True
        while esperando:
            for evento in pygame.event.get():
                # Si el usuario cierra la ventana, salimos del juego
                if evento.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if evento.type == pygame.KEYDOWN and evento.key == pygame.K_RETURN:
                    # Si el usuario presiona ENTER, salimos del menú
                    esperando = False