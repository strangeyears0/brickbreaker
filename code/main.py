import pygame, sys, time
from settings import *
from sprites import Player, Ball

class Game:
    def __init__(self):

        #General setup
        pygame.init()
        self.display_surface = pygame.display.set_mode((WINNDOW_WIDTH,WINDOW_HEIGHT))
        pygame.display.set_caption("Brick Breaker")

        #background
        self.bg = self.create_bg()

        #sprite group setup
        self.all_sprites = pygame.sprite.Group()

        # setup
        self.player = Player(self.all_sprites)
        self.ball = Ball(self.all_sprites,self.player)
    def create_bg(self):
        bg_original = pygame.image.load("../graphics/background/wepik-export-20230712175345mPfb.png").convert()
        scaled_bg = pygame.transform.scale(bg_original,(WINNDOW_WIDTH,WINDOW_HEIGHT))
        return scaled_bg
    def run(self):
        last_time = time.time()
        while True:

            #Delta time
            dt = time.time() - last_time
            last_time=time.time()

            #event loop
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.ball.active = True

            #UPDATE THE GAME
            self.all_sprites.update(dt)
            #draw the frame
            self.display_surface.blit(self.bg,(0,0))
            self.all_sprites.draw(self.display_surface)
            #update window
            pygame.display.update()

if __name__ == '__main__':
    game = Game()
    game.run()

