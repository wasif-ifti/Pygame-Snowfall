# main.py
# Name: Wasif Islam
# Description: Animated snowfall using Pygame
#   SPACE = pause / resume the snow
#   Q     = quit

import asyncio
import random
import pygame
from drawable import Rectangle, Snowflake

WIDTH = 500
HEIGHT = 500
GROUND_Y = 300


async def main():
    pygame.init()
    surface = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Snowfall")
    clock = pygame.time.Clock()

    sky = Rectangle(0, 0, WIDTH, GROUND_Y, (0, 0, 255))
    ground = Rectangle(0, GROUND_Y, WIDTH, HEIGHT - GROUND_Y, (0, 255, 0))
    drawables = [sky, ground]

    running = True
    animationRunning = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    running = False
                elif event.key == pygame.K_SPACE:
                    animationRunning = not animationRunning

        if animationRunning:
            # Add a new snowflake at a random spot along the top
            x = random.randint(0, WIDTH)
            drawables.append(Snowflake(x, 0, random.randint(3, 6),
                                       random.randint(1, 3)))

            # Keep the scene from slowing down: once there's a lot of snow,
            # drop the oldest flake (index 2, right after the sky and ground)
            if len(drawables) > 1500:
                drawables.pop(2)

            # Move every snowflake down; landed ones stay on the ground
            for item in drawables:
                if isinstance(item, Snowflake):
                    landingY = GROUND_Y + random.randint(0, 15)
                    item.fall(landingY)

        for item in drawables:
            item.draw(surface)

        pygame.display.update()
        clock.tick(30)
        await asyncio.sleep(0)  # lets the game run in a web browser too

    pygame.quit()


if __name__ == "__main__":
    asyncio.run(main())
