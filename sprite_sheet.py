import pygame

class sprite_sheet:
    def __init__(self, filename):
        self.sprite = pygame.image.load(filename).convert_alpha()
    
    def get_sprite(self, index, width, height, scale):
        image = pygame.Surface((width, height)).convert_alpha()
        image.fill((0, 255, 0))
        image.blit(self.sprite, (0, 0), ((index % 6) * width, (index // 6) * height, width, height))
        image = pygame.transform.scale(image, (width * scale, height * scale))
        image.set_colorkey((0, 255, 0))
        
        return image