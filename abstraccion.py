from abc import ABC, abstractmethod

# Ejemplo de Abstracción
# Autor: Jenifer Fernanda Vaca Escobar

class Dispositivo(ABC):

    @abstractmethod
    def encender(self):
        pass

    @abstractmethod
    def apagar(self):
        pass


class Laptop(Dispositivo):

    def encender(self):
        print("La laptop está encendiendo...")

    def apagar(self):
        print("La laptop se ha apagado.")


if __name__ == "__main__":
    lap = Laptop()
    lap.encender()
    lap.apagar()