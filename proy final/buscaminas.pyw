import pygame
import random
import time

# Inicializar Pygame
pygame.init()

# Configuración de la ventana de inicio
START_BACKGROUND_COLOR = (200, 200, 200)

# Configuración del juego
WIDTH, HEIGHT = 600, 600
# Colores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)
RED = (255, 0, 0)

# Inicializar la ventana

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Buscaminas")
icono = pygame.image.load("proy final/logo.ico")  # Cambia "icono.png" al nombre real del archivo
pygame.display.set_icon(icono)

# ventana de inicio
def start_screen():
    start_screen = pygame.display.set_mode((WIDTH, HEIGHT))

    font = pygame.font.Font(None, 36)
    
    mensaje="Bienvenido al Buscaminas"
    mensaje2="Elija dificultad:"
    linea1 = font.render(mensaje, True, (0, 0, 0))
    linea2 = font.render(mensaje2, True, (0, 0, 0))
    mines_text_rect = linea1.get_rect(center=(WIDTH // 2, 80))
    mines_text_rect2 = linea2.get_rect(center=(WIDTH // 2, 100))

    facil = pygame.Rect(200, 150, 200, 50)
    medio = pygame.Rect(200, 220, 200, 50)
    dificil = pygame.Rect(200, 290, 200, 50)

    faciltx=font.render("Facil", True,WHITE,)
    facilrect=faciltx.get_rect(center=facil.center)

    mediotx=font.render("Medio", True,WHITE)
    mediorect=mediotx.get_rect(center=medio.center)

    dificiltx=font.render("Dificil", True,WHITE)
    dificilrect=dificiltx.get_rect(center=dificil.center)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if facil.collidepoint(event.pos):
                    return 10  # Cambia esta cantidad según la dificultad
                elif medio.collidepoint(event.pos):
                    return 25  # Cambia esta cantidad según la dificultad
                elif dificil.collidepoint(event.pos):
                    return 35  # Cambia esta cantidad según la dificultad

        start_screen.fill(START_BACKGROUND_COLOR)
        pygame.draw.rect(start_screen, (0, 0, 0), facilrect)
        pygame.draw.rect(start_screen, (0, 0, 0), mediorect)
        pygame.draw.rect(start_screen, (0, 0, 0), dificilrect)
        start_screen.blit(linea1, mines_text_rect)
        start_screen.blit(linea2, mines_text_rect2)

          # Blit texto en los botones
        start_screen.blit(faciltx, facilrect)
        start_screen.blit(mediotx,mediorect)
        start_screen.blit(dificiltx, dificilrect)

        pygame.display.flip()

# Función para revelar celdas
def revelarminas(row, col):
    if 0 <= row < FILAS and 0 <= col < COLUMNAS:
        if revelar[row][col]:
            return
        revelar[row][col] = True
        if tablero[row][col] == 0:
            for i in range(row - 1, row + 2):
                for j in range(col - 1, col + 2):
                    revelarminas(i, j)
        elif tablero[row][col] == -1:
            game_over()
        return

# Definir funciones para mostrar mensajes
def mensajefinal(mensaje):
    y=130
    font = pygame.font.Font(None, 42)
    linea=mensaje.split("\n")
    for linea in linea:
        text = font.render(linea, True, BLACK, RED)
        screen.blit(text, (10,y))
        y+=font.get_height()+10
    pygame.display.flip()

#Función para manejar el final del juego
def game_over():
    for row in range(FILAS):
        for col in range(COLUMNAS):
            revelar[row][col] = True

# Bucle principal del juego
while True:
    # Obtener cantidad de minas seleccionada desde la ventana de inicio
    cantidadminas = start_screen()
    #conteo de tiempo
    iniciotiempo=time.time()

    # Configuración del juego
    if cantidadminas==10:
        FILAS, COLUMNAS = 8, 8
    elif cantidadminas==25:
        FILAS,COLUMNAS= 12,12
        WIDTH, HEIGHT = 600, 600
    elif cantidadminas==35:
        FILAS,COLUMNAS=15,15
        WIDTH, HEIGHT = 600, 600


    tamañocelda = WIDTH // COLUMNAS

    # Crear el tablero del juego
    tablero = [[0 for _ in range(COLUMNAS)] for _ in range(FILAS)]
    minas = random.sample(range(FILAS * COLUMNAS), cantidadminas)
    for pos in minas:
        row = pos // COLUMNAS
        col = pos % COLUMNAS
        tablero[row][col] = -1
        for i in range(row - 1, row + 2):
            for j in range(col - 1, col + 2):
                if 0 <= i < FILAS and 0 <= j < COLUMNAS and tablero[i][j] != -1:
                    tablero[i][j] += 1

    running = True
    # Inicializar la matriz de celdas reveladas
    revelar = [[False for _ in range(COLUMNAS)] for _ in range(FILAS)]

    pygame.display.flip()


    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    col = event.pos[0] // tamañocelda
                    row = event.pos[1] // tamañocelda
                    revelarminas(row, col)

    # Comprobar si todas las celdas sin minas han sido reveladas
        all_cells_revealed = all(all(revelar[row][col] or tablero[row][col] == -1 for col in range(COLUMNAS)) for row in range(FILAS))
        
        # Dibujar el tablero
        screen.fill(WHITE)

        for row in range(FILAS):
            for col in range(COLUMNAS):
                cell = pygame.Rect(col * tamañocelda, row * tamañocelda, tamañocelda, tamañocelda)
                pygame.draw.rect(screen, GRAY, cell)
                if revelar[row][col]:
                    if tablero[row][col] == -1:
                        pygame.draw.rect(screen, BLACK, cell)
                    else:
                        font = pygame.font.Font(None, 36)
                        text = font.render(str(tablero[row][col]), True, BLACK)
                        text_rect = text.get_rect(center=cell.center)
                        screen.blit(text, text_rect)
                if not revelar[row][col]:
                    pygame.draw.rect(screen, BLACK, cell, 1)  # Dibujar contorno de celda
                    
        
        
    # Comprobar condiciones de victoria y derrota
        if any(revelar[row][col] and tablero[row][col] == -1 for row in range(FILAS) for col in range(COLUMNAS)):
            finaltiempo=time.time()
            resta=finaltiempo-iniciotiempo
            tiempo="{:.2f}".format(resta)
            mensajefinal(f"¡Perdiste! \nTu tiempo fue de {tiempo} seg.")
            pygame.display.flip()
            pygame.time.delay(3000)
            break
        elif all_cells_revealed:
            finaltiempo=time.time()
            resta=finaltiempo-iniciotiempo
            tiempo="{:.2f}".format(resta)
            mensajefinal(f"¡Felicitaciones, ganaste!\nTu tiempo fue de {tiempo} seg.")
            pygame.display.flip()
            pygame.time.delay(5000)
            break




    
        pygame.display.flip()

# Cerrar Pygame
pygame.quit()
