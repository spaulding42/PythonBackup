import spritesheet
import pygame
pygame.init()

pygame.font.init()

WIDTH, HEIGHT = 1000,500
FLOOR = HEIGHT - 100
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Devio")

#Background sprites
SKY = pygame.transform.scale(pygame.image.load('assets/sky.png'), (WIDTH, HEIGHT-100))
GROUND = pygame.transform.scale(pygame.image.load('assets/ground_full.png'), (WIDTH, 100))
BLACK_BACKGROUND = pygame.transform.scale(pygame.image.load('assets/black_background.png'), (WIDTH, HEIGHT))

#Object sprites
BRICK = pygame.transform.scale(pygame.image.load('assets/brick.png'), (50,50))
STONE = pygame.transform.scale(pygame.image.load('assets/stone.png'), (50,50))
EDIT_BLOCK = pygame.transform.scale(pygame.image.load('assets/edit_block.png'), (50,50))
END_DOOR = pygame.transform.scale(pygame.image.load('assets/End_Door.png'), (50,100))
SPIKEY_BRICK = pygame.transform.scale(pygame.image.load('assets/spikeybrick.png'), (50,50))

DEVIO_RIGHT_JUMPING = pygame.transform.scale(pygame.image.load('assets/Devio_jump.png'), (45,95))
DEVIO_LEFT_JUMPING = pygame.transform.flip(pygame.transform.scale(pygame.image.load('assets/Devio_jump.png'), (45,95)), True, False)

DEVIO_SPRITE_STANDING = pygame.image.load('assets/Devio_standing_sprite.png').convert_alpha()
DEVIO_SPRITE_SHEET_STANDING = spritesheet.SpriteSheet(DEVIO_SPRITE_STANDING)
DEVIO_SPRITE_WALKING = pygame.image.load('assets/Devio_walking_sprite.png').convert_alpha()
DEVIO_SPRITE_SHEET_WALKING = spritesheet.SpriteSheet(DEVIO_SPRITE_WALKING)
DEVIO = DEVIO_SPRITE_SHEET_WALKING.get_image(0,45,100)


#ENEMY SPRITES
ANGRY_BRICK = pygame.transform.scale(pygame.image.load('assets/angrybrick.png'),(100,100))
JUMPER_GUY_SPRITE_WALKING = pygame.image.load('assets/kangaroo_walking_sprite.png').convert_alpha()
JUMPER_GUY_SPRITE_SHEET_WALKING = spritesheet.SpriteSheet(JUMPER_GUY_SPRITE_WALKING)
JUMPER_GUY = JUMPER_GUY_SPRITE_SHEET_WALKING.get_image(0,45,100)
TURTLE_SPRITE = pygame.image.load('assets/turtle_sprite1.png').convert_alpha()
TURTLE_SPRITE_SHEET = spritesheet.SpriteSheet(TURTLE_SPRITE)
TURTLE = TURTLE_SPRITE_SHEET.get_image(0, 75,50)

#Sound files
JUMP_SOUND = pygame.mixer.Sound('assets/sounds/jump.wav')
HIT_ENEMY_SOUND = pygame.mixer.Sound('assets/sounds/enemy_jump.wav')
BREAK_BRICK_SOUND = pygame.mixer.Sound('assets/sounds/brick_break.wav')
DEATH_SOUND = pygame.mixer.Sound('assets/sounds/death.wav')

