@startuml

class Juego {
    - ancho: int
    - alto: int
    - pantalla: Surface
    - clock: Clock
    - texturas: dict
    - sonidos: dict
    - jugador: Jugador
    - enemigos: list<Enemigo>
    - jefe_final: JefeFinal
    - puntaje: int
    - vidas: int
    - corriendo: bool
    + __init__()
    + manejar_eventos()
    + actualizar()
    + detectar_colisiones()
    + dibujar()
    + dibujar_barra_vida()
    + mostrar_puntaje()
    + mostrar_vidas()
    + mostrar_winner()
    + mostrar_game_over()
    + mostrar_portada()
    + mostrar_tutorial()
    + ejecutar()
}

class EntidadJuego {
    - imagen: Surface
    - rect: Rect
    + dibujar(pantalla: Surface)
}

class Jugador {
    - imagen: Surface
    - rect: Rect
    - velocidad: int
    - sonido_disparo: Sound
    - proyectiles: list<Proyectil>
    - vida: int
    + __init__(textura, sonido_disparo)
    + mover()
    + disparar()
    + actualizar_proyectiles(enemigos: list<Enemigo>, juego: Juego)
    + recibir_dano(cantidad: int)
    + dibujar(pantalla: Surface)
    + dibujar_barra_vida(pantalla: Surface)
}

class Enemigo {
    - imagen: Surface
    - rect: Rect
    - velocidad: int
    - vida: int
    + mover(jugador_rect: Rect)
    + recibir_dano(cantidad: int)
    + dibujar(pantalla: Surface)
}

class JefeFinal {
    - imagen: Surface
    - rect: Rect
    - velocidad: int
    - vida: int
    - vivo: bool
    + mover()
    + disparar()
    + actualizar_proyectiles()
    + recibir_dano(cantidad: int)
    + dibujar(pantalla: Surface)
}

class Proyectil {
    - imagen: Surface
    - rect: Rect
    - velocidad: int
    + __init__(x, y, imagen, velocidad)
    + mover()
    + dibujar(pantalla: Surface)
}

class Menu {
    - pantalla: Surface
    + mostrar()
}

class cargar_sonidos {
    + cargar_sonidos()
}

class cargar_texturas {
    + cargar_texturas()
}

Jugador --|> EntidadJuego
Enemigo --|> EntidadJuego
JefeFinal --|> EntidadJuego
Proyectil --|> EntidadJuego

@enduml
