import pygame
from settings import SPRITE_WIDTH, SPRITE_HEIGHT, CELL_SIZE

class sprite_sheet:
    def __init__(self, filename):
        self.sheet = pygame.image.load(filename).convert_alpha()

    def get_sprite(self, index):
        image = pygame.Surface((SPRITE_WIDTH, SPRITE_HEIGHT))
        image.fill((127, 127, 127))
        image.blit(self.sheet, (0, 0), ((index % 6) * SPRITE_WIDTH, (index // 6) * SPRITE_HEIGHT, SPRITE_WIDTH, SPRITE_HEIGHT))
        image = pygame.transform.scale(image, (CELL_SIZE, CELL_SIZE))
        image.set_colorkey((127, 127, 127))
        return image
    
if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode((CELL_SIZE, CELL_SIZE))
    sheet = sprite_sheet('assets/Chess_kdl45.svg')
    screen.blit(sheet.get_sprite(0), (0, 0))
    run = True

    while run:

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

    pygame.quit()