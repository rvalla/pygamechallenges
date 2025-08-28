import pygame
import random as rd

#Primero hay que inicializar el entorno...
#Definimos el ancho y el alto de la ventanta...
ancho = 800
alto = 800
pygame.init() #inicializamos pygame...
screen = pygame.display.set_mode((ancho, alto)) #creamos la ventana...
clock = pygame.time.Clock() #creamos el reloj para controlar la animación...
el_framerate = 30 #Decidimos la cantidad de cuadros por segundo para la animación...
running = True #Variable para poder parar el juego...

#Necesitamos un vector en donde guardar la posición de un círculo.
#Calculamos primero la mitad de la pantalla:
mitad_ancho = screen.get_width() / 2
mitad_alto = screen.get_height() / 2
#La posición inicial la definimos creando un vector:
position = pygame.Vector2(mitad_ancho, mitad_alto)
#Definimos un diametro para el círculo:
diameter = 50
#Definimos nuestros colores...
fondo = pygame.Color(60,30,40) #Valores para rojo, verde y azul (0-255)...
el_color = pygame.Color(160,200,220)

#Controlamos el random walk.
ancho_ruido = 2
alto_ruido = 2

#Ahora trabajamos en nuestro bucle principal...
while running: #Mientras running sea True vamos a repetir lo que sigue...

    #Vamos a consultar los eventos que ocurren durante una iteración del bucle...
    for event in pygame.event.get():
        if event.type == pygame.QUIT: #Si alguien cierra la ventana...
            running = False #Al terminar esta iteración el bucle se termina...

    #Tapamos el cuadro anterior con el color de fondo...
    screen.fill(fondo)

    #Ahora dibujamos el círculo...
    pygame.draw.circle(screen, el_color, position, diameter)

    #Chequeamos si el usuario toca alguna tecla...
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        alto_ruido += 1 #Aumentamos el rango aleatorio...
    if keys[pygame.K_RIGHT]:
        ancho_ruido += 1
    if keys[pygame.K_SPACE]:
        #Con espacio volvemos al centro...
        position = pygame.Vector2(mitad_ancho, mitad_alto)
        #Volvemos el ancho del ruido al mínimo...
        ancho_ruido = 2
        alto_ruido = 2

    #Actualizamos la posición del círculo:
    position.x += rd.randint(-ancho_ruido, ancho_ruido)
    position.y += rd.randint(-alto_ruido, alto_ruido)

    #Actualizamos la pantalla, esta función es necesaria:
    pygame.display.flip()

    #Establecemos una velocidad de reproducción FPS.
    #Como el reloj cuenta en milisegundos dividimos 1000ms por el framerate:
    clock.tick(1000 / el_framerate)

#Si salimos del bucle while cerramos pygame:
pygame.quit()
