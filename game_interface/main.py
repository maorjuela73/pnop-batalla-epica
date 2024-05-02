import pygame
import sys
from game_logic.character import Character
from game_logic.battle import Battle

# Inicialización de Pygame
pygame.init()

# Constantes de pantalla
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Batalla Épica')

# Colores
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Fuentes
font = pygame.font.Font(None, 36)

# Cargar imágenes
hero_image = pygame.image.load('assets/images/hero.png').convert_alpha()
monster_image = pygame.image.load('assets/images/monster.png').convert_alpha()
background_image = pygame.image.load('assets/images/background.jpg').convert()

# Reescalar imágenes
hero_image = pygame.transform.scale(hero_image, (150, 150))
monster_image = pygame.transform.scale(monster_image, (150, 150))

# Posiciones de los sprites
hero_pos = (150, 250)
monster_pos = (550, 250)

# Crear personajes y batalla
hero = Character("Héroe", 100, 20)
monster = Character("Monstruo", 80, 15)
battle = Battle(hero, monster)

def draw_health_bar(character, x, y, width, height):
    health_percentage = character.health / 100
    pygame.draw.rect(screen, RED, (x, y, width, height))
    pygame.draw.rect(screen, GREEN, (x, y, width * health_percentage, height))

def main():
    clock = pygame.time.Clock()
    running = True

    while running:
        # Dibuja la imagen de fondo
        screen.blit(background_image, (0, 0))
        
        # Dibuja los sprites
        screen.blit(hero_image, hero_pos)
        screen.blit(monster_image, monster_pos)

        # Dibuja las barras de salud
        draw_health_bar(hero, 100, 200, 200, 20)
        draw_health_bar(monster, 500, 200, 200, 20)
        
        # Manejar eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    battle.start_battle()

        # Actualizar pantalla
        pygame.display.flip()
        clock.tick(30)

    pygame.quit()
    sys.exit()

if __name__ == '__main__':
    main()
