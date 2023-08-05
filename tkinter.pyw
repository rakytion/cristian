import pygame
#tamaño de pantalla y tablero
width=400
height=400
rows, cols=10, 10
cell_size= width // rows
  #colores
BLANCO=(255, 255, 255)
NEGRO=(0, 0, 0)
#ventana del juego
window= pygame.display.set_mode((width, height))
pygame.display.set_caption("BUSCAMINAS")
while True:
  for event in pygame.event.get():
    if event.type==pygame.QUIT:
      pygame.quit()
      quit()
        