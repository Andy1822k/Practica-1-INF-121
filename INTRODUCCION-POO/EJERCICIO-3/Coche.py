class Coche:
    
    def __init__(self, marca, modelo, velocidad=0):
        self.marca = marca
        self.modelo = modelo
        self.velocidad = velocidad
        
    def acelerar(self):
        self.velocidad += 10
        print(f"{self.marca} {self.modelo} ha acelerado. Velocidad actual: {self.velocidad} km/h")

    def frenar(self):
        self.velocidad -= 5
        if self.velocidad < 0:
            self.velocidad = 0
        print(f"{self.marca} {self.modelo} ha frenado. Velocidad actual: {self.velocidad} km/h")
        
    def mostrar_velocidad(self):
        print(f"{self.marca} {self.modelo} tiene una velocidad de {self.velocidad} km/h")

coche1 = Coche("Toyota", "Corolla")
coche2 = Coche("Ford", "Mustang")
coche1.acelerar()
coche2.acelerar()
coche1.frenar()
coche2.frenar()
coche1.mostrar_velocidad()
coche2.mostrar_velocidad()
