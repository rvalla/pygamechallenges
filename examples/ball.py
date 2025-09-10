#Vamos a crear una clase pelota.
class Ball():

    #Para instanciar una pelota se llama al constructor:
    def __init__(self, size, color, position, speed, acceleration):
        self.size = size
        self.color = color
        self.position = position
        self.speed = speed
        self.acceleration = acceleration

    #Definimos una función para actualizar la pelota:
    def update(self):
        self.speed[0] += self.acceleration[0]
        self.speed[1] += self.acceleration[1]
        self.position[0] += self.speed[0]
        self.position[1] += self.speed[1]

    #Definimos una función para acelerar la pelota:
    def accelerate(self, acceleration):
        self.acceleration = acceleration

    #Definimos una función para establecer una velocidad:
    def set_speed(self, speed):
        self.speed = speed

    def set_speed_x(self, speed_x):
        self.speed[0] = speed_x
