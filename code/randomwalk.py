import pygame
import random as rd

#Primero hay que inicializar el entorno...
pygame.init()
screen = pygame.display.set_mode((600, 600))
clock = pygame.time.Clock()
running = True

#Definimos una posición...
position = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
diameter = 50

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #Tapamos el cuadro anterior...
    screen.fill("black")

    pygame.draw.circle(screen, "white", position, diameter)

    #Cambiamos la posición del círculo al azar...
    position.x += rd.randint(0,6) - 3
    position.y += rd.randint(0,6) - 3

    #Volvemos al centro con el espacio...
    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE]:
        position.x = screen.get_width() / 2
        position.y = screen.get_height() / 2

    #Actualizamos la pantalla...
    pygame.display.flip()

    #Establecemos una velocidad de reproducción FPS...
    clock.tick(24)


pygame.quit()
