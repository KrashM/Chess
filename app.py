import pygame
from settings import *
from sprite_sheet import sprite_sheet

def decifer_FEN(fen_string, sheet, screen):
    x = y = i = 0
    while fen_string[i] != ' ':
        if fen_string[i] == '/':
            y += 1
            x = 0
        elif fen_string[i] in PIECES:
            screen.blit(sheet.get_sprite(PIECES.index(fen_string[i])), (x * CELL_SIZE, y * CELL_SIZE))
            x += 1
        else:
            x += int(fen_string[i])
        i += 1

    rest = fen_string[i :].split()
    to_move = rest[0] == 'w'
    can_castle = ['K' in rest[1], 'Q' in rest[1], 'k' in rest[1], 'q' in rest[1]]
    en_passant_exist = rest[2]
    half_moves, full_moves = map(int, rest[3 :])

    return screen, to_move, can_castle, en_passant_exist, half_moves, full_moves

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

    sheet = sprite_sheet(SPRITE_SHEET_NAME)
    screen, to_move, can_castle, en_passant_exist, half_moves, full_moves = decifer_FEN(STARTING_POSITION, sheet, screen)

    run = True

    while run:

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                print("Mouse clicked")
            if event.type == pygame.QUIT:
                run = False

    pygame.quit()

if __name__ == '__main__':
    main()