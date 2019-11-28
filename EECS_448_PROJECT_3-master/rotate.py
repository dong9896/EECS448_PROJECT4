import pygame
import pygame.font
import math
pygame.init()
size = (400, 400)
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
width = screen.get_width() / 2
height = screen.get_height() / 2

def blitRotate(surf, image, pos, originPos, angle):
    # calcaulate the axis aligned bounding box of the rotated image
    w, h = image.get_size()
    box = [pygame.math.Vector2(p) for p in [(0, 0), (w, 0), (w, -h), (0, -h)]]
    box_rotate = [p.rotate(angle) for p in box]
    min_box = (min(box_rotate, key=lambda p: p[0])[0], min(box_rotate, key=lambda p: p[1])[1])
    max_box = (max(box_rotate, key=lambda p: p[0])[0], max(box_rotate, key=lambda p: p[1])[1])

    # calculate the translation of the pivot
    pivot = pygame.math.Vector2(originPos[0], -originPos[1])
    pivot_rotate = pivot.rotate(40)
    pivot_move = pivot_rotate - pivot

    # calculate the upper left origin of the rotated image
    origin = (pos[0] - originPos[0] + min_box[0] - pivot_move[0], pos[1] - originPos[1] - max_box[1] + pivot_move[1])

    # get a rotated image
    rotated_image = pygame.transform.rotate(image, angle)

    # rotate and blit the image
    surf.blit(rotated_image, origin)



image = pygame.image.load('image/icon.png')

w, h = image.get_size()

angle = 0
done = False
pos = (width, height)
while not done:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                done = True
    if event.type == pygame.KEYDOWN:
        if event.key == ord('a'):
            angle = angle + 10
        if event.key == ord('w'):
            print(math.sin(angle))
            if math.sin(angle) > 0:
                width = width * (1 - math.sin(angle)/100)
                height = height * (1 + math.cos(angle)/100)
            elif math.cos(angle) < 0:
                width = width * (1 + math.sin(angle) / 100)
                height = height * (1 - math.cos(angle) / 100)
        if event.key == ord('d'):
            angle = angle - 10
        if event.key == ord('s'):
            height = (height + 1 )

    pos = (width, height)
    screen.fill(0)

    blitRotate(screen, image, pos, (w / 2, h / 2), angle)

    pygame.display.flip()

pygame.quit()
