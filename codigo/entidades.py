import abc


class EntidadJuego(abc.ABC):
    @abc.abstractmethod
    def mover(self):
        pass

    @abc.abstractmethod
    def dibujar(self, pantalla):
        pass