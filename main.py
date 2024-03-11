import pygame
import random

def new_star():
    return [random.randint(0, screen_width), random.randint(0, screen_height)]


def move_and_check(star):
    star[1] += speed
    if star[1] > screen_height:
        star[1] = 0
        star[0] = random.randint(0, screen_width)
    return star


def draw_star(star):
    pygame.draw.circle(screen, (255, 255, 255), (star[0], star[1]), 2)

screen_width = screen_height = 600

pygame.init()
screen = pygame.display.set_mode((screen_width, screen_height))
done = False

number_of_stars = 100
speed = 0.1
stars = []

for i in range(0, number_of_stars):
    stars.append(new_star())

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    screen.fill((0, 0, 0))

    for i in range(0, number_of_stars):
        s = stars[i]
        s = move_and_check(s)
        stars[i] = s
        draw_star(s)

    pygame.display.flip()
pygame.quit()
