import pygame 

def show(info, x=10, y=10, size=50, color=(255, 255, 255), background=(0, 0, 0)):
    font = pygame.font.Font(None, size)

    display_surface = pygame.display.get_surface()
    debug_surf = font.render(str(info), True, color)
    debug_rect = debug_surf.get_rect(topleft = (x, y))
    pygame.draw.rect(display_surface, background, debug_rect)
    display_surface.blit(debug_surf, debug_rect)