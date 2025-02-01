from pygame import *

window = display.set_mode((700, 500))
display.set_caption('Доганялки')
bg = transform.scale(image.load("background.png"), (700, 500))

x1 = 100
y1 = 300

x2 = 300
y2 = 300

sprite1 = transform.scale(image.load("sprite1.png"), (100, 100))
sprite2 = transform.scale(image.load("sprite2.png"), (100, 100))

run = True
clock = time.Clock()
FPS = 60
speed = 10

while run:
    window.blit(bg, (0, 0))
    window.blit(sprite1, (x1, y1))
    window.blit(sprite2, (x2, y2))

    for e in event.get():
        if e.type == QUIT:
            run = False

    key_pressed = key.get_pressed()
    if key_pressed[K_a] and x1 > 5:
        x1 -= speed
    if key_pressed[K_d] and x1 < 595:
        x1 += speed
    if key_pressed[K_w] and x1 > 5:
        y1 -= speed
    if key_pressed[K_s] and x1 < 395:
        y1 += speed


    display.update()
    clock.tick(FPS)

