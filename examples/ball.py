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
        self.speed.x += self.acceleration.x
        self.speed.y += self.acceleration.y
        self.position.x += self.speed.x
        self.position.y += self.speed.y

    #Definimos una función para acelerar la pelota:
    def accelerate(self, acceleration):
        self.acceleration.x = acceleration[0]
        self.acceleration.y = acceleration[1]

    #Definimos una función para establecer una velocidad:
    def set_speed(self, speed):
        self.speed.x = speed[0]
        self.speed.y = speed[1]

    def set_speed_x(self, speed_x):
        self.speed.x = speed_x
