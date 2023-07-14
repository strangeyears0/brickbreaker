import pygame
from settings import *
from random import choice

class Player(pygame.sprite.Sprite):
    def __init__(self,groups):
        super().__init__(groups)

        #setup
        self.image = pygame.Surface((WINDOW_WIDTH // 10, WINDOW_HEIGHT // 20))
        self.image.fill('black')

        #position
        self.rect = self.image.get_rect(midbottom = (WINDOW_WIDTH // 2, WINDOW_HEIGHT - 20))
        # create old rect
        self.old_rect = self.rect.copy()
        self.direction = pygame.math.Vector2()
        self.speed = 300
        self.pos = pygame.math.Vector2(self.rect.topleft)
    def input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT]:
            self.direction.x = 1
        elif keys[pygame.K_LEFT]:
            self.direction.x = -1
        else:
            self.direction.x = 0
    def screen_constraint(self):
        if self.rect.right > WINDOW_WIDTH:
            self.rect.right = WINDOW_WIDTH
            self.pos.x = self.rect.x
        if self.rect.left < 0:
            self.rect.left = 0
            self.pos.x = self.rect.x
    def update(self,dt):
        self.old_rect = self.rect.copy()
        self.input()
        self.pos.x += self.direction.x * self.speed * dt
        self.rect.x = round(self.pos.x)
        self.screen_constraint()

class Ball(pygame.sprite.Sprite):
    def __init__(self,groups,player):
        super().__init__(groups)

        #collision objects
        self.player = player

        #graphic setup

        self.image = pygame.image.load('../graphics/ball/ball.png').convert_alpha()

        #position setup
        self.rect = self.image.get_rect(midbottom = player.rect.midtop)
        self.old_rect = self.rect.copy()
        self.direction = pygame.math.Vector2((choice((1,-1)),-1))
        self.pos = pygame.math.Vector2(self.rect.topleft)
        self.speed = 400

        #active
        self.active = False
    def window_collision(self,direction):
        if direction == 'horizontal1':
            if self.rect.left < 0:
                self.rect.left = 0
                self.pos.x = self.rect.x
                self.direction.x *= -1

            if self.rect.right > WINDOW_WIDTH :
                self.rect.right = WINDOW_WIDTH
                self.pos.x = self.rect.x
                self.direction.x *= -1

        if direction == 'vertical1':
            if self.rect.top < 0:
                self.rect.top = 0
                self.pos.y = self.rect.y
                self.direction.y *= -1

            if self.rect.bottom > WINDOW_HEIGHT :
                self.active = False
                self.direction.y = -1

    def collision(self,direction):
        #find overlapping objects
        overlap_sprites = []
        if self.rect.colliderect(self.player.rect):
            overlap_sprites.append(self.player)

        if overlap_sprites:
            if direction ==  'horizontal1':
                for sprite in overlap_sprites:
                    if self.rect.right >= sprite.rect.left and self.old_rect.right <= sprite.old_rect.left:
                        self.rect.right = sprite.rect.left
                        self.pos.x = self.rect.x
                        self.direction.x *= -1

                    if self.rect.left <= sprite.rect.right and self.old_rect.left >= sprite.old_rect.right:
                        self.rect.left = sprite.rect.right
                        self.pos.x = self.rect.x
                        self.direction.x *= -1
            if direction == 'vertical1':
                for sprite in overlap_sprites:
                    if self.rect.bottom >= sprite.rect.top and self.old_rect.bottom <= sprite.old_rect.top:
                        self.rect.bottom = sprite.rect.top
                        self.pos.y = self.rect.y
                        self.direction.y *= -1

                    if self.rect.top <= sprite.rect.bottom and self.old_rect.top >= sprite.old_rect.bottom:
                        self.rect.top = sprite.rect.bottom
                        self.pos.y = self.rect.y
                        self.direction.y *= -1


    def update(self,dt):
        if self.active:

            if self.direction.magnitude() != 0:
                self.direction = self.direction.normalize()
            #create old rect
            self.old_rect = self.rect.copy()

            #horizontal movement + collision
            self.pos.x += self.direction.x * self.speed * dt
            self.rect.x = round(self.pos.x)
            self.collision('horizontal1')
            self.window_collision('horizontal1')

            # vertical movement + collision
            self.pos.y += self.direction.y * self.speed * dt
            self.rect.y = round(self.pos.y)
            self.collision('vertical1')
            self.window_collision('vertical1')

        else:
            self.rect.midbottom = self.player.rect.midtop
            self.pos = pygame.math.Vector2(self.rect.topleft)