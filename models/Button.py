import pygame
import os

class Button:
    def __init__(self, x, y, width, height, text, action):
        self.action = action
        self.x = x
        self.y = y
        self.text = text
        pygame.font.init()
        
        self.font = pygame.font.Font(os.path.join('resources', 'font', 'font.ttf'), 15)
        self.rect = pygame.Rect(x, y, width, height)

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                if self.rect.collidepoint(event.pos):
                    print('Button clicked')
                    self.action()

    def render(self, screen):
        color = (0,0,0)
        pygame.draw.rect(screen, color, self.rect, 4)
        text_surface = self.font.render(self.text, False, color)
        screen.blit(text_surface, (self.x, self.y))

