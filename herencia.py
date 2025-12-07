# Herencia
# Autor: Jenifer Fernanda Vaca Escobar

class Animal:
    
    def comer(self):
        print("El animal está comiendo.")


class Perro(Animal):
    
    def ladrar(self):
        print("El perro ladra: ¡Guau!")


perro = Perro()
perro.comer()
perro.ladrar()