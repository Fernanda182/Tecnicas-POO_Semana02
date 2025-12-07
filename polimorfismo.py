# Polimorfismo
# Autor: Jenifer Fernanda Vaca

class Figura:

    def area(self):
        print("Área genérica.")


class Cuadrado(Figura):

    def __init__(self, lado):
        self.lado = lado

    def area(self):
        print("Área del cuadrado:", self.lado * self.lado)


class Circulo(Figura):

    def __init__(self, radio):
        self.radio = radio

    def area(self):
        print("Área del círculo:", 3.1416 * (self.radio ** 2))


figuras = [Cuadrado(4), Circulo(3)]

for f in figuras:
    f.area()