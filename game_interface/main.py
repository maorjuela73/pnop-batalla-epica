import pygame
import sys
from game_logic.character import Character
from game_logic.battle import Battle

# Clase para manejar los sprites de los personajes
class CharacterSprite(pygame.sprite.Sprite):
    def __init__(self, image, pos):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect(center=pos)

    def update(self):
        pass

# Inicialización de Pygame
pygame.init()

# Constantes de pantalla
SCREEN_WIDTH, SCREEN_HEIGHT = 1050, 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Epic Battle Simulator')

# Colores
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
RED_BAR = (180, 37, 62)
BLACK = (0, 0, 0)

# Fuentes
retro_font = pygame.font.Font('assets/fonts/pixel_font.ttf', 18, bold=True)

# Cargar imágenes
background_image = pygame.image.load('assets/images/background.png').convert()
message_box = pygame.image.load('assets/images/message_box.png').convert_alpha()

# Cargar la imagen del sprite
hero_sprite_sheet = pygame.image.load('assets/sprites/idle.png').convert_alpha()

# Dividir la imagen en fotogramas
hero_frames = []
frame_width = 128
frame_height = 128

for i in range(4):
    frame = hero_sprite_sheet.subsurface(pygame.Rect(i * frame_width ,0 , frame_width, frame_height))
    # Escalar el fotograma a 150x150
    frame = pygame.transform.scale(frame, (300, 300))
    hero_frames.append(frame)
    
# Control de animación
current_frame = 0
frame_rate = 8  # Cambiar el fotograma cada 6 actualizaciones
frame_count = 0

# Escalar imágenes
message_box = pygame.transform.scale(message_box, (message_box.get_width() // 2.5, message_box.get_height() // 2.5))

# Posiciones de los sprites
hero_pos = (340, 254)
monster_pos = (550, 350)
message_box_pos = (180, 115)

# Crear personajes y batalla
hero = Character("Héroe", 100, 20)
monster = Character("Monstruo", 80, 15)
battle = Battle(hero, monster)

def draw_health_bar(character, x, y, width, height):
    health_percentage = max(character.health, 0) / 100
    pygame.draw.rect(screen, BLACK, (x, y, width, height))
    pygame.draw.rect(screen, RED_BAR, (x, y, width * health_percentage, height))

def main():
    global frame_count, current_frame
    clock = pygame.time.Clock()
    running = True
    in_battle = True
    damage_messages = []

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and in_battle:
                    player_alive, enemy_alive = battle.perform_turn(damage_messages)
                    if not player_alive or not enemy_alive:
                        in_battle = False


        # Actualizar fotograma de animación
        frame_count += 1
        if frame_count >= frame_rate:
            frame_count = 0
            current_frame = (current_frame + 1) % 4  # Ciclar a través de los 6 fotogramas

        # Actualizar la interfaz gráfica
        screen.blit(background_image, (0, 0))

        screen.blit(hero_frames[current_frame], hero_pos)

        draw_health_bar(hero, 142, 41, 306, 15)
        draw_health_bar(monster, 603, 41, 308, 15)

        # Mostrar mensajes de daño
        screen.blit(message_box, message_box_pos)
        y_offset = 40
        for message in damage_messages[-2:]:  # Mostrar solo los últimos 2 mensajes
            damage_surf = retro_font.render(message, True, BLACK)
            screen.blit(damage_surf, (388 - damage_surf.get_width() / 2, 140 + y_offset))
            y_offset += 20

        pygame.display.flip()
        clock.tick(30)

    pygame.quit()
    sys.exit()

if __name__ == '__main__':
    main()
