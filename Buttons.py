import pygame

class Button():
    def __init__(self, x, y, image, scale):
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

    def draw(self, surface, events):   # ✅ mit "events"
        action = False
        pos = pygame.mouse.get_pos()

        if self.rect.collidepoint(pos):
            for event in events:
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    action = True

        surface.blit(self.image, (self.rect.x, self.rect.y))
        return action