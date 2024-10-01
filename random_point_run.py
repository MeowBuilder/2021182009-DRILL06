from pico2d import *
from random import randint

TUK_WIDTH, TUK_HEIGHT = 1280, 1024
open_canvas(TUK_WIDTH, TUK_HEIGHT)

TUK_ground = load_image('TUK_GROUND.png')
character = load_image('animation_sheet.png')
cursor = load_image('hand_arrow.png')


def handle_events():
    global running
    global x, y, dx,dy
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_a:
            random_cursor()
    pass

def random_cursor():
    global dx,dy
    dx = randint(0,TUK_WIDTH)
    dy = randint(0,TUK_HEIGHT)
    pass


def print_screen():
    global frame
    clear_canvas()
    TUK_ground.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)
    if dx < x:
        character.clip_composite_draw(frame * 100, 100 * 1, 100, 100,0,'h', x, y,100,100)
    else:
        character.clip_draw(frame * 100, 100 * 1, 100, 100, x, y,100,100)
    cursor.clip_draw(0,0,50,52,dx,dy)
    update_canvas()
    frame = (frame + 1) % 8
    pass
    
running = True
x, y = TUK_WIDTH // 2, TUK_HEIGHT // 2
dx,dy = x,y
frame = 0

while running:
        print_screen()
        handle_events()
        delay(0.05)
    random_cursor()

close_canvas()




