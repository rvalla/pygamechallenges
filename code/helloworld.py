import pygame

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

    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        position.y -= 10
    if keys[pygame.K_DOWN]:
        position.y += 10
    if keys[pygame.K_RIGHT]:
        position.x -= 10
    if keys[pygame.K_LEFT]:
        position.x += 10

    position.x += 1

    #Actualizamos la pantalla...
    pygame.display.flip()

    #Establecemos una velocidad de reproducción FPS...
    clock.tick(24)


pygame.quit()
