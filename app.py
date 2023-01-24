import pygame
from settings import *
from sprite_sheet import sprite_sheet

def decifer_FEN(fen_string, sheet, screen):
    x = y = 0
    for i in range(len(fen_string)):
        if fen_string[i] == '/':
            y += 1
            x = 0
        if '0' <= fen_string[i] and fen_string[i] <= '8':
            x += int(fen_string[i])
        if fen_string[i] in PIECES:
            screen.blit(sheet.get_sprite(PIECES.index(fen_string[i]), SPRITE_WIDTH, SPRITE_HEIGHT, 2), (x * CELL_SIZE, y * CELL_SIZE))
            x += 1
    return screen

def main():
    pygame.init()

    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

    pygame.display.set_caption("ChessBoard")

    for x in range(8):
        for y in range(8):
            if (x + y) % 2:
                pygame.draw.rect(screen, Color.Black, (x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE))
            else:
                pygame.draw.rect(screen, Color.White, (x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE))
                
    sheet = sprite_sheet('assets/Chess_Pieces_Sprite.svg')

    fen = 'rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR'

    screen = decifer_FEN(fen, sheet, screen)

    run = True

    while run:

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

    pygame.quit()

if __name__ == '__main__':
    main()