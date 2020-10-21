import pygame
from checkers.constants import WIDTH, HEIGHT
from checkers.board import Board

FPS = 60

pygame.init()
WIN = pygame.display.set_mode((WIDTH, HEIGHT))


def main():
    run = True
    clock = pygame.time.Clock()
    board = Board()
    while run:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                print("down")
                pass
        board.draw(WIN)
        pygame.display.update()


main()
