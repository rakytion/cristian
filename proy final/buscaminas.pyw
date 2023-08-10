import pygame
import random

# Inicializar Pygame
pygame.init()

# Configuración del juego
WIDTH, HEIGHT = 400, 400
ROWS, COLS = 8, 8
MINE_COUNT = 10
CELL_SIZE = WIDTH // COLS

# Colores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)
RED = (255, 0, 0)

# Definir dimensiones y posición del botón de reinicio
RESET_BUTTON_WIDTH = 120
RESET_BUTTON_HEIGHT = 40
RESET_BUTTON_X = (WIDTH - RESET_BUTTON_WIDTH) // 2
RESET_BUTTON_Y = HEIGHT - RESET_BUTTON_HEIGHT - 10
reset_button_rect = pygame.Rect(RESET_BUTTON_X, RESET_BUTTON_Y, RESET_BUTTON_WIDTH, RESET_BUTTON_HEIGHT)


# Inicializar la ventana
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Buscaminas")

# Crear el tablero del juego
board = [[0 for _ in range(COLS)] for _ in range(ROWS)]
mines = random.sample(range(ROWS * COLS), MINE_COUNT)
for pos in mines:
    row = pos // COLS
    col = pos % COLS
    board[row][col] = -1
    for i in range(row - 1, row + 2):
        for j in range(col - 1, col + 2):
            if 0 <= i < ROWS and 0 <= j < COLS and board[i][j] != -1:
                board[i][j] += 1

# Función para revelar celdas
def reveal(row, col):
    if 0 <= row < ROWS and 0 <= col < COLS:
        if revealed[row][col]:
            return
        revealed[row][col] = True
        if board[row][col] == 0:
            for i in range(row - 1, row + 2):
                for j in range(col - 1, col + 2):
                    reveal(i, j)
        elif board[row][col] == -1:
            game_over()
        return

# Definir funciones para mostrar mensajes
def show_message(message):
    font = pygame.font.Font(None, 48)
    text = font.render(message, True, RED)
    text_rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
    screen.blit(text, text_rect)
    pygame.display.flip()

# Función para manejar el final del juego
def game_over():
    for row in range(ROWS):
        for col in range(COLS):
            revealed[row][col] = True

# Inicializar la matriz de celdas reveladas
revealed = [[False for _ in range(COLS)] for _ in range(ROWS)]

# Definir función para reiniciar el juego
def restart_game():
    global revealed, board
    revealed = [[False for _ in range(COLS)] for _ in range(ROWS)]
    board = [[0 for _ in range(COLS)] for _ in range(ROWS)]
    mines = random.sample(range(ROWS * COLS), MINE_COUNT)
    for pos in mines:
        row = pos // COLS
        col = pos % COLS
        board[row][col] = -1
        for i in range(row - 1, row + 2):
            for j in range(col - 1, col + 2):
                if 0 <= i < ROWS and 0 <= j < COLS and board[i][j] != -1:
                    board[i][j] += 1


# Bucle principal del juego
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                col = event.pos[0] // CELL_SIZE
                row = event.pos[1] // CELL_SIZE
                reveal(row, col)

  # Comprobar si todas las celdas sin minas han sido reveladas
    all_cells_revealed = all(all(revealed[row][col] or board[row][col] == -1 for col in range(COLS)) for row in range(ROWS))
    

    # Dibujar el tablero
    screen.fill(WHITE)
    for row in range(ROWS):
        for col in range(COLS):
            cell = pygame.Rect(col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE)
            pygame.draw.rect(screen, GRAY, cell)
            if revealed[row][col]:
                if board[row][col] == -1:
                    pygame.draw.rect(screen, BLACK, cell)
                else:
                    font = pygame.font.Font(None, 36)
                    text = font.render(str(board[row][col]), True, BLACK)
                    text_rect = text.get_rect(center=cell.center)
                    screen.blit(text, text_rect)
            if not revealed[row][col]:
                pygame.draw.rect(screen, BLACK, cell, 1)  # Dibujar contorno de celda
                
    
    
 # Comprobar condiciones de victoria y derrota
    if any(revealed[row][col] and board[row][col] == -1 for row in range(ROWS) for col in range(COLS)):
        show_message("¡Perdiste!")
        pygame.draw.rect(screen, GRAY, reset_button_rect)  # Dibujar el botón de reinicio
        pygame.display.flip()
        pygame.time.delay(2000)
        restart_game()
    elif all_cells_revealed:
        show_message("¡Felicitaciones, ganaste!")
        pygame.draw.rect(screen, GRAY, reset_button_rect)  # Dibujar el botón de reinicio
        pygame.display.flip()
        pygame.time.delay(2000)
        restart_game()


    # Dibujar el botón de reinicio
    pygame.draw.rect(screen, GRAY, reset_button_rect)
    restart_font = pygame.font.Font(None, 24)
    restart_text = restart_font.render("Volver a jugar", True, BLACK)
    restart_text_rect = restart_text.get_rect(center=(RESET_BUTTON_X + RESET_BUTTON_WIDTH // 2, RESET_BUTTON_Y + RESET_BUTTON_HEIGHT // 2))
    screen.blit(restart_text, restart_text_rect)
    
    pygame.display.flip()

    # Comprobar eventos del botón de reinicio
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if pygame.Rect(RESET_BUTTON_X, RESET_BUTTON_Y, RESET_BUTTON_WIDTH, RESET_BUTTON_HEIGHT).collidepoint(event.pos):
                restart_game()

# Cerrar Pygame
pygame.quit()
