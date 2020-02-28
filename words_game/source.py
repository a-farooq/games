import pygame as pg
from pygame.locals import *


def initialize():
    num = int(input("Number of players: "))
    print(num)

    for i in range(num):
        player = input("Name of player %d: " % (i+1))
        print(player)


class InputBox:
    def __init__(self, x, y, w, h, text=''):
        self.rect = pg.Rect(x, y, w, h)
        self.active = False


def main():
    screen = pg.display.set_mode((800, 600))

    #pygame.display.set_caption("Copyright: Aamil Farooq")

    clock = pg.time.Clock()
    input_box1 = InputBox(100, 100, 140, 32)
    input_box2 = InputBox(100, 300, 140, 32)
    input_boxes = [input_box1, input_box2]
    done = False

    while not done:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                done = True
            for box in input_boxes:
                box.handle_event(event)

        for box in input_boxes:
            box.update()

        screen.fill((30, 30, 30))
        for box in input_boxes:
            box.draw(screen)

        pg.display.flip()
        clock.tick(30)

    #while True:
    #    word = input("Z's turn")

    #    word = input("K's turn")


if __name__ == "__main__":
    pg.init()
    main()
    #initialize()
    pg.quit()
