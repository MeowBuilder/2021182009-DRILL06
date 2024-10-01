from pico2d import *
from random import randint

TUK_WIDTH, TUK_HEIGHT = 1280, 1024
open_canvas(TUK_WIDTH, TUK_HEIGHT)

TUK_ground = load_image('TUK_GROUND.png')
character = load_image('animation_sheet.png')
cursor = load_image('hand_arrow.png')


def handle_events():
    pass

def random_cursor():
    pass


def print_screen():
    pass
    
running = True
x, y = TUK_WIDTH // 2, TUK_HEIGHT // 2
dx,dy = x,y
frame = 0

while running:
        print_screen()
        handle_events()
    random_cursor()

close_canvas()




