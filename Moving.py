
import pygame
from pygame.locals import *

import time

import random


size=40
#background_color=(139, 181, 172, 1)
class Apple():
    def __init__(self,parent_floor):
        self.parent_floor=parent_floor
        self.image=pygame.image.load("apple.jpg").convert()
        self.pamuux=size*3
        self.pamuuy=size*3
    def draw(self):
        self.parent_floor.blit(self.image, (self.pamuux, self.pamuuy))  # where the blocker should be
        pygame.display.flip()
    def move(self):
        self.pamuux = random.randint(1,24)*size
        self.pamuuy = random.randint(1,19)*size

class Snake():
    def __init__(self,parent_floor,length):
        #self.length=length
        self.parent_floor=parent_floor
        self.pamuu = pygame.image.load("block.jpg").convert()
        self.direction = 'down'
        self.length = length
        self.pamuux = [size]*length
        self.pamuuy = [size]*length
        #self.direction='down'
    def increase_length(self):
        self.length+=1
        self.pamuux.append(-1)
        self.pamuuy.append(-1)
    def draw(self):
        #self.parent_floor.fill(background_color)
        for i in range(self.length):

            self.parent_floor.blit(self.pamuu, (self.pamuux[i], self.pamuuy[i]))  # where the blocker should be
        pygame.display.flip()
    def move_left(self):
        self.direction='left'

    def move_right(self):
        self.direction='right'

    def move_up(self):
        self.direction='up'

    def move_down(self):
        self.direction='down'

    def walk(self):
        for i in range(self.length-1,0,-1):
            self.pamuux[i]=self.pamuux[i - 1]
            self.pamuuy[i]=self.pamuuy[i - 1]
        if self.direction == 'up':
            self.pamuuy[0] -= size
        if self.direction == 'down':
            self.pamuuy[0] += size
        if self.direction == 'right':
            self.pamuux[0] += size
        if self.direction == 'left':
            self.pamuux[0] -=size

        self.draw()



class Game():
    def __init__(self):
        pygame.init()
        pygame.mixer.init()
        self.background_music()
        pygame.display.set_caption("Snake and Apple Game")

        self.floor = pygame.display.set_mode(size=(1000, 800))  # setting display size
        self.floor.fill(color=(139, 181, 172, 1))  # filling the color of the whole display
        self.Snake=Snake(self.floor,1)
        self.Snake.draw()
        self.apple=Apple(self.floor)
        self.apple.draw()
        #initialization of music
        # pygame.mixer.init()
        # self.background_music()   #background music
    def display_score(self):
        font = pygame.font.SysFont('arial', 30)
        score = font.render(f"score:{self.Snake.length}", True, (255, 255, 255))
        self.floor.blit(score, (800, 10))


    def is_collision(self,x1,y1,x2,y2): #increaseing snake size
        if x1>=x2 and x1<x2+size:
            if y1>=y2 and y1<y2+size:
                return True
        return False

    def background_music(self):
        pygame.mixer.music.load("C:/Users/kolup/OneDrive/Desktop/snake/nagin.mp3")
        pygame.mixer.music.play()

    def play_sound(self):
        sound=pygame.mixer.Sound("C:/Users/kolup/OneDrive/Desktop/snake/ding.mp3")
        pygame.mixer.Sound.play(sound)
    # def background_music(self):
    #     pygame.mixer.music.load("C:/Users/kolup/OneDrive/Desktop/snake/nagin.mp3")
    #     pygame.mixer.music.play()
    def background_image(self):
        bg=pygame.image.load("C:/Users/kolup/OneDrive/Desktop/snake/background.jpg")
        self.floor.blit(bg,(0,0))


    def play(self):
        self.background_image()
        self.Snake.walk()
        self.apple.draw()
        self.display_score()

        pygame.display.flip()

        # snake colliding with apple
        if self.is_collision(self.Snake.pamuux[0],self.Snake.pamuuy[0],self.apple.pamuux,self.apple.pamuuy):
            self.play_sound()
            self.Snake.increase_length()
            self.apple.move()


        #colliding with itself (snake eating itself)
        for i in range(2,self.Snake.length):
            if self.is_collision(self.Snake.pamuux[0],self.Snake.pamuuy[0],self.Snake.pamuux[i],self.Snake.pamuuy[i]):
                raise "GameOver"
    def show_game_over(self):

        font = pygame.font.SysFont('arial', 30)
        line1 = font.render(f"score:{self.Snake.length}", True, (255, 255, 255))
        self.floor.blit(line1,(200,300))
        line2=font.render("To play again press enter and to quit press escape",True,(255,255,255))
        self.floor.blit(line2,(200,350))
        pygame.display.flip()
        pygame.mixer.music.pause()
    def reset(self):
        self.Snake = Snake(self.floor, 1)
        self.apple = Apple(self.floor)






    def run(self):
        run = True
        pause=False
        while run:  # while loop is for screen stay until the user enter esc or wrong it will stay
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        run = False
                    if event.key == K_RETURN:
                        pygame.mixer.music.unpause()
                        pause=False
                    if not pause:
                        if event.key == K_UP:
                            self.Snake.move_up()

                        if event.key == K_DOWN:
                            self.Snake.move_down()

                        if event.key == K_LEFT:
                            self.Snake.move_left()
                        if event.key == K_RIGHT:
                            self.Snake.move_right()


                elif event.type == QUIT:
                    run=False


            try:
                if not pause:


                    self.play()

            except Exception as e:
                self.show_game_over()
                pause = True
                self.reset()
            time.sleep(0.2)


if __name__=="__main__":
    game=Game()
    game.run()
